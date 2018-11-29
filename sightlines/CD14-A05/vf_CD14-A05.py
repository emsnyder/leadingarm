import numpy as np
import VoigtFit
import matplotlib
matplotlib.use("GTKAgg")


# -- Add the redshift of the cloud doing the absorption
#    Estimating 0 for everything.
z = 0.0

dataset = VoigtFit.DataSet(z)
dataset.set_name("CD14-A05-SiII")
dataset.verbose = True


# -- If log(NHI) is not known use:
logNHI = None


# -- Rebin the data set by 3 pixels

def downsample_1d(myarr, factor):
    """
    Downsample a 1D array by averaging over *factor* pixels.
    Crops right side if the shape is not a multiple of factor.

    Got this specific function from "Adam Ginsburgs python codes" on agpy
    myarr : numpy array

    factor : how much you want to rebin the array by
    """
    xs = myarr.shape[0]
    crarr = myarr[:xs-(xs % int(factor))]
    dsarr = np.mean(np.concatenate([[crarr[i::factor] for i in range(factor)]]), axis=0)

    return dsarr


# -- Load the COS data (G130M and G160M if available) in ASCII format:
G160M_filename = "/Users/efrazer/leadingarm/sightlines/CD14-A05/CD14-A05-G160M"

res_g160m = 19000.

wl_g160m, spec_g160m, err_g160m = np.loadtxt(G160M_filename, unpack=True)

wl_g160m_rb = downsample_1d(wl_g160m, 3)
spec_g160m_rb = downsample_1d(spec_g160m, 3)
err_g160m_rb = downsample_1d(err_g160m, 3)

dataset.add_data(wl_g160m_rb, spec_g160m_rb, 299792.458/res_g160m, err=err_g160m_rb, normalized=False)

G130M_filename = "/Users/efrazer/leadingarm/sightlines/CD14-A05/CD14-A05-G130M"

res_g130m = 16000.

wl_g130m, spec_g130m, err_g130m = np.loadtxt(G130M_filename, unpack=True)

wl_g130m_rb = downsample_1d(wl_g130m, 3)
spec_g130m_rb = downsample_1d(spec_g130m, 3)
err_g130m_rb = downsample_1d(err_g130m, 3)

dataset.add_data(wl_g130m_rb, spec_g130m_rb, 299792.458/res_g130m, err=err_g130m_rb, normalized=False)

# There is night only data for this sightline, so add this when fitting OI.
# G130M_N_filename = "/Users/efrazer/leadingarm/sightlines/CD14-A05/CD14-A05-G130M-N"
#
# wl_g130m_n, spec_g130m_n, err_g130m_n = np.loadtxt(G130M_N_filename, unpack=True)
#
# wl_g130m_rb_n = downsample_1d(wl_g130m_n, 3)
# spec_g130m_rb_n = downsample_1d(spec_g130m_n, 3)
# err_g130m_rb_n = downsample_1d(err_g130m_n, 3)
#
# dataset.add_data(wl_g130m_rb_n, spec_g130m_rb_n, 299792.458/res_g130m, err=err_g130m_rb_n, normalized=False)


# -- Change the width of velocity search region
dataset.velspan = 1000.0


# -- Add the ions we want to fit

# ION WAVELENGTH  F_VALUE
# C II    1334.5323   0.127800
# C IV    1548.2049   1.908E-01
# C IV    1550.7785   9.522E-02
# Si IV   1393.7550   5.280E-01
# Si IV   1402.7700   2.620E-01
# Si III  1206.5000   1.660E+00
# Si II   1260.4221   1.007E+00
# Si II   1193.2897   4.991E-01
# Si II   1190.4158   2.502E-01
# O I     1302

dataset.add_line("SiII_1260")
dataset.add_line("SiII_1193")
dataset.add_line("SiII_1190")
dataset.add_line("SiII_1526")
# dataset.add_line("SiIV_1393")
# dataset.add_line("SiIV_1402")
# dataset.add_line("CIV_1548")
# dataset.add_line("CIV_1550")
# dataset.add_line("OI_1302")


# NOTES ABOUT THE DETECTIONS:
# log N(C II) is an upper limit. Line is blended.
# log N(Si II) is an upper limit. Line is blended.
# log N(Si IV) is an upper limit. Line is blended.


# -- Add MW and initial single components for each ion:
#    add 1 to all the logN values for the MW 
#    b for the MW is twice the size of the b for the sightline
#    ordered by [ion, z, b, logN] then switches to fix z, b, or N during the fit

# SiII
dataset.add_component("SiII",  0., 15.0, 15.85, var_z=1, var_b=1, var_N=1)
dataset.add_component_velocity("SiII",  -70., 10., 13.05, var_z=1, var_b=1, var_N=1)
dataset.add_component_velocity("SiII",  50., 15., 14.05, var_z=1, var_b=1, var_N=1)
dataset.add_component_velocity("SiII",  120., 30.5, 13.85, var_z=1, var_b=1, var_N=1)
dataset.add_component_velocity("SiII",  200., 50.5, 13.65, var_z=1, var_b=1, var_N=1)


# SiIV
# dataset.add_component("SiIV",  0., 30.0, 13.63, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIV",  75, 30, 13.3, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIV",  170, 30, 13.3, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIV",  190, 30, 12.3, var_z=1, var_b=1, var_N=1)

# CIV
# dataset.add_component("CIV",   0., 42.0, 14.52, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CIV",   50, 15.5, 13.2, var_z=1, var_b=1, var_N=1)
# # dataset.add_component_velocity("CIV",   120, 15.5, 13.0, var_z=1, var_b=1, var_N=1)

# OI
# dataset.add_component("OI",  0., 30.0, 14.05, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("OI",  50., 15., 13.05, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("OI",  120., 47.5, 13.05, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("OI",  -50., 47.5, 13.05, var_z=1, var_b=1, var_N=1)

# -- Prepare the dataset: This will prompt the user for interactive
#    masking and normalization, as well as initiating the Parameters:

dataset.cheb_order = 1

dataset.prepare_dataset(norm=True, mask=True)


# -- Fit the dataset:
popt, chi2 = dataset.fit()

dataset.plot_fit(filename="CD14-A05-SiII.pdf")


# -- Save the dataset to file: taken from the dataset.name
dataset.save()
dataset.save_parameters("CD14-A05-SiII.fit")
dataset.save_cont_parameters_to_file("CD14-A05-SiII.cont")
dataset.save_fit_regions("CD14-A05-SiII.reg")


import numpy as np
import VoigtFit
import matplotlib
matplotlib.use("GTKAgg")


# -- Add the redshift of the cloud doing the absorption
#    Estimating 0 for everything.
z = 0.0

dataset = VoigtFit.DataSet(z)
dataset.set_name("RBS1897-NiII")
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
G160M_filename = "/Users/efrazer/leadingarm/sightlines/RBS1897/RBS1897-G160M"

res_g160m = 19000.

wl_g160m, spec_g160m, err_g160m = np.loadtxt(G160M_filename, unpack=True)

wl_g160m_rb = downsample_1d(wl_g160m, 3)
spec_g160m_rb = downsample_1d(spec_g160m, 3)
err_g160m_rb = downsample_1d(err_g160m, 3)

dataset.add_data(wl_g160m_rb, spec_g160m_rb, 299792.458/res_g160m, err=err_g160m_rb, normalized=False)

G130M_filename = "/Users/efrazer/leadingarm/sightlines/RBS1897/RBS1897-G130M"

res_g130m = 16000.

wl_g130m, spec_g130m, err_g130m = np.loadtxt(G130M_filename, unpack=True)

wl_g130m_rb = downsample_1d(wl_g130m, 3)
spec_g130m_rb = downsample_1d(spec_g130m, 3)
err_g130m_rb = downsample_1d(err_g130m, 3)

dataset.add_data(wl_g130m_rb, spec_g130m_rb, 299792.458/res_g130m, err=err_g130m_rb, normalized=False)


# -- Change the width of velocity search region
dataset.velspan = 1200.0


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

# dataset.add_line("SiII_1260")
# dataset.add_line("SiII_1193")
# dataset.add_line("SiII_1190")
# dataset.add_line("SiIII_1206")
# dataset.add_line("SiIV_1393")
# dataset.add_line("SiIV_1402")
# dataset.add_line("CII_1334")
# dataset.add_line("CIV_1548")
# dataset.add_line("CIV_1550")
dataset.add_line("NiII_1370")


# NOTES ABOUT THE DETECTIONS:
# log N(C II) is an upper limit. Line is blended.
# log N(C IV) is an upper limit. Line is blended.
# log N(Si IV) is an upper limit. Line is blended.


# -- Add MW and initial single components for each ion:
#    add 1 to all the logN values for the MW 
#    b for the MW is twice the size of the b for the sightline
#    ordered by [ion, z, b, logN] then switches to fix z, b, or N during the fit


# Ni II
dataset.add_component("NiII",  0., 10.0, 11.6, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("NiII",  90, 10.0, 10.6, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("NiII",  135, 30.0, 12.6, var_z=1, var_b=1, var_N=1)

# SiII
# dataset.add_component("SiII",  0., 40.0, 13.6, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiII",  90, 30.0, 12.6, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiII",  135, 30.0, 12.6, var_z=1, var_b=1, var_N=1)

# SiIII
# dataset.add_component("SiIII", 0., 40.0, 13.57, var_z=1, var_b=1, var_N=1)
# # dataset.add_component_velocity("SiIII", 60, 30.0, 12.57, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIII", 100, 30.0, 12.57, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIII", 135, 30.0, 12.57, var_z=1, var_b=1, var_N=1)
# # dataset.add_component_velocity("SiIII", 185, 30.0, 12.57, var_z=1, var_b=1, var_N=1)

# SiIV
# dataset.add_component("SiIV",  0., 100.0, 13.48, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIV",  135, 50.0, 12.48, var_z=1, var_b=1, var_N=1)

# CII
# dataset.add_component("CII",   0,  30.0, 14.7, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CII",   80, 30.0, 13.2, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CII",   135, 20.0, 13.2, var_z=1, var_b=1, var_N=1)

# CIV
# dataset.add_component("CIV",   0., 100.0, 14.2, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CIV",   135, 50.0, 13.2, var_z=1, var_b=1, var_N=1)


# -- Prepare the dataset: This will prompt the user for interactive
#    masking and normalization, as well as initiating the Parameters:

dataset.cheb_order = 1
dataset.norm_method = 'spline'
dataset.prepare_dataset(norm=True, mask=True)


# -- Fit the dataset:
popt, chi2 = dataset.fit()

# dataset.plot_fit(filename="RBS1897-NiII.pdf")


# -- Save the dataset to file: taken from the dataset.name
dataset.save()
dataset.save_parameters("RBS1897-NiII.fit")
dataset.save_cont_parameters_to_file("RBS1897-NiII.cont")
dataset.save_fit_regions("RBS1897-NiII.reg")


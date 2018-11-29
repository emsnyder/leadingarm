import numpy as np
import VoigtFit
import matplotlib
matplotlib.use("GTKAgg")


# -- Add the redshift of the cloud doing the absorption
#    Estimating 0 for everything.
z = 0.0

dataset = VoigtFit.DataSet(z)
dataset.set_name("PKS1136-13-XXX")
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
G130M_filename = "/Users/efrazer/leadingarm/sightlines/PKS1136-13/PKS1136-13-G130M"

res_g130m = 16000.

wl_g130m, spec_g130m, err_g130m = np.loadtxt(G130M_filename, unpack=True)

wl_g130m_rb = downsample_1d(wl_g130m, 3)
spec_g130m_rb = downsample_1d(spec_g130m, 3)
err_g130m_rb = downsample_1d(err_g130m, 3)

dataset.add_data(wl_g130m_rb, spec_g130m_rb, 299792.458/res_g130m, err=err_g130m_rb, normalized=False)


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

# dataset.add_line("SiII_1260")
# dataset.add_line("SiII_1193")
# dataset.add_line("SiII_1190")
# dataset.add_line("SiIII_1206")
# dataset.add_line("SiIV_1393")
# dataset.add_line("SiIV_1402")
# dataset.add_line("CII_1334")


# NOTES ABOUT THE DETECTIONS:
# log N(Si IV) is an upper limit. Line is blended.


# -- Add MW and initial single components for each ion:
#    add 1 to all the logN values for the MW 
#    b for the MW is twice the size of the b for the sightline
#    ordered by [ion, z, b, logN] then switches to fix z, b, or N during the fit

# SiII
# dataset.add_component("SiII",  0., 70.0, 13.57, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiII",  180, 35.0, 12.57, var_z=1, var_b=1, var_N=1)

# SiIII
# dataset.add_component("SiIII", 0., 70.0, 13.36, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIII", 180, 35.0, 12.36, var_z=1, var_b=1, var_N=1)

# SiIV
# dataset.add_component("SiIV",  0., 70.0, 13.77, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIV",  180, 35.0, 12.77, var_z=1, var_b=1, var_N=1)

# CII
# dataset.add_component("CII",   0,  70.0, 14.62, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CII",   180, 35.0, 13.62, var_z=1, var_b=1, var_N=1)

# CIV
# dataset.add_component("CIV",   0., 70.0, -998.0, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CIV",   180, 35.0, -999.0, var_z=1, var_b=1, var_N=1)


# -- Prepare the dataset: This will prompt the user for interactive
#    masking and normalization, as well as initiating the Parameters:

dataset.cheb_order = 1

dataset.prepare_dataset(norm=True, mask=True)


# -- Fit the dataset:
popt, chi2 = dataset.fit()

dataset.plot_fit(filename="PKS1136-13-XXX.pdf", max_rows=6)


# -- Save the dataset to file: taken from the dataset.name
dataset.save()
dataset.save_parameters("PKS1136-13-XXX.fit")
dataset.save_cont_parameters_to_file("PKS1136-13-XXX.cont")
dataset.save_fit_regions("PKS1136-13-XXX.reg")

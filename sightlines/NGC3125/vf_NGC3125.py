import numpy as np
import VoigtFit
import matplotlib
matplotlib.use("GTKAgg")


# -- Add the redshift of the cloud doing the absorption
#    Estimating 0 for everything.
z = 0.0

dataset = VoigtFit.DataSet(z)
dataset.set_name("NGC3125-SiIII")
dataset.verbose = True


# -- If log(NHI) is not known use:
logNHI = None


# -- Rebin the data set by 3 pixels

def downsample_1d(myarr,factor):
    """
    Downsample a 1D array by averaging over *factor* pixels.
    Crops right side if the shape is not a multiple of factor.

    Got this specific function from "Adam Ginsburgs python codes" on agpy
    myarr : numpy array

    factor : how much you want to rebin the array by
    """
    xs = myarr.shape[0]
    crarr = myarr[:xs-(xs % int(factor))]
    dsarr = np.mean( np.concatenate(
                     [[crarr[i::factor] for i in range(factor)] ]
                     ),axis=0)

    return dsarr


# -- Load the COS data (G130M and G160M if available) in ASCII format:
G130M_filename = "/Users/efrazer/science/cosdata/NGC3125-G130M"

res_g130m = 16000.

wl_g130m, spec_g130m, err_g130m = np.loadtxt(G130M_filename, unpack=True)

wl_g130m_rb = downsample_1d(wl_g130m, 3)
spec_g130m_rb = downsample_1d(spec_g130m, 3)
err_g130m_rb = downsample_1d(err_g130m, 3)

dataset.add_data(wl_g130m_rb, spec_g130m_rb, 299792.458/res_g130m, err=err_g130m_rb, normalized=False)


# -- Change the width of velocity search region
dataset.velspan = 800.0


# -- Add the ions we want to fit

# ION WAVELENGTH  F_VALUE
# C II    1334.5323   0.127800
# C IV    1548.2049   1.908E-01
# C IV    1550.7785   9.522E-02
# SiIV    1393.7550   5.280E-01
# SiIV    1402.7700   2.620E-01
# SiIII   1206.5000   1.660E+00
# SiII    1260.4221   1.007E+00
# SiII    1193.2897   4.991E-01
# SiII    1190.4158   2.502E-01

# dataset.add_line("CII_1334")
#dataset.add_line("SiII_1260")
# dataset.add_line("SiII_1193")  # blended
# dataset.add_line("SiII_1190")  # blended
dataset.add_line("SiIII_1206")
# dataset.add_line("SiIV_1393")
# dataset.add_line("SiIV_1402")


# NOTES ABOUT THE DETECTIONS:
# log N(C II) is an upper limit. Line is blended.
# log N(Si IV) is an upper limit. Line is blended.


# -- Add MW components for each ion:

# SiII
#                      ion     z   b   logN
# dataset.add_component("SiII",  0., 60.0, 13.8, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiII",  120, 20.0, 13.1, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiII",  190, 30.0, 13.1, var_z=1, var_b=1, var_N=1)

# SiIII
dataset.add_component("SiIII",  0., 60.0, 13.8, var_z=1, var_b=1, var_N=1)
dataset.add_component_velocity("SiIII",  120, 20.0, 13.1, var_z=1, var_b=1, var_N=1)
dataset.add_component_velocity("SiIII",  190, 30.0, 13.1, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIII",  210, 30.0, 13.1, var_z=1, var_b=1, var_N=1)


# -- Prepare the dataset: This will prompt the user for interactive
#    masking and normalization, as well as initiating the Parameters:

# dataset.cheb_order = 1
dataset.cheb_order = -1
dataset.norm_method = 'spline'
dataset.prepare_dataset(norm=True, mask=True)


# -- Fit the dataset:
popt, chi2 = dataset.fit()

dataset.plot_fit(filename="NGC3125-SiIII.pdf", max_rows=6)


# -- Save the dataset to file: taken from the dataset.name
dataset.save()
dataset.save_parameters("NGC3125-SiIII.fit")
dataset.save_cont_parameters_to_file("NGC3125-SiIII.cont")
dataset.save_fit_regions("NGC3125-SiIII.reg")


import numpy as np
import VoigtFit
import matplotlib
matplotlib.use("GTKAgg")


# -- Add the redshift of the cloud doing the absorption
#    Estimating 0 for everything.
z = 0.0

dataset = VoigtFit.DataSet(z)
dataset.set_name("PHL1811-SiIV")
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
# G160M_filename = "/Users/efrazer/science/cosdata/PHL1811-G160M"
#
# res_g160m = 19000.
#
# wl_g160m, spec_g160m, err_g160m = np.loadtxt(G160M_filename, unpack=True)
#
# wl_g160m_rb = downsample_1d(wl_g160m, 3)
# spec_g160m_rb = downsample_1d(spec_g160m, 3)
# err_g160m_rb = downsample_1d(err_g160m, 3)
# 
# dataset.add_data(wl_g160m_rb, spec_g160m_rb, 299792.458/res_g160m, err=err_g160m_rb, normalized=False)

G130M_filename = "/Users/efrazer/science/cosdata/PHL1811-G130M"

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
# SiIV    1393.7550   5.280E-01
# SiIV    1402.7700   2.620E-01
# SiIII   1206.5000   1.660E+00
# SiII    1260.4221   1.007E+00
# SiII    1193.2897   4.991E-01
# SiII    1190.4158   2.502E-01

# # dataset.add_line("CII_1334")
# dataset.add_line("CIV_1548")
# dataset.add_line("CIV_1550")
# dataset.add_line("SiII_1260") # will be blended with 1259 Sulfur line
# dataset.add_line("SiII_1193")
# dataset.add_line("SiII_1190")
# dataset.add_line("SiIII_1206")
dataset.add_line("SiIV_1393")
dataset.add_line("SiIV_1402")


# NOTES ABOUT THE DETECTIONS:
# All detections are OK.


# -- Add MW components for each ion:
#                      ion     z   b   logN
# dataset.add_component("CII",   0,  120., 14.5, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiIII", 0., 260.0, 14.6, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiIV",  0., 260.0, 14.46, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CIV",   0., 260.0, 15.3, var_z=1, var_b=1, var_N=1)
# # add 1 to all the logN values


# -- Add the MS components
#    The z is now an offset in velocity
# dataset.add_component_velocity("CII",   -260, 40.0, 13.5, var_z=0, var_b=1, var_N=1)
# dataset.add_component_velocity("CII",   -205, 70.0, 13.7, var_z=0, var_b=1, var_N=1)
# dataset.add_component_velocity("CII",   -165, 50, 13.4, var_z=0, var_b=1, var_N=1)

# dataset.add_component_velocity("SiII",  -200, 130.0, 13.37, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIII", -200, 130.0, 13.6, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiIV",  -200, 130.0, 13.46, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CIV",   -200, 130.0, 14.3, var_z=1, var_b=1, var_N=1)

# C II
# dataset.add_component("CII",  -0.000862,  17.35, 13.389, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CII",  -0.000690,  18.29, 14.088, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CII",  -0.000565,   9.78, 13.541, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CII",  -0.000054,  31.20, 14.559, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CII",   0.000108,  35.00, 14.612, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("CII", 275, 50, 13.4, var_z=1, var_b=1, var_N=1)

# Si II
# dataset.add_component("SiII",  0.,         30.0, 14.37, var_z=1, var_b=1, var_N=1)
# dataset.add_component_velocity("SiII",  -50,    18.0, 14.37, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiII",  -0.000690,  18.29, 13.6, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiII",  -0.000565,   9.78, 13.5, var_z=1, var_b=1, var_N=1)

# SiIII
# dataset.add_component_velocity("SiIII",  -350,  17.35, 13.389, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiIII",  -0.000862,  17.35, 13.389, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiIII",  -0.000690,  18.29, 14.088, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiIII",  -0.000565,   9.78, 13.541, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiIII",  -0.000054,  31.20, 14.559, var_z=1, var_b=1, var_N=1)
# dataset.add_component("SiIII",   0.000108,  35.00, 14.612, var_z=1, var_b=1, var_N=1)

# SiIV

dataset.add_component_velocity("SiIV",  -350,  17., 13.0, var_z=1, var_b=1, var_N=1)
dataset.add_component("SiIV",  -0.000862,  17.35, 13.389, var_z=1, var_b=1, var_N=1)
dataset.add_component("SiIV",  -0.000690,  18.29, 14.088, var_z=1, var_b=1, var_N=1)
dataset.add_component("SiIV",  -0.000565,   9.78, 13.541, var_z=1, var_b=1, var_N=1)
dataset.add_component("SiIV",  -0.000054,  31.20, 14.559, var_z=1, var_b=1, var_N=1)
dataset.add_component("SiIV",   0.00018,  35.00, 14.612, var_z=1, var_b=1, var_N=1)

# C IV
# dataset.add_component_velocity("CIV",  -350,  17.35, 13.389, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CIV",  -0.000862,  17.35, 13.389, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CIV",  -0.000690,  18.29, 14.088, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CIV",  -0.000565,   9.78, 13.541, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CIV",  -0.000054,  31.20, 14.559, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CIV",   0.000108,  35.00, 14.612, var_z=1, var_b=1, var_N=1)
# dataset.add_component("CIV",   0.000108,  35.00, 14.612, var_z=1, var_b=1, var_N=1)



# -- Prepare the dataset: This will prompt the user for interactive
#    masking and normalization, as well as initiating the Parameters:

dataset.cheb_order = 1
# dataset.norm_method = 'spline'
dataset.prepare_dataset(norm=True, mask=True)


# -- Fit the dataset:
popt, chi2 = dataset.fit()

dataset.plot_fit(filename="PHL1811-SiIV.pdf", max_rows=6)


# -- Save the dataset to file: taken from the dataset.name
dataset.save()
dataset.save_parameters("PHL1811-SiIV.fit")
dataset.save_cont_parameters_to_file("PHL1811-SiIV.cont")
dataset.save_fit_regions("PHL1811-SiIV.reg")

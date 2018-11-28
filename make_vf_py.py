import numpy as np
from astropy.io import fits
import os

rootdir = '/Users/efrazer/leadingarm/'

datatable = os.path.join(rootdir, 'datafile1418.fits')

data = fits.getdata(datatable)


def checklimits(ionflag, ionname):

    if ionflag == -1:
        flag = '# {} is a lower limit. Line is saturated.\n'.format(ionname)
    elif ionflag == 1:
        flag = '# {} is an upper limit. Line is blended.\n'.format(ionname)
    elif ionflag == 0:
        flag = None
    else:
        raise ValueError

    return flag


for row in data:

    # if os.path.isfile('/Users/efrazer/science/scripts_new/vf_{}.py'.format(row['target'])):
    #     continue

    filepath = os.path.join(rootdir, 'sightlines', row['target'])

    with open(os.path.join(filepath, 'vf_{}.py'.format(row['target'])), 'w') as f:

        f.write('import numpy as np\n')
        f.write('import VoigtFit\n')
        f.write('import matplotlib\n')
        f.write('matplotlib.use("GTKAgg")\n')
        f.write('\n')
        f.write('\n')
        f.write('# -- Add the redshift of the cloud doing the absorption\n')
        f.write('#    Estimating 0 for everything.\n')
        f.write('z = 0.0\n')
        f.write('\n')
        f.write('dataset = VoigtFit.DataSet(z)\n')
        f.write('dataset.set_name("{}-XXX")\n'.format(row['target']))
        f.write('dataset.verbose = True\n')
        f.write('\n')
        f.write('\n')
        f.write('# -- If log(NHI) is not known use:\n')
        f.write('logNHI = None\n')
        f.write('\n')
        f.write('\n')
        f.write('# -- Rebin the data set by 3 pixels\n')
        f.write('\n')
        f.write('def downsample_1d(myarr, factor):\n')
        f.write('    """\n')
        f.write('    Downsample a 1D array by averaging over *factor* pixels.\n')
        f.write('    Crops right side if the shape is not a multiple of factor.\n')
        f.write('\n')
        f.write('    Got this specific function from "Adam Ginsburgs python codes" on agpy')
        f.write('\n')
        f.write('    myarr : numpy array\n')
        f.write('\n')
        f.write('    factor : how much you want to rebin the array by\n')
        f.write('    """\n')
        f.write('    xs = myarr.shape[0]\n')
        f.write('    crarr = myarr[:xs-(xs % int(factor))]\n')
        f.write('    dsarr = np.mean(np.concatenate([[crarr[i::factor] for i in range(factor)]]), axis=0)\n')
        f.write('\n')
        f.write('    return dsarr\n')
        f.write('\n')
        f.write('\n')
        
        f.write('# -- Load the COS data (G130M and G160M if available) in ASCII format:\n')
        
        if os.path.isfile(os.path.join(filepath, "{}-G160M".format(row['target']))):
            G160M_path = os.path.join(filepath, "{}-G160M".format(row['target']))
            f.write('G160M_filename = "{}"\n'.format(G160M_path))
            f.write('\n')
            f.write('res_g160m = 19000.\n')
            f.write('\n')
            f.write('wl_g160m, spec_g160m, err_g160m = np.loadtxt(G160M_filename, unpack=True)\n')
            f.write('\n')
            f.write('wl_g160m_rb = downsample_1d(wl_g160m, 3)\n')
            f.write('spec_g160m_rb = downsample_1d(spec_g160m, 3)\n')
            f.write('err_g160m_rb = downsample_1d(err_g160m, 3)\n')
            f.write('\n')
            f.write('dataset.add_data(wl_g160m_rb, spec_g160m_rb, '
                    '299792.458/res_g160m, err=err_g160m_rb, normalized=False)\n')
            f.write('\n')
        elif os.path.isfile(os.path.join(filepath, "{}_spec-G160M".format(row['target']))):
            G160M_path = os.path.join(filepath, "{}_spec-G160M".format(row['target']))
            f.write('G160M_filename = "{}"\n'.format(G160M_path))
            f.write('\n')
            f.write('res_g160m = 19000.\n')
            f.write('\n')
            f.write('wl_g160m, spec_g160m, err_g160m = np.loadtxt(G160M_filename, unpack=True)\n')
            f.write('\n')
            f.write('wl_g160m_rb = downsample_1d(wl_g160m, 3)\n')
            f.write('spec_g160m_rb = downsample_1d(spec_g160m, 3)\n')
            f.write('err_g160m_rb = downsample_1d(err_g160m, 3)\n')
            f.write('\n')
            f.write('dataset.add_data(wl_g160m_rb, spec_g160m_rb, '
                    '299792.458/res_g160m, err=err_g160m_rb, normalized=False)\n')
            f.write('\n')
        else:
            pass
            
        if os.path.isfile(os.path.join(filepath, "{}-G130M".format(row['target']))):
            G130M_path = os.path.join(filepath, "{}-G130M".format(row['target']))
            f.write('G130M_filename = "{}"\n'.format(G130M_path))
            f.write('\n')
            f.write('res_g130m = 16000.\n')
            f.write('\n')
            f.write('wl_g130m, spec_g130m, err_g130m = np.loadtxt(G130M_filename, unpack=True)\n')
            f.write('\n')
            f.write('wl_g130m_rb = downsample_1d(wl_g130m, 3)\n')
            f.write('spec_g130m_rb = downsample_1d(spec_g130m, 3)\n')
            f.write('err_g130m_rb = downsample_1d(err_g130m, 3)\n')
            f.write('\n')
            f.write('dataset.add_data(wl_g130m_rb, spec_g130m_rb, '
                    '299792.458/res_g130m, err=err_g130m_rb, normalized=False)\n')
            f.write('\n')
        elif os.path.isfile(os.path.join(filepath, "{}_spec-G130M".format(row['target']))):
            G130M_path = os.path.join(filepath, "{}_spec-G130M".format(row['target']))
            f.write('G130M_filename = "{}"\n'.format(G130M_path))
            f.write('\n')
            f.write('res_g130m = 16000.\n')
            f.write('\n')
            f.write('wl_g130m, spec_g130m, err_g130m = np.loadtxt(G130M_filename, unpack=True)\n')
            f.write('\n')
            f.write('wl_g130m_rb = downsample_1d(wl_g130m, 3)\n')
            f.write('spec_g130m_rb = downsample_1d(spec_g130m, 3)\n')
            f.write('err_g130m_rb = downsample_1d(err_g130m, 3)\n')
            f.write('\n')
            f.write('dataset.add_data(wl_g130m_rb, spec_g130m_rb, '
                    '299792.458/res_g130m, err=err_g130m_rb, normalized=False)\n')
            f.write('\n')
        else:
            pass

        if os.path.isfile(os.path.join(filepath, "{}-G130M-N".format(row['target']))):
            G130M_path = os.path.join(filepath, "{}-G130M-N".format(row['target']))
            f.write('# There is night only data for this sightline, so add this when fitting OI.\n')
            f.write('# G130M_N_filename = "{}"\n'.format(G130M_path))
            f.write('\n')
            f.write('# wl_g130m_n, spec_g130m_n, err_g130m_n = np.loadtxt(G130M_N_filename, unpack=True)\n')
            f.write('\n')
            f.write('# wl_g130m_rb_n = downsample_1d(wl_g130m_n, 3)\n')
            f.write('# spec_g130m_rb_n = downsample_1d(spec_g130m_n, 3)\n')
            f.write('# err_g130m_rb_n = downsample_1d(err_g130m_n, 3)\n')
            f.write('\n')
            f.write('# dataset.add_data(wl_g130m_rb_n, spec_g130m_rb_n, '
                    '299792.458/res_g130m, err=err_g130m_rb_n, normalized=False)\n')
            f.write('\n')
        elif os.path.isfile(os.path.join(filepath, "{}_spec-G130M-N".format(row['target']))):
            G130M_path = os.path.join(filepath, "{}_spec-G130M-N".format(row['target']))
            f.write('# There is night only data for this sightline, so add this when fitting OI.\n')
            f.write('# G130M_N_filename = "{}"\n'.format(G130M_path))
            f.write('\n')
            f.write('# wl_g130m_n, spec_g130m_n, err_g130m_n = np.loadtxt(G130M_N_filename, unpack=True)\n')
            f.write('\n')
            f.write('# wl_g130m_rb_n = downsample_1d(wl_g130m_n, 3)\n')
            f.write('# spec_g130m_rb_n = downsample_1d(spec_g130m_n, 3)\n')
            f.write('# err_g130m_rb_n = downsample_1d(err_g130m_n, 3)\n')
            f.write('\n')
            f.write('# dataset.add_data(wl_g130m_rb_n, spec_g130m_rb_n, '
                    '299792.458/res_g130m, err=err_g130m_rb_n, normalized=False)\n')
            f.write('\n')
        else:
            pass

        f.write('\n')
        f.write('# -- Change the width of velocity search region\n')
        f.write('dataset.velspan = 1000.0\n')
        f.write('\n')
        f.write('\n')
        f.write('# -- Add the ions we want to fit\n')
        f.write('\n')
        f.write('# ION WAVELENGTH  F_VALUE\n')
        f.write('# C II    1334.5323   0.127800\n')
        f.write('# C IV    1548.2049   1.908E-01\n')
        f.write('# C IV    1550.7785   9.522E-02\n')
        f.write('# Si IV   1393.7550   5.280E-01\n')
        f.write('# Si IV   1402.7700   2.620E-01\n')
        f.write('# Si III  1206.5000   1.660E+00\n')
        f.write('# Si II   1260.4221   1.007E+00\n')
        f.write('# Si II   1193.2897   4.991E-01\n')
        f.write('# Si II   1190.4158   2.502E-01\n')
        f.write('# O I     1302\n')
        f.write('\n')

        # don't add the lines at all if there's no detection of the ion
        if row['logN(SiII)'] != -999:
            f.write('# dataset.add_line("SiII_1260")\n')
            f.write('# dataset.add_line("SiII_1193")\n')
            f.write('# dataset.add_line("SiII_1190")\n')

        if row['logN(SiIII)'] != -999:
            f.write('# dataset.add_line("SiIII_1206")\n')

        if row['logN(SiIV)'] != -999:
            f.write('# dataset.add_line("SiIV_1393")\n')
            f.write('# dataset.add_line("SiIV_1402")\n')

        if row['logN(CII)'] != -999:
            f.write('# dataset.add_line("CII_1334")\n')

        if row['logN(CIV)'] != -999:
            f.write('# dataset.add_line("CIV_1548")\n')
            f.write('# dataset.add_line("CIV_1550")\n')

        if os.path.isfile(os.path.join(filepath, "{}_spec-G130M-N".format(row['target']))) or\
                os.path.isfile(os.path.join(filepath, "{}-G130M-N".format(row['target']))):
            f.write('# dataset.add_line("OI_1302")\n')

        f.write('\n')
        f.write('\n')

        # add warning to check for upper limits (blended lines) or lower limits (saturated lines)
        f.write('# NOTES ABOUT THE DETECTIONS:\n')
        flaglist = [checklimits(row['logN(CII)_lim'], 'log N(C II)'),
                    checklimits(row['logN(CIV)_lim'], 'log N(C IV)'),
                    checklimits(row['logN(SiII)_lim'], 'log N(Si II)'),
                    checklimits(row['logN(SiIII)_lim'], 'log N(Si III)'),
                    checklimits(row['logN(SiIV)_lim'], 'log N(Si IV)')]
        for flag in flaglist:
            if flag is not None:
                f.write(flag)
        if all(v is None for v in flaglist):
            f.write('# All detections are OK.\n')

        f.write('\n')
        f.write('\n')

        f.write('# -- Add MW and initial single components for each ion:\n')
        f.write('#    add 1 to all the logN values for the MW \n')
        f.write('#    b for the MW is twice the size of the b for the sightline\n')
        f.write('#    ordered by [ion, z, b, logN] then switches to fix z, b, or N during the fit\n')
        f.write('\n')

        if row['vms'] == -999:
            vcen = (row['vmin'] + row['vmax'])/2.
        else:
            vcen = row['vms']
            
        b_start = np.abs(row['vmax'] - row['vmin'])/2.

        f.write('# SiII\n')
        f.write('# dataset.add_component("SiII",  0., {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(b_start*2., row['logN(SiII)']+1.))
        f.write('# dataset.add_component_velocity("SiII",  {}, {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(vcen, b_start, row['logN(SiII)']))
        f.write('\n')
        f.write('# SiIII\n')
        f.write('# dataset.add_component("SiIII", 0., {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(b_start*2., row['logN(SiIII)']+1.))
        f.write('# dataset.add_component_velocity("SiIII", {}, {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(vcen, b_start, row['logN(SiIII)']))
        f.write('\n')
        f.write('# SiIV\n')
        f.write('# dataset.add_component("SiIV",  0., {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(b_start*2., row['logN(SiIV)']+1.))
        f.write('# dataset.add_component_velocity("SiIV",  {}, {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(vcen, b_start, row['logN(SiIV)']))
        f.write('\n')
        f.write('# CII\n')
        f.write('# dataset.add_component("CII",   0,  {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(b_start * 2., row['logN(CII)'] + 1.))
        f.write('# dataset.add_component_velocity("CII",   {}, {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(vcen, b_start, row['logN(CII)']))
        f.write('\n')
        f.write('# CIV\n')
        f.write('# dataset.add_component("CIV",   0., {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(b_start*2., row['logN(CIV)']+1.))
        f.write('# dataset.add_component_velocity("CIV",   {}, {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(vcen, b_start, row['logN(CIV)']))
        f.write('\n')
        if os.path.isfile(os.path.join(filepath, "{}_spec-G130M-N".format(row['target']))):
            f.write('# OI\n')
            f.write('# dataset.add_component("OI",   0., {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(b_start * 2., row['logN(OI)'] + 1.))
            f.write('# dataset.add_component_velocity("CIV",   {}, {}, {}, var_z=1, var_b=1, var_N=1)\n'.format(vcen, b_start, row['logN(OI)']))

        f.write('\n')
        f.write('# -- Prepare the dataset: This will prompt the user for interactive\n')
        f.write('#    masking and normalization, as well as initiating the Parameters:\n')
        f.write('\n')
        f.write('dataset.cheb_order = 1\n')
        f.write('\n')
        f.write('dataset.prepare_dataset(norm=True, mask=True)\n')
        f.write('\n')
        f.write('\n')
        f.write('# -- Fit the dataset:\n')
        f.write('popt, chi2 = dataset.fit()\n')
        f.write('\n')
        f.write('dataset.plot_fit(filename="{}-XXX.pdf", max_rows=6)\n'.format(row['target']))
        f.write('\n')
        f.write('\n')
        f.write('# -- Save the dataset to file: taken from the dataset.name\n')
        f.write('dataset.save()\n')
        f.write('dataset.save_parameters("{}-XXX.fit")\n'.format(row['target']))
        f.write('dataset.save_cont_parameters_to_file("{}-XXX.cont")\n'.format(row['target']))
        f.write('dataset.save_fit_regions("{}-XXX.reg")\n'.format(row['target']))
        f.write('\n')

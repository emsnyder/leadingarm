import glob
import os
import numpy as np
import pickle
from astropy.io import fits

CVAL = 299792.0  # km/s

FITDIR = '/Users/efrazer/leadingarm/sightlines/'
DATAFILE = '/Users/efrazer/leadingarm/datafile1418.fits'


# -----------------------------------------------
def set_up_dict(fit_list):

    fitdict = {}

    sightlines = []

    for myfile in fit_list:
        name = myfile.split('/')[-2]
        if name in sightlines:
            continue
        else:
            sightlines.append(name)

    for sl in sightlines:
        fitdict[sl] = {}

    return fitdict


# -----------------------------------------------
def measure_sn(name, ion, flux):

    # for certain sightlines use custom arrays
    if (name == 'SDSSJ234500.43-005936.0') and (ion == 'CII'):
        bounds = [30, 60, len(flux)-50, len(flux)]
    elif (name == 'ESO267-G13') and (ion == 'SiII'):
        bounds = [0, 20, len(flux)-50, len(flux)]
    elif (name == 'IRAS_F09539-0439') and (ion == 'SiII'):
        bounds = [0, 20, 0, 20]
    elif (name == 'IRAS_F09539-0439') and (ion == 'OI'):
        bounds = [0, 50, 0, 50]
    elif (name == 'LBQS0107-0233') and (ion == 'SiIII'):
        bounds = [25, 75, len(flux)-100, len(flux)-50]
    elif (name == 'HE1159-1338') and (ion == 'SiII'):
        bounds = [len(flux)-50, len(flux), len(flux)-50, len(flux)]
    elif (name == 'LBQS0107-0235') and (ion == 'CII'):
        bounds = [len(flux) - 30, len(flux), len(flux) - 30, len(flux)]
    elif (name == 'LBQS0107-0235') and (ion == 'SiIII'):
        bounds = [0, 25, 0, 25]
    elif (name == 'UGC12163') and (ion == 'CII'):
        bounds = [len(flux) - 30, len(flux), len(flux) - 30, len(flux)]
    elif (name == 'UGC12163') and (ion == 'SiIII'):
        bounds = [len(flux) - 50, len(flux), len(flux) - 50, len(flux)]
    elif (name == 'UGC12163') and (ion == 'CIV'):
        bounds = [0, 20, 0, 20]
    elif (name == 'CD14-A05') and (ion == 'OI'):
        bounds = [15, 30, len(flux) - 40, len(flux)]
    elif (name == 'MRK1044') and (ion == 'CII'):
        bounds = [0, 40, len(flux) - 25, len(flux)]
    elif (name == 'NGC7714') and (ion == 'CIV'):
        bounds = [0, 15, len(flux) - 25, len(flux)]
    elif (name == 'PG0044+030') and (ion == 'SiIII'):
        bounds = [0, 30, len(flux) - 15, len(flux)]
    elif (name == 'RX_J0209.5-0438') and (ion == 'CII'):
        bounds = [40, 70, len(flux) - 15, len(flux)]
    elif (name == 'RX_J0209.5-0438') and (ion == 'CIV'):
        bounds = [40, 70, len(flux) - 40, len(flux)]
    elif (name == 'PG0003+158') and (ion == 'SiII'):
        bounds = [0, 25, len(flux)-70, len(flux)-40]
    elif (name == 'PG0003+158') and (ion == 'SiIII'):
        bounds = [0, 25, len(flux)-30, len(flux)]
    elif (name == 'NGC3125') and (ion == 'OI'):
        bounds = [0, 30, 0, 30]
    elif (name == 'PKS1101-325') and (ion == 'SII'):
        bounds = [25, 50, len(flux)-30, len(flux)]
    elif (name == 'PKS1101-325') and (ion == 'OI'):
        bounds = [0, 50, len(flux)-25, len(flux)]
    elif (name == 'PKS1101-325') and (ion == 'SiII'):
        bounds = [0, 50, 0, 50]
    elif (name == 'LBQS0107-0233') and (ion == 'SiIII'):
        bounds = [25, 50, len(flux)-30, len(flux)]
    elif (name == 'HE0153-4520') and (ion == 'CII'):
        bounds = [0, 50, len(flux)-70, len(flux)-40]
    elif (name == 'HE0153-4520') and (ion == 'SiII'):
        bounds = [0, 25, len(flux)-50, len(flux)]
    elif (name == 'PG0026+129') and (ion == 'SiIV'):
        bounds = [len(flux) - 30, len(flux), len(flux) - 30, len(flux)]
    elif (name == 'MRC2251-178') and (ion == 'CII'):
        bounds = [0, 30, len(flux)-25, len(flux)]
    elif (name == 'IO-AND') and (ion == 'SiIII'):
        bounds = [0, 25, len(flux)-50, len(flux)]
    elif (name == 'IO-AND') and (ion == 'SiIV'):
        bounds = [0, 25, len(flux)-50, len(flux)]
    elif (name == 'SDSSJ015530.02-085704.0') and (ion == 'SiIII'):
        bounds = [20, 40, len(flux)-30, len(flux)]
    else:
        bounds = [0, 50, len(flux)-50, len(flux)]

    startsn = np.mean(flux[bounds[0]: bounds[1]]) / np.std(flux[bounds[0]: bounds[1]])
    endsn = np.mean(flux[bounds[2]: bounds[3]]) / np.nanstd(flux[bounds[2]: bounds[3]])

    meansn = np.mean([startsn, endsn])

    nonnanmean = np.nan_to_num(meansn)

    return nonnanmean * 1.8   # this is for binning the data by 3 pix


# -----------------------------------------------
def get_dir(name):

    bigtable = fits.getdata(DATAFILE)

    sel = np.where(bigtable['target'] == name)

    direc = bigtable['region'][sel]

    if 'LA' in direc[0]:
        dirnew = 'LA'
    elif 'MS' in direc[0]:
        dirnew = 'MS'
    else:
        print(direc)
        dirnew = direc

    return dirnew


# -----------------------------------------------
def extract_fits(input_path, fitdict):

    # pull out the name of the sightline
    name = input_path.split('/')[-2]

    compnum = []
    ion = []
    z = []
    z_err = []
    b = []
    b_err = []
    n = []
    n_err = []
    fitfile = open(input_path, 'r')
    for line in fitfile:
        line = line.strip()
        if ('#' not in line) and (line != ''):
            # don't save the 0 comp -- always the MW
            if line.split()[0] == '0':
                continue
            # don't save the component if b_err > 1.5*b
            if float(line.split()[5]) > 1.5*float(line.split()[4]):
                ion.append(line.split()[1])
                continue
            # don't save the component if b < 5 km/s
            if float(line.split()[4]) < 5:
                ion.append(line.split()[1])
                continue
            compnum.append(int(line.split()[0]))
            ion.append(line.split()[1])
            z.append(float(line.split()[2]))
            z_err.append(float(line.split()[3]))
            b.append(float(line.split()[4]))
            b_err.append(float(line.split()[5]))
            n.append(float(line.split()[6]))
            n_err.append(float(line.split()[7]))

    # if compnum == []:
    #
    #     return
    #
    # else:

    wave = []
    flux = []
    flux_err = []
    bestfit = []
    masked = []
    regfile = open(input_path.strip('.fit') + '.reg', 'r')
    for line in regfile:
        line = line.strip()
        if ('#' not in line) and (line != ''):
            wave.append(float(line.split()[0]))
            flux.append(float(line.split()[1]))
            flux_err.append(float(line.split()[2]))
            bestfit.append(float(line.split()[3]))
            masked.append(int(line.split()[4]))

    # compute S/N
    sn = measure_sn(name, ion[0], flux)

    # match name in datafile to get direction
    direc = get_dir(name)
    print(direc)

    compdict = {'component number': compnum,
                'redshift': z,
                'redshift error': z_err,
                'b value': b,
                'b value error': b_err,
                'column density': n,
                'column density error': n_err
                }

    iondict = {ion[0]: {'S/N': sn,
                        'direction': direc,
                        'wavelength': wave,
                        'flux': flux,
                        'flux error': flux_err,
                        'best fit line': bestfit,
                        'masked regions': masked,
                        'components': compdict
                        }
               }

    fitdict[name].update(iondict)
    fitdict[name].update({'direction': direc})

    # import pdb
    # pdb.set_trace()
    #
    # return fitdict


# -----------------------------------------------
def main():

    fitlist1 = glob.glob(os.path.join(FITDIR, '*', '*I.fit'))
    fitlist2 = glob.glob(os.path.join(FITDIR, '*', '*V.fit'))

    fitlist = fitlist1 + fitlist2

    fitdict = set_up_dict(fitlist)

    for myfile in fitlist:
        print(myfile)
        extract_fits(myfile, fitdict)

    with open('fitdict_test.pickle', 'wb') as handle:
        pickle.dump(fitdict, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # df = pd.DataFrame(popdict)
    # df.to_latex('fitdict.tex', na_rep='--')


# -----------------------------------------------
if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# import glob
import os
import numpy as np

'''
Stream
------
FAIRALL9 - Si II, III, and IV
NGC7714
PHL2525
RBS144 - Si II, III
SDSSJ001224.01-102226.5 - C II and IV
SDSSJ234500.43-005936.0 - Si II, III and IV (some large errors

Leading Arm
-----------
IRASF09539-0439 - Si II and Si IV
NGC3125 - Si II, III, IV (wonky)
PKS1101-325 - Si II and Si IV
SDSSJ095915.60+050355.0 - Si III, C IV
CD14-A05 - Si II and Si IV
UVQSJ1016-3150 - Si II and Si III
'''

c = 299792.0  # km/s

rootdir = '/Users/efrazer/leadingarm/sightlines/'

sldict = {'UVQSJ101629.20-315023.6':
              {'ion_label': ['Si II 1193', 'Si III 1206'],
               'ions': ['SiII', 'SiIII'],
               'dir': 'LA'},
          'CD14-A05':
              {'ion_label': ['Si II 1193', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'SDSSJ095915.60+050355.0':
              {'ion_label': ['Si III 1206', 'C IV 1548'],
               'ions': ['SiIII', 'CIV'],
               'dir': 'LA'},
          'PKS1101-325':
              {'ion_label': ['Si II 1190', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'NGC3125':
              {'ion_label': ['Si II 1190', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'IRAS_F09539-0439':
              {'ion_label': ['Si II 1190', 'Si IV 1393'],
               'ions': ['SiII', 'SiIV'],
               'dir': 'LA'},
          'SDSSJ234500.43-005936.0':
              {'ion_label': ['Si II 1260', 'Si III 1206', 'Si IV 1393'],
               'ions': ['SiII', 'SiIII', 'SiIV'],
               'dir': 'MS'},
          'SDSSJ001224.01-102226.5':
              {'ion_label': ['C II 1334', 'C IV 1548'],
               'ions': ['CII', 'CIV'],
               'dir': 'MS'},
          'RBS144':
              {'ion_label': ['Si II 1193', 'Si III 1206'],
               'ions': ['SiII', 'SiIII'],
               'dir': 'MS'},
          'PHL2525':
              {'ion_label': ['C II 1334', 'C IV 1548'],
               'ions': ['CII', 'CIV'],
               'dir': 'MS'},
          'NGC7714':
              {'ion_label': ['C II 1334', 'C IV 1548'],
               'ions': ['CII', 'CIV'],
               'dir': 'MS'},
          'FAIRALL9':
              {'ion_label': ['Si II 1193', 'Si III 1206', 'Si IV 1402'],
               'ions': ['SiII', 'SiIII', 'SiIV'],
               'dir': 'MS'}
          }


def extract_fits(input_path):
    compnum = []
    ion = []
    z = []
    z_err = []
    b = []
    b_err = []
    n = []
    n_err = []
    fitfile = open(input_path+'.fit', 'r')
    for line in fitfile:
        line = line.strip()
        if ('#' not in line) and (line != ''):
            compnum.append(int(line.split()[0]))
            ion.append(line.split()[1])
            z.append(float(line.split()[2]))
            z_err.append(float(line.split()[3]))
            b.append(float(line.split()[4]))
            b_err.append(float(line.split()[5]))
            n.append(float(line.split()[6]))
            n_err.append(float(line.split()[7]))

    wave = []
    flux = []
    flux_err = []
    bestfit = []
    masked = []
    regfile = open(input_path+'.reg', 'r')
    for line in regfile:
        line = line.strip()
        if ('#' not in line) and (line != ''):
            wave.append(float(line.split()[0]))
            flux.append(float(line.split()[1]))
            flux_err.append(float(line.split()[2]))
            bestfit.append(float(line.split()[3]))
            masked.append(int(line.split()[4]))

    return compnum, z, z_err, b, b_err, n, n_err, np.array(wave), \
           np.array(flux_err), np.array(flux), np.array(bestfit), np.array(masked)


def wl_to_v(input_arr, ion):
    if '1190' in ion:
        restwl = 1190.4158
    elif '1193' in ion:
        restwl = 1193.2897
    elif '1260' in ion:
        restwl = 1260.4221
    elif '1253' in ion:
        restwl = 1253.8110
    elif '1206' in ion:
        restwl = 1206.5000
    elif '1393' in ion:
        restwl = 1393.7550
    elif '1402' in ion:
        restwl = 1402.7700
    elif '1334' in ion:
        restwl = 1334.5323
    elif '1548' in ion:
        restwl = 1548.2049
    elif '1550' in ion:
        restwl = 1550.7785
    else:
        raise ValueError('cant find input ion: {}'.format(ion))

    v = ((input_arr - restwl)/restwl)*c

    return v


# set up figure for LA sightlines

plt.figure(figsize=(12,8))
gs = gridspec.GridSpec(2, 3, wspace=0.3, hspace=0.3)

i, j = 0, 0

for key in sldict:

    if sldict[key]['dir'] == 'LA':

        ax = plt.subplot(gs[i, j])

        for m, (ion, ion_label) in enumerate(zip(sldict[key]['ions'],sldict[key]['ion_label'])):

            slpath = os.path.join(rootdir, key, key + '-' + ion)
            comp, zval, zval_err, bval, bval_err, nval, nval_err, wlarr, fluxarr_err, \
            fluxarr, bestfitarr, maskarr = extract_fits(slpath)

            v_arr = wl_to_v(wlarr, ion_label)

            if m == 0:
                ax.plot(v_arr, fluxarr, color='orange', linestyle='-', label=ion_label)
                ax.plot(v_arr, bestfitarr, color='black', linestyle='-', label='Best Fit')
                for zcomp in zval:
                    vcomp = zcomp*c
                    ax.axvline(vcomp, color='orange', linestyle='--')

            elif m == 1:
                ax.plot(v_arr, fluxarr+0.75, color='deepskyblue', linestyle='-', label=ion_label)
                ax.plot(v_arr, bestfitarr+0.75, color='black', linestyle='-')
                for zcomp in zval:
                    vcomp = zcomp*c
                    ax.axvline(vcomp, color='deepskyblue', linestyle='--')

            else:
                ax.plot(v_arr, fluxarr+1.25, color='limegreen', linestyle='-', label=ion_label)
                ax.plot(v_arr, bestfitarr+1.25, color='black', linestyle='-')
                for zcomp in zval:
                    vcomp = zcomp*c
                    ax.axvline(vcomp, color='limegreen', linestyle='--')

        ax.set_xlim(-300.,+500.)
        ax.set_xlabel('Relative Velocity [km/s]')
        ax.set_ylabel('Normalized Flux')
        ax.set_title(key)
        handles, labels = ax.get_legend_handles_labels()
        handles = [handles[0], handles[2], handles[1]]
        labels = [labels[0], labels[2], labels[1]]
        ax.legend(handles, labels, prop={'size': 6})

        j = j+1
        if j == 3:
            j = 0
            i = 1

plt.suptitle('Leading Arm Sightlines')

plt.show()

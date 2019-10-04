import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# import glob
import os
import numpy as np
import pickle

plt.rc('font', family='Arial')

ROOTDIR = '/Users/efrazer/leadingarm/sightlines/'
PICKLEFILE = '/Users/efrazer/leadingarm/fitdict.pickle'
C = 299792.0  # km/s

IONSTOUSE = {'SDSSJ234500.43-005936.0': ['SiII_1260', 'SiIII_1206', 'SiIV_1393'],
             'RBS1897': ['SiII_1260', 'SiIII_1206'],
             'SDSSJ015530.02-085704.0': ['SiII_1193', 'SiIII_1206', 'SiIV_1393'],
             'IO-AND': ['SiII_1193', 'SiIII_1206', 'SiIV_1393'],
             'MRC2251-178': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'SDSSJ095915.60+050355.0': ['SiIII_1206', 'CIV_1548'],
             'RBS144': ['SiII_1193', 'SiIII_1206'],
             'PG0026+129': ['CII_1334', 'SiIII_1206', 'SiIV_1393'],
             'PKS1136-13': ['CII_1334'],
             'HE0153-4520': ['SiII_1260', 'SiIII_1206'],
             'FAIRALL9': ['SiII_1193', 'SiIII_1206', 'SiIV_1402'],
             'MRK304': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'LBQS0107-0233': ['SiIII_1206', 'CIV_1548'],
             'PKS1101-325': ['SiII_1190'],
             'PG1049-005': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'SDSSJ094331.60+053131.0': ['SiII_1193', 'SiIII_1206'],
             'NGC3125': ['SiII_1190'],
             'SDSSJ001224.01-102226.5': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'PG0003+158': ['SiII_1193', 'SiIII_1206', 'CIV_1548'],
             'PHL1811': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'UVQSJ101629.20-315023.6': ['SiII_1193', 'SiIII_1206'],
             'MRK1513': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'RX_J0209.5-0438': ['CII_1334', 'CIV_1548'],
             'ESO265-G23': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'PHL2525': ['CII_1334', 'CIV_1548'],
             'PG0044+030': ['CII_1334', 'SiIII_1206'],
             'ESO267-G13': ['SiII_1193'],
             'NGC7714': [],
             'MRK1044': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'CD14-A05': [],
             'UGC12163': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'LBQS0107-0235': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'HE1159-1338': ['SiII_1193', 'SiIII_1206'],
             'MRK335': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PG1011-040': ['SiII_1260', 'SiIII_1206'],
             'IRAS_F09539-0439': ['SiII_1190', 'SiIV_1393'],
             'PG2349-014': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'H1101-232': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'SDSSJ225738.20+134045.0': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'HE0226-4110': ['CII_1334', 'SiIII_1206', 'CIV_1548']
             }


# -------------------------------------------------------------

def wl_to_v(input_dict, ionval):
    """convert wavelength to velocity offset
    """

    if '1190' in ionval:
        restwl = 1190.4158
        col = 'orange'
        lab = 'Si II ' + r'$\lambda$' + '1190'
        key = 'SiII'
        lev = 0
    elif '1193' in ionval:
        restwl = 1193.2897
        col = 'orange'
        lab = 'Si II ' + r'$\lambda$' + '1193'
        key = 'SiII'
        lev = 0
    elif '1260' in ionval:
        restwl = 1260.4221
        col = 'orange'
        lab = 'Si II ' + r'$\lambda$' + '1260'
        key = 'SiII'
        lev = 0
    elif '1253' in ionval:
        restwl = 1253.8110
        col = 'orange'
        lab = 'Si II ' + r'$\lambda$' + '1253'
        key = 'SiII'
        lev = 0
    elif '1206' in ionval:
        restwl = 1206.5000
        col = 'deeppink'
        lab = 'Si III ' + r'$\lambda$' + '1206'
        key = 'SiIII'
        lev = 1
    elif '1393' in ionval:
        restwl = 1393.7550
        col = 'deepskyblue'
        lab = 'Si IV ' + r'$\lambda$' + '1393'
        key = 'SiIV'
        lev = 2
    elif '1402' in ionval:
        restwl = 1402.7700
        col = 'deepskyblue'
        lab = 'Si IV ' + r'$\lambda$' + '1402'
        key = 'SiIV'
        lev = 2
    elif '1334' in ionval:
        restwl = 1334.5323
        col = 'orange'
        lab = 'C II ' + r'$\lambda$' + '1334'
        key = 'CII'
        lev = 0
    elif '1548' in ionval:
        restwl = 1548.2049
        col = 'deepskyblue'
        lab = 'C IV ' + r'$\lambda$' + '1548'
        key = 'CIV'
        lev = 2
    elif '1550' in ionval:
        restwl = 1550.7785
        col = 'deepskyblue'
        lab = 'C IV ' + r'$\lambda$' + '1550'
        key = 'CIV'
        lev = 2
    else:
        raise ValueError('cant find input ion: {}'.format(ionval))

    wavearr = np.array(input_dict[key]['wavelength'])

    v = ((wavearr - restwl)/restwl) * C

    return v, col, lab, key, lev


# -------------------------------------------------------------

if __name__ == '__main__':

    # unload the dictionary
    with open(PICKLEFILE, 'rb') as handle:
        fitdict = pickle.load(handle)

    # collect the data
    for sightline in fitdict:

        ionlist = IONSTOUSE[sightline]

        if len(ionlist) > 1:

            fig, axes = plt.subplots(3, 1, sharex=True, sharey=True, figsize=(7, 9))

            for ion in ionlist:

                vel_arr, colorval, labelval, keyval, level = wl_to_v(fitdict[sightline], ion)

                axes[level].plot(vel_arr, fitdict[sightline][keyval]['flux'],
                                 color=colorval, linestyle='-', label=labelval)
                axes[level].plot(vel_arr, fitdict[sightline][keyval]['best fit line'],
                                 color='black', linestyle='-', label='Best Fit')

                for zcomp in fitdict[sightline][keyval]['components']['redshift']:
                    vcomp = zcomp*C
                    axes[level].axvline(vcomp, color=colorval, linestyle='--')

                axes[level].legend(prop={'size': 12})
                direction = fitdict[sightline][keyval]['direction'][0].split('-')[0]

            for n in np.arange(0, 3):
                axes[n].set_ylim(-0.1, 1.5)
                axes[n].set_yticks(np.arange(0, 1.6, 0.2))
                axes[n].set_xticks(np.arange(-600, 700, 100))
                axes[n].set_axisbelow(True)
                axes[n].yaxis.grid(color='lightgray', linestyle='dashed')
                axes[n].xaxis.grid(color='lightgray', linestyle='dashed')
                plt.setp(axes[n].get_xticklabels(), fontsize=12)
                plt.setp(axes[n].get_yticklabels(), fontsize=12)

            fig.subplots_adjust(hspace=0)
            axes[0].set_title('{}   ({})'.format(sightline, direction), fontsize=20)
            axes[0].set_xlim(-600, 600)
            fig.add_subplot(111, frameon=False)
            plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
            plt.xlabel('velocity (' + r'$km\>s^{-1}$' + ')', fontsize=16)
            plt.ylabel("normalized flux", fontsize=16)

            plt.show()

        else:
            continue

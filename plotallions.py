import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# import glob
import os
import numpy as np
import pickle

plt.rc('font', family='Arial')
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'

ROOTDIR = '/Users/efrazer/leadingarm/'
OUTFOLDER = 'stackfigs'
PICKLEFILE = '/Users/efrazer/leadingarm/fitdict_test.pickle'
C = 299792.0  # km/s

IONSTOUSE = {'ESO265-G23': ['SiII_1193', 'SiIII_1206', 'SiIV_1393'],
             'FAIRALL9': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'H1101-232': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'HE0153-4520': ['SiII_1190', 'SiIII_1206'],
             'HE0226-4110': ['CII_1334', 'SiIII_1206', 'CIV_1550'],
             'HE1159-1338': ['SiII_1193', 'SiIII_1206'],
             'IO-AND': ['SiII_1193', 'SiIII_1206', 'SiIV_1393'],
             'IRAS_F09539-0439': ['SiII_1190', 'SiIV_1393'],
             'LBQS0107-0235': ['CII_1334', 'SiIII_1206'],
             'MRC2251-178': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'MRK304': ['CII_1334', 'SiIII_1206', 'CIV_1550'],
             'MRK335': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'MRK1044': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'MRK1513': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PG0003+158': ['SiII_1193', 'SiIII_1206', 'CIV_1548'],
             'PG0026+129': ['CII_1334', 'SiIII_1206', 'SiIV_1393'],
             'PG0044+030': ['CII_1334', 'SiIII_1206'],
             'PG1011-040': ['SiII_1193', 'SiIII_1206'],
             'PG1049-005': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PG2349-014': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             'PHL1811': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PHL2525': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'PKS1101-325': ['SiII_1193', 'SiIII_1206'],
             'PKS1136-13': ['CII_1334', 'SiIII_1206'],
             'RBS144': ['SiII_1193', 'SiIII_1206'],
             'RBS1897': ['SiII_1260', 'SiIII_1206'],
             'SDSSJ015530.02-085704.0': ['SiII_1260', 'SiIII_1206', 'SiIV_1393'],
             'SDSSJ095915.60+050355.0': ['SiIII_1206', 'CIV_1548'],
             'SDSSJ234500.43-005936.0': ['SiII_1260', 'SiIII_1206', 'SiIV_1393'],
             'UGC12163': ['CII_1334', 'SiIII_1206', 'CIV_1548'],
             'UVQSJ101629.20-315023.6': ['SiII_1260', 'SiIII_1206'],
             # 'ESO267-G13': ['SiII_1193'],
             # 'LBQS0107-0233': ['SiIII_1206', 'CIV_1548'],
             # 'NGC3125': ['SiII_1190'],
             # 'RX_J0209.5-0438': ['CII_1334', 'CIV_1548'],
             # 'SDSSJ001224.01-102226.5': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             # 'SDSSJ094331.60+053131.0': ['SiII_1193', 'SiIII_1206'],
             # 'SDSSJ225738.20+134045.0': ['SiII_1190', 'SiIII_1206', 'SiIV_1393'],
             }


# -------------------------------------------------------------

def wl_to_v(input_dict, ionval):
    """convert wavelength to velocity offset
    """

    if '1190' in ionval:
        restwl = 1190.4158
        col = 'orange'
        lab = 'Si II ' + r'$\mathrm{\lambda}$' + '1190'
        key = 'SiII'
        lev = 0
    elif '1193' in ionval:
        restwl = 1193.2897
        col = 'orange'
        lab = 'Si II ' + r'$\mathrm{\lambda}$' + '1193'
        key = 'SiII'
        lev = 0
    elif '1260' in ionval:
        restwl = 1260.4221
        col = 'orange'
        lab = 'Si II ' + r'$\mathrm{\lambda}$' + '1260'
        key = 'SiII'
        lev = 0
    elif '1253' in ionval:
        restwl = 1253.8110
        col = 'orange'
        lab = 'Si II ' + r'$\mathrm{\lambda}$' + '1253'
        key = 'SiII'
        lev = 0
    elif '1206' in ionval:
        restwl = 1206.5000
        col = 'deeppink'
        lab = 'Si III ' + r'$\mathrm{\lambda}$' + '1206'
        key = 'SiIII'
        lev = 1
    elif '1393' in ionval:
        restwl = 1393.7550
        col = 'deepskyblue'
        lab = 'Si IV ' + r'$\mathrm{\lambda}$' + '1393'
        key = 'SiIV'
        lev = 2
    elif '1402' in ionval:
        restwl = 1402.7700
        col = 'deepskyblue'
        lab = 'Si IV ' + r'$\mathrm{\lambda}$' + '1402'
        key = 'SiIV'
        lev = 2
    elif '1334' in ionval:
        restwl = 1334.5323
        col = 'orange'
        lab = 'C II ' + r'$\mathrm{\lambda}$' + '1334'
        key = 'CII'
        lev = 0
    elif '1548' in ionval:
        restwl = 1548.2049
        col = 'deepskyblue'
        lab = 'C IV ' + r'$\mathrm{\lambda}$' + '1548'
        key = 'CIV'
        lev = 2
    elif '1550' in ionval:
        restwl = 1550.7785
        col = 'deepskyblue'
        lab = 'C IV ' + r'$\mathrm{\lambda}$' + '1550'
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

        if len(ionlist) == 1:

            fig, axes = plt.subplots(len(ionlist), 1, sharex=True, sharey=True, figsize=(6, 6))

            for i, ion in enumerate(ionlist):

                vel_arr, colorval, labelval, keyval, level = wl_to_v(fitdict[sightline], ion)

                axes.plot(vel_arr, fitdict[sightline][keyval]['flux'],
                          color=colorval, linestyle='-', label=labelval)
                axes.plot(vel_arr, fitdict[sightline][keyval]['best fit line'],
                          color='black', linestyle='-', label='Best Fit')

                for zcomp in fitdict[sightline][keyval]['components']['redshift']:
                    vcomp = zcomp*C
                    axes.axvline(vcomp, color=colorval, linestyle='--')

                if sightline == 'UGC12163':
                    axes.legend(prop={'size': 12}, loc=4)
                else:
                    axes.legend(prop={'size': 12})
                direction = fitdict[sightline][keyval]['direction']

            axes.set_ylim(-0.1, 1.5)
            axes.set_yticks(np.arange(0, 1.5, 0.5))
            axes.set_xticks(np.arange(-600, 700, 100))
            axes.set_axisbelow(True)
            axes.yaxis.grid(color='lightgray', linestyle='dashed')
            axes.xaxis.grid(color='lightgray', linestyle='dashed')
            plt.setp(axes.get_xticklabels(), fontsize=12)
            plt.setp(axes.get_yticklabels(), fontsize=12)

            fig.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
            plt.margins(0, 0)

            axes.set_title('{}   ({})'.format(sightline, direction), fontsize=20)
            if direction == 'LA':
                axes.set_xlim(-400, 500)
            elif sightline == 'UGC12163':
                axes.set_xlim(-600, 400)
            elif vcomp < 0:
                axes.set_xlim(-500, 400)
            elif vcomp > 0:
                axes.set_xlim(-400, 500)
            else:
                axes.set_xlim(-500, 500)
            fig.add_subplot(111, frameon=False)
            plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
            plt.xlabel('velocity (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
            plt.ylabel("normalized flux", fontsize=16)
            # plt.tight_layout(h_pad=0.5)
            plt.savefig(os.path.join(ROOTDIR, OUTFOLDER, '{}.pdf'.format(sightline)),
                        bbox_inches='tight', pad_inches=0.1)
            plt.close()

        if len(ionlist) > 1:

            fig, axes = plt.subplots(len(ionlist), 1, sharex=True, sharey=True, figsize=(6, 6))

            for i, ion in enumerate(ionlist):

                vel_arr, colorval, labelval, keyval, level = wl_to_v(fitdict[sightline], ion)

                axes[i].plot(vel_arr, fitdict[sightline][keyval]['flux'],
                             color=colorval, linestyle='-', label=labelval)
                axes[i].plot(vel_arr, fitdict[sightline][keyval]['best fit line'],
                             color='black', linestyle='-', label='Best Fit')

                for zcomp in fitdict[sightline][keyval]['components']['redshift']:
                    vcomp = zcomp*C
                    axes[i].axvline(vcomp, color=colorval, linestyle='--')

                if sightline == 'UGC12163':
                    axes[i].legend(prop={'size': 12}, loc=4)
                else:
                    axes[i].legend(prop={'size': 12})
                direction = fitdict[sightline][keyval]['direction']

            for n in np.arange(len(ionlist)):
                axes[n].set_ylim(-0.1, 1.5)
                axes[n].set_yticks(np.arange(0, 1.5, 0.5))
                axes[n].set_xticks(np.arange(-600, 700, 100))
                axes[n].set_axisbelow(True)
                axes[n].yaxis.grid(color='lightgray', linestyle='dashed')
                axes[n].xaxis.grid(color='lightgray', linestyle='dashed')
                plt.setp(axes[n].get_xticklabels(), fontsize=12)
                plt.setp(axes[n].get_yticklabels(), fontsize=12)

            if sightline == 'PG0044+030':
                axes[1].text(-385, 0.85, 'B')
            if sightline == 'PG0026+129':
                axes[0].text(-360, 0.8, 'B')
            if sightline == 'SDSSJ234500.43-005936.0':
                axes[0].text(-230, 0.6, 'B')
            if sightline == 'PG1049-005':
                axes[0].text(240, 0.6, 'CII*')
                axes[0].text(75, 0.3, 'N')
                axes[1].text(60, 0.4, 'N')
            if sightline == 'PG1011-040':
                axes[0].text(85, 0.4, 'U')
            if sightline == 'PKS1136-13':
                axes[1].text(180, 1.05, 'U')
            if sightline == 'ESO265-G23':
                axes[0].text(130, 0.2, 'N')
            if sightline == 'FAIRALL9':
                axes[0].text(45, 0.3, 'N')
                axes[0].text(235, 0.6, 'CII*')
                axes[2].text(45, 0.6, 'N')
            if sightline == 'H1101-232':
                axes[2].text(135, 1, 'U')
                axes[0].text(-60, 0.9, 'N')
            if sightline == 'HE0153-4520':
                axes[0].text(-50, 0.55, 'N')
                axes[1].text(75, 0.35, 'U')
            if sightline == 'HE0226-4110':
                axes[2].text(10, 0.75, 'N')
                axes[2].text(195, 1.0, 'U')
            if sightline == 'IRAS_F09539-0439':
                axes[1].text(75, 0.7, 'N')
            if sightline == 'LBQS0107-0235':
                axes[1].text(-280, 0.8, 'U')
                axes[1].text(-105, 0.65, 'N')
            if sightline == 'MRK335':
                axes[0].text(-250, 1.02, 'U')
            if sightline == 'PHL2525':
                axes[0].text(50, 0.4, 'N')
            if sightline == 'UVQSJ101629.20-315023.6':
                axes[0].text(120, 0.5, 'N')
            if sightline == 'IO-AND':
                axes[2].text(-90, 0.95, 'N')
            if sightline == 'PKS1101-325':
                axes[0].text(100, 0.12, 'N')
                axes[0].text(160, 0.18, 'N')
                axes[1].text(90, 0.12, 'N')
                axes[1].text(155, 0.15, 'N')
            if sightline == 'SDSSJ015530.02-085704.0':
                axes[1].text(150, 0.2, 'N')
                axes[1].text(340, 0.2, 'N')
                axes[2].text(-50, 0.8, 'N')
                axes[2].text(70, 1.05, 'N')

            fig.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
            plt.margins(0, 0)
            axes[0].set_title('{}   ({})'.format(sightline, direction), fontsize=20)
            if direction == 'LA':
                axes[0].set_xlim(-400, 500)
            elif sightline == 'UGC12163':
                axes[0].set_xlim(-600, 400)
            elif vcomp < 0:
                axes[0].set_xlim(-500, 400)
            elif vcomp > 0:
                axes[0].set_xlim(-400, 500)
            else:
                axes[0].set_xlim(-500, 500)
            fig.add_subplot(111, frameon=False)
            plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
            plt.xlabel('velocity (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
            plt.ylabel("normalized flux", fontsize=16)
            # plt.tight_layout(h_pad=0.5)
            plt.savefig(os.path.join(ROOTDIR, OUTFOLDER, '{}.pdf'.format(sightline)),
                        bbox_inches='tight', pad_inches=0.1)
            plt.close()

        else:
            continue

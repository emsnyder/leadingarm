import matplotlib.pyplot as plt
import os
import numpy as np
import scipy.stats as scs
import matplotlib.patheffects as pe
import pickle

plt.rc('font', family='Arial')
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Arial'

ROOTDIR = '/Users/efrazer/leadingarm/sightlines/'
OUTDIR = '/Users/efrazer/leadingarm/figures/'
PICKLEFILE = '/Users/efrazer/leadingarm/fitdict.pickle'

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
             'PKS1136-13': ['CII_1334'],  # removed  'SiIII_1206' since no comps there
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


# ------------------------------------------------------------
def getoffsets(infodict, direction, ion1, ion2):

    vlist = []

    for sightline in infodict:

        dubions = IONSTOUSE[sightline]

        ions = [dubion.split('_')[0] for dubion in dubions]

        if (ion1 in ions) & (ion2 in ions):

            if (direction in infodict[sightline][ion1]['direction']) &\
                    (direction in infodict[sightline][ion2]['direction']):

                listofmins = []

                for vcomp1 in fitdict[sightline][ion1]['components']['redshift']:

                    alllist = []

                    for vcomp2 in fitdict[sightline][ion2]['components']['redshift']:

                        deltav = (vcomp1 - vcomp2) * 3.e5
                        alllist.append(deltav)

                    # print(sightline, alllist)

                    listofmins.append(min(alllist, key=abs))

                vlist.extend(listofmins)

            else:
                continue

        else:
            continue

    return vlist


# ------------------------------------------------------------
def plotvelocities(direction, vellist1, vellist2, minbin, maxbin, xaxrange,
                   label1='Low - Med', label2='Low - High', outname='{}_veloffsets'):

    vellist1 = np.array(vellist1)
    vellist2 = np.array(vellist2)

    sel1 = np.where(np.abs(vellist1) < xaxrange)
    sel2 = np.where(np.abs(vellist2) < xaxrange)

    mean1 = np.mean(vellist1[sel1])
    mean2 = np.mean(vellist2[sel2])
    var1 = np.var(vellist1[sel1])
    var2 = np.var(vellist2[sel2])
    sigma1 = np.sqrt(var1)
    sigma2 = np.sqrt(var2)
    x1 = np.linspace(min(vellist1)-50., max(vellist1)+50., 200)
    x2 = np.linspace(min(vellist2)-50., max(vellist2)+50., 200)
    print('{} Statistics'.format(direction))
    print('{} mean = {}, sigma = {}'.format(label1, mean1, sigma1))
    print('{} mean = {}, sigma = {}'.format(label2, mean2, sigma2))

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.set_axisbelow(True)
    ax.yaxis.grid(color='lightgray', linestyle='dashed')
    ax.xaxis.grid(color='lightgray', linestyle='dashed')

    plt.plot(x1, scs.norm.pdf(x1, mean1, sigma1), label='Gaussian for {}'.format(label1),
             color='deeppink', linewidth=3, linestyle='dashed', alpha=0.7)
    plt.plot(x2, scs.norm.pdf(x2, mean2, sigma2), label='Gaussian for {}'.format(label2),
             color='deepskyblue', linewidth=3, linestyle='dashed', alpha=0.7)

    binwidth = 20.

    nums, bins, patches = plt.hist((vellist1, vellist2),
                                   bins=np.arange(minbin, maxbin, binwidth),
                                   color=['deeppink', 'deepskyblue'],
                                   alpha=0.7,
                                   rwidth=0.8,
                                   edgecolor='k',
                                   align='mid',
                                   density=True,
                                   label=['{}, N={}'.format(label1, len(vellist1)),
                                          '{}, N={}'.format(label2, len(vellist2))])

    plt.xlabel('velocity offset (' + r'$\mathrm{km\>s^{-1}}$' + ')', fontsize=16)
    plt.xticks(bins)
    plt.ylabel('relative number', fontsize=16)
    # plt.yticks(np.arange(np.max(n_ms))+1)
    plt.xlim(minbin, maxbin)
    plt.title('{} Sightlines'.format(direction), fontsize=20)
    plt.legend(prop={'size': 12})
    plt.setp(ax.get_xticklabels(), fontsize=14)
    plt.setp(ax.get_yticklabels(), fontsize=14)
    # plt.show()
    plt.savefig(os.path.join(OUTDIR, outname.format(direction) + '.pdf'))
    plt.close()


# ------------------------------------------------------------
if __name__ == '__main__':

    # unload the dictionary
    with open(PICKLEFILE, 'rb') as handle:
        fitdict = pickle.load(handle)

    # compute velocity offsets
    vel_ms_si_ii_iv = getoffsets(fitdict, 'MS', 'SiII', 'SiIV')
    vel_ms_si_ii_iii = getoffsets(fitdict, 'MS', 'SiII', 'SiIII')
    vel_ms_c_ii_si_iii = getoffsets(fitdict, 'MS', 'CII', 'SiIII')
    vel_ms_c_ii_iv = getoffsets(fitdict, 'MS', 'CII', 'CIV')

    ms_lowmed = vel_ms_si_ii_iii + vel_ms_c_ii_si_iii
    ms_lowhigh = vel_ms_si_ii_iv + vel_ms_c_ii_iv

    # plot the offsets
    plotvelocities('Magellanic Stream', ms_lowmed, ms_lowhigh, -80, 100, 60.)

    # compute velocity offsets
    vel_la_si_ii_iv = getoffsets(fitdict, 'LA', 'SiII', 'SiIV')
    vel_la_si_ii_iii = getoffsets(fitdict, 'LA', 'SiII', 'SiIII')
    vel_la_c_ii_si_iii = getoffsets(fitdict, 'LA', 'CII', 'SiIII')
    vel_la_c_ii_iv = getoffsets(fitdict, 'LA', 'CII', 'CIV')

    la_lowmed = vel_la_si_ii_iii + vel_la_c_ii_si_iii
    la_lowhigh = vel_la_si_ii_iv + vel_la_c_ii_iv

    # plot the offsets
    plotvelocities('Leading Arm', la_lowmed, la_lowhigh, -100, 100, 60.)

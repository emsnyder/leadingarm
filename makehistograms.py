import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
import glob
import os
import numpy as np
from scipy import stats

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


def extract_fits(input_file):
    compnum = []
    ion = []
    z = []
    z_err = []
    b = []
    b_err = []
    n = []
    n_err = []
    fitfile = open(input_file, 'r')
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

    return compnum, z, z_err, b, b_err, n, n_err


blist_la_lo = []
berrlist_la_lo = []
blist_ms_lo = []
berrlist_ms_lo = []
blist_la_med = []
berrlist_la_med = []
blist_ms_med = []
berrlist_ms_med = []
blist_la_hi = []
berrlist_la_hi = []
blist_ms_hi = []
berrlist_ms_hi = []
nlist_la_lo = []
nerrlist_la_lo = []
nlist_ms_lo = []
nerrlist_ms_lo = []
nlist_la_med = []
nerrlist_la_med = []
nlist_ms_med = []
nerrlist_ms_med = []
nlist_la_hi = []
nerrlist_la_hi = []
nlist_ms_hi = []
nerrlist_ms_hi = []

for key in sldict:

    if sldict[key]['dir'] == 'LA':

        slpath = os.path.join(rootdir, key, key + '-*.fit')
        fitfiles = glob.glob(os.path.join(rootdir, slpath))

        for myfile in fitfiles:

            cnum, z, z_err, b, b_err, n, n_err = extract_fits(myfile)

            if ('OI.fit' in myfile) or ('CII.fit' in myfile) or ('SII.fit' in myfile):

                for comp, bval, b_errval in zip(cnum, b, b_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_la_lo.append(bval)
                    berrlist_la_lo.append(b_errval)

            elif 'SiII.fit' in myfile:

                for comp, bval, b_errval, nval, n_errval in zip(cnum, b, b_err, n, n_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_la_lo.append(bval)
                    berrlist_la_lo.append(b_errval)
                    nlist_la_lo.append(nval)
                    nerrlist_la_lo.append(n_errval)

            elif 'SiIII.fit' in myfile:

                for comp, bval, b_errval, nval, n_errval in zip(cnum, b, b_err, n, n_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_la_med.append(bval)
                    berrlist_la_med.append(b_errval)
                    nlist_la_med.append(nval)
                    nerrlist_la_med.append(n_errval)

            elif 'CIV.fit' in myfile:

                for comp, bval, b_errval in zip(cnum, b, b_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_la_hi.append(bval)
                    berrlist_la_hi.append(b_errval)

            elif 'SiIV.fit' in myfile:

                for comp, bval, b_errval, nval, n_errval in zip(cnum, b, b_err, n, n_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_la_hi.append(bval)
                    berrlist_la_hi.append(b_errval)
                    nlist_la_hi.append(nval)
                    nerrlist_la_hi.append(n_errval)

            else:
                raise ValueError('???')

    elif sldict[key]['dir'] == 'MS':

        slpath = os.path.join(rootdir, key, key + '-*.fit')
        fitfiles = glob.glob(os.path.join(rootdir, slpath))

        for myfile in fitfiles:
            cnum, z, z_err, b, b_err, n, n_err = extract_fits(myfile)

            if ('OI.fit' in myfile) or ('CII.fit' in myfile) or ('SII.fit' in myfile):

                for comp, bval, b_errval in zip(cnum, b, b_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_ms_lo.append(bval)
                    berrlist_ms_lo.append(b_errval)

            elif 'SiII.fit' in myfile:

                for comp, bval, b_errval, nval, n_errval in zip(cnum, b, b_err, n, n_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_ms_lo.append(bval)
                    berrlist_ms_lo.append(b_errval)
                    nlist_ms_lo.append(nval)
                    nerrlist_ms_lo.append(n_errval)

            elif 'SiIII.fit' in myfile:

                for comp, bval, b_errval, nval, n_errval in zip(cnum, b, b_err, n, n_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_ms_med.append(bval)
                    berrlist_ms_med.append(b_errval)
                    nlist_ms_med.append(nval)
                    nerrlist_ms_med.append(n_errval)

            elif 'CIV.fit' in myfile:

                for comp, bval, b_errval in zip(cnum, b, b_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_ms_hi.append(bval)
                    berrlist_ms_hi.append(b_errval)

            elif 'SiIV.fit' in myfile:

                for comp, bval, b_errval, nval, n_errval in zip(cnum, b, b_err, n, n_err):
                    if comp == 0:
                        continue
                    if bval < 10.:
                        continue
                    if bval > 70.:
                        continue
                    blist_ms_hi.append(bval)
                    berrlist_ms_hi.append(b_errval)
                    nlist_ms_hi.append(nval)
                    nerrlist_ms_hi.append(n_errval)

            else:
                raise ValueError('???')
    else:
        raise ValueError('what')

binwidth = 10.
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
n_la, bins_la, patches_la = plt.hist((blist_la_lo, blist_la_hi), bins=np.arange(10, 80, binwidth),
                                     color=['orange', 'deepskyblue'], alpha=0.7, rwidth=0.8, align='mid',
                                     label=['Low Ions (O I, Si II, C II, S II), N={}'.format(len(blist_la_lo)),
                                            'High Ions (Si IV, C IV), N={}'.format(len(blist_la_hi))])
kstest_la_b = stats.ks_2samp(blist_la_hi, blist_la_lo)
plt.text(49, 6, 'K-S Statistic p-value={:6.5f}'.format(kstest_la_b[1]))
plt.xlabel('b-value ' + r'$[km/s]$', fontsize=16)
plt.xticks(bins_la)
plt.ylabel('# of components', fontsize=16)
plt.yticks(np.arange(np.max(n_la))+1)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-b-LA.pdf')
plt.close()


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
n_ms, bins_ms, patches_ms = plt.hist((blist_ms_lo, blist_ms_hi), bins=np.arange(10, 80, binwidth),
                                     color=['orange', 'deepskyblue'], alpha=0.7, rwidth=0.8, align='mid',
                                     label=['Low Ions (O I, Si II, C II), N={}'.format(len(blist_ms_lo)),
                                            'High Ions (Si IV, C IV), N={}'.format(len(blist_ms_hi))])
kstest_ms_b = stats.ks_2samp(blist_ms_hi, blist_ms_lo)
plt.text(49, 4.3, 'K-S Statistic p-value={:6.5f}'.format(kstest_ms_b[1]))
plt.xlabel('b-value ' + r'$[km/s]$', fontsize=16)
plt.xticks(bins_ms)
plt.ylabel('# of components', fontsize=16)
plt.yticks(np.arange(np.max(n_ms))+1)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-b-MS.pdf')
plt.close()


# Make the Column Density Plots now

binwidth = 0.25
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
n_la_ncol, bins_la_ncol, patches_la_ncol = plt.hist((nlist_la_lo, nlist_la_med, nlist_la_hi),
                                                    bins=np.arange(12.25, 14.5, binwidth),
                                                    color=['orange', 'deeppink', 'deepskyblue'],
                                                    align='mid', histtype='bar', rwidth=0.8, alpha=0.7,
                                                    label=['Si II, N={}'.format(len(nlist_la_lo)),
                                                           'Si III, N={}'.format(len(nlist_la_med)),
                                                           'Si IV, N={}'.format(len(nlist_la_hi))])
plt.xlabel('Column Density ' + r'$[\log(N/cm^{-2})]$', fontsize=16)
plt.xticks(bins_la_ncol)
plt.ylabel('# of components', fontsize=16)
plt.yticks(np.arange(np.max(n_la_ncol))+1)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-N-LA.pdf')
plt.close()


binwidth = 0.25
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
n_ms_ncol, bins_ms_ncol, patches_ms_ncol = plt.hist((nlist_ms_lo, nlist_ms_med, nlist_ms_hi),
                                                    bins=np.arange(12.25, 14.0, binwidth),
                                                    color=['orange', 'deeppink', 'deepskyblue'],
                                                    align='mid', histtype='bar', rwidth=0.8, alpha=0.7,
                                                    label=['Si II, N={}'.format(len(nlist_ms_lo)),
                                                           'Si III, N={}'.format(len(nlist_ms_med)),
                                                           'Si IV, N={}'.format(len(nlist_ms_hi))])
plt.xlabel('Column Density ' + r'$[\log(N/cm^{-2})]$', fontsize=16)
plt.xticks(bins_ms_ncol)
plt.ylabel('# of components', fontsize=16)
plt.yticks(np.arange(np.max(n_ms_ncol))+1)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-N-MS.pdf')
plt.close()

print('Leading Arm high ion b values = {}'.format(blist_la_hi))
print('Leading Arm low ion b values = {}'.format(blist_la_lo))
print('Stream high ion b values = {}'.format(blist_ms_hi))
print('Stream low ion b values = {}'.format(blist_ms_lo))

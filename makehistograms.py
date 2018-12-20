import matplotlib.pyplot as plt
# import matplotlib.gridspec as gridspec
import glob
import os
import numpy as np

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

                for bval, b_errval in zip(b, b_err):
                    blist_la_lo.append(bval)
                    berrlist_la_lo.append(b_errval)

            elif 'SiII.fit' in myfile:

                for bval, b_errval, nval, n_errval in zip(b, b_err, n, n_err):
                    blist_la_lo.append(bval)
                    berrlist_la_lo.append(b_errval)
                    nlist_la_lo.append(nval)
                    nerrlist_la_lo.append(n_errval)

            elif 'SiIII.fit' in myfile:

                for bval, b_errval, nval, n_errval in zip(b, b_err, n, n_err):
                    blist_la_med.append(bval)
                    berrlist_la_med.append(b_errval)
                    nlist_la_med.append(nval)
                    nerrlist_la_med.append(n_errval)

            elif 'CIV.fit' in myfile:

                for bval, b_errval in zip(b, b_err):
                    blist_la_hi.append(bval)
                    berrlist_la_hi.append(b_errval)

            elif 'SiIV.fit' in myfile:

                for bval, b_errval, nval, n_errval in zip(b, b_err, n, n_err):
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

                for bval, b_errval in zip(b, b_err):
                    blist_ms_lo.append(bval)
                    berrlist_ms_lo.append(b_errval)

            elif 'SiII.fit' in myfile:

                for bval, b_errval, nval, n_errval in zip(b, b_err, n, n_err):
                    blist_ms_lo.append(bval)
                    berrlist_ms_lo.append(b_errval)
                    nlist_ms_lo.append(nval)
                    nerrlist_ms_lo.append(n_errval)

            elif 'SiIII.fit' in myfile:

                for bval, b_errval, nval, n_errval in zip(b, b_err, n, n_err):
                    blist_ms_med.append(bval)
                    berrlist_ms_med.append(b_errval)
                    nlist_ms_med.append(nval)
                    nerrlist_ms_med.append(n_errval)

            elif 'CIV.fit' in myfile:

                for bval, b_errval in zip(b, b_err):
                    blist_ms_hi.append(bval)
                    berrlist_ms_hi.append(b_errval)

            elif 'SiIV.fit' in myfile:

                for bval, b_errval, nval, n_errval in zip(b, b_err, n, n_err):
                    blist_ms_hi.append(bval)
                    berrlist_ms_hi.append(b_errval)
                    nlist_ms_hi.append(nval)
                    nerrlist_ms_hi.append(n_errval)

            else:
                raise ValueError('???')
    else:
        raise ValueError('what')

binwidth = 5.
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
n_la_lo, bins_la_lo, patches_la_lo = plt.hist(blist_la_lo,
                                              bins=np.arange(min(blist_la_lo), max(blist_la_lo) + binwidth, binwidth),
                                              color='orange', alpha=0.7, rwidth=0.85,
                                              label='Low Ions (O I, Si II, C II, S II)  N={}'.format(len(blist_la_lo)))
n_la_hi, bins_la_hi, patches_la_hi = plt.hist(blist_la_hi,
                                              bins=np.arange(min(blist_la_hi), max(blist_la_hi) + binwidth, binwidth),
                                              color='deepskyblue', alpha=0.7, rwidth=0.85,
                                              label='High Ions (Si IV, C IV)  N={}'.format(len(blist_la_hi)))
plt.xlabel('b-value [km/s]', fontsize=16)
plt.ylabel('N', fontsize=16)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-b-LA.pdf')

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
n_ms_lo, bins_ms_lo, patches_ms_lo = plt.hist(blist_ms_lo,
                                              bins=np.arange(min(blist_ms_lo), max(blist_ms_lo) + binwidth, binwidth),
                                              color='orange', alpha=0.7, rwidth=0.85,
                                              label='Low Ions (O I, Si II, C II)  N={}'.format(len(blist_ms_lo)))
n_ms_hi, bins_ms_hi, patches_ms_hi = plt.hist(blist_ms_hi,
                                              bins=np.arange(min(blist_ms_hi), max(blist_ms_hi) + binwidth, binwidth),
                                              color='deepskyblue', alpha=0.7, rwidth=0.85,
                                              label='High Ions (Si III, Si IV, C IV)  N={}'.format(len(blist_ms_hi)))
plt.xlabel('b-value [km/s]', fontsize=16)
plt.ylabel('N', fontsize=16)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-b-MS.pdf')


# Make the Column Density Plots now

binwidth = 0.3
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
n_la_lo_ncol, bins_la_lo_ncol, patches_la_lo_ncol = plt.hist(nlist_la_lo,
                                                             bins=np.arange(min(nlist_la_lo), max(nlist_la_lo) + binwidth, binwidth),
                                                             color='orange', alpha=0.7, rwidth=0.85,
                                                             label='Si II  N={}'.format(len(nlist_la_lo)))
n_la_med_ncol, bins_la_med_ncol, patches_la_med_ncol = plt.hist(nlist_la_med,
                                                                bins=np.arange(min(nlist_la_med), max(nlist_la_med) + binwidth, binwidth),
                                                                color='orange', alpha=0.7, rwidth=0.85,
                                                                label='Si III  N={}'.format(len(nlist_la_med)))
n_la_hi_ncol, bins_la_hi_ncol, patches_la_hi_ncol = plt.hist(nlist_la_hi,
                                                             bins=np.arange(min(nlist_la_hi), max(nlist_la_hi) + binwidth, binwidth),
                                                             color='deepskyblue', alpha=0.7, rwidth=0.85,
                                                             label='Si IV  N={}'.format(len(nlist_la_hi)))
plt.xlabel('Column Density [log(N/cm^-2)]', fontsize=16)
plt.ylabel('N', fontsize=16)
plt.title('Leading Arm Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-N-LA.pdf')

binwidth=0.3
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
n_ms_lo_ncol, bins_ms_lo_ncol, patches_ms_lo_ncol = plt.hist(nlist_ms_lo, bins=np.arange(min(nlist_ms_lo), max(nlist_ms_lo) + binwidth, binwidth), color='orange', alpha=0.7, rwidth=0.85, label='Low Ions (O I, Si II, C II)')
n_ms_hi_ncol, bins_ms_hi_ncol, patches_ms_hi_ncol = plt.hist(nlist_ms_hi, bins=np.arange(min(nlist_ms_hi), max(nlist_ms_hi) + binwidth, binwidth), color='deepskyblue', alpha=0.7, rwidth=0.85, label='High Ions (Si III, Si IV, C IV)')
plt.xlabel('Column Density [log(N/cm^-2)]', fontsize=16)
plt.ylabel('N', fontsize=16)
plt.title('Magellanic Stream Sightlines', fontsize=20)
plt.legend(prop={'size': 12})
plt.setp(ax.get_xticklabels(), fontsize=14)
plt.setp(ax.get_yticklabels(), fontsize=14)
plt.savefig('hist-N-MS.pdf')

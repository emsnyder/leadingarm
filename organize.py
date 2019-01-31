import os
import shutil
from astropy.io import fits

rootdir = '/Users/efrazer/leadingarm/'

datatable = '/Users/efrazer/leadingarm/datafile1418.fits'

data = fits.getdata(datatable)

for row in data:

    if not os.path.exists(os.path.join(rootdir, 'sightlines', row['target'])):

        os.makedirs(os.path.join(rootdir, 'sightlines', row['target']))

        newdir = os.path.join(rootdir, 'sightlines', row['target'])

        if os.path.isfile('/Users/efrazer/science/cosdata/{}-G160M'.format(row['target'])):

            shutil.copyfile('/Users/efrazer/science/cosdata/{}-G160M'.format(row['target']),
                            os.path.join(newdir, '{}-G160M'.format(row['target'])))

        elif os.path.isfile('/Users/efrazer/science/cosdata/{}_spec-G160M'.format(row['target'])):

            shutil.copyfile('/Users/efrazer/science/cosdata/{}_spec-G160M'.format(row['target']),
                            os.path.join(newdir, '{}-G160M'.format(row['target'])))

        else:

            pass

        if os.path.isfile('/Users/efrazer/science/cosdata/{}-G130M'.format(row['target'])):

            shutil.copyfile('/Users/efrazer/science/cosdata/{}-G130M'.format(row['target']),
                            os.path.join(newdir, '{}-G130M'.format(row['target'])))

        elif os.path.isfile('/Users/efrazer/science/cosdata/{}_spec-G130M'.format(row['target'])):

            shutil.copyfile('/Users/efrazer/science/cosdata/{}_spec-G130M'.format(row['target']),
                            os.path.join(newdir, '{}-G130M'.format(row['target'])))

        else:

            pass

        if os.path.isfile('/Users/efrazer/science/cosdata/{}-G130M-N'.format(row['target'])):

            shutil.copyfile('/Users/efrazer/science/cosdata/{}-G130M-N'.format(row['target']),
                            os.path.join(newdir, '{}-G130M-N'.format(row['target'])))

        elif os.path.isfile('/Users/efrazer/science/cosdata/{}_spec-G130M-N'.format(row['target'])):

            shutil.copyfile('/Users/efrazer/science/cosdata/{}_spec-G130M-N'.format(row['target']),
                            os.path.join(newdir, '{}-G130M-N'.format(row['target'])))

        else:

            pass

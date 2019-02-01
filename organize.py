import os
import shutil
from astropy.io import fits

rootdir = '/Users/efrazer/leadingarm/'

datatable = '/Users/efrazer/leadingarm/datafile1418.fits'

data = fits.getdata(datatable)

# for row in data:
#
#     if not os.path.exists(os.path.join(rootdir, 'sightlines', row['target'])):
#
#         os.makedirs(os.path.join(rootdir, 'sightlines', row['target']))
#
#         newdir = os.path.join(rootdir, 'sightlines', row['target'])
#
#         if os.path.isfile('/Users/efrazer/science/cosdata/{}-G160M'.format(row['target'])):
#
#             shutil.copyfile('/Users/efrazer/science/cosdata/{}-G160M'.format(row['target']),
#                             os.path.join(newdir, '{}-G160M'.format(row['target'])))
#
#         elif os.path.isfile('/Users/efrazer/science/cosdata/{}_spec-G160M'.format(row['target'])):
#
#             shutil.copyfile('/Users/efrazer/science/cosdata/{}_spec-G160M'.format(row['target']),
#                             os.path.join(newdir, '{}-G160M'.format(row['target'])))
#
#         else:
#
#             pass
#
#         if os.path.isfile('/Users/efrazer/science/cosdata/{}-G130M'.format(row['target'])):
#
#             shutil.copyfile('/Users/efrazer/science/cosdata/{}-G130M'.format(row['target']),
#                             os.path.join(newdir, '{}-G130M'.format(row['target'])))
#
#         elif os.path.isfile('/Users/efrazer/science/cosdata/{}_spec-G130M'.format(row['target'])):
#
#             shutil.copyfile('/Users/efrazer/science/cosdata/{}_spec-G130M'.format(row['target']),
#                             os.path.join(newdir, '{}-G130M'.format(row['target'])))
#
#         else:
#
#             pass
#
#         if os.path.isfile('/Users/efrazer/science/cosdata/{}-G130M-N'.format(row['target'])):
#
#             shutil.copyfile('/Users/efrazer/science/cosdata/{}-G130M-N'.format(row['target']),
#                             os.path.join(newdir, '{}-G130M-N'.format(row['target'])))
#
#         elif os.path.isfile('/Users/efrazer/science/cosdata/{}_spec-G130M-N'.format(row['target'])):
#
#             shutil.copyfile('/Users/efrazer/science/cosdata/{}_spec-G130M-N'.format(row['target']),
#                             os.path.join(newdir, '{}-G130M-N'.format(row['target'])))
#
#         else:
#
#             pass


# modified to add README files to each sightline directory

paths = ['/Users/efrazer/leadingarm/sightlines/3C57/README.md',
         '/Users/efrazer/leadingarm/sightlines/CD14-A05/README.md',
         '/Users/efrazer/leadingarm/sightlines/FAIRALL9/README.md',
         '/Users/efrazer/leadingarm/sightlines/IRAS_F09539-0439/README.md',
         '/Users/efrazer/leadingarm/sightlines/NGC3125/README.md',
         '/Users/efrazer/leadingarm/sightlines/NGC7714/README.md',
         '/Users/efrazer/leadingarm/sightlines/PHL2525/README.md',
         '/Users/efrazer/leadingarm/sightlines/PKS1101-325/README.md',
         '/Users/efrazer/leadingarm/sightlines/RBS144/README.md',
         '/Users/efrazer/leadingarm/sightlines/SDSSJ001224.01-102226.5/README.md',
         '/Users/efrazer/leadingarm/sightlines/SDSSJ095915.60+050355.0/README.md',
         '/Users/efrazer/leadingarm/sightlines/SDSSJ234500.43-005936.0/README.md',
         '/Users/efrazer/leadingarm/sightlines/UVQSJ101629.20-315023.6/README.md']

for row in data:
    path = os.path.join(rootdir, 'sightlines', row['target'],'README.md')

    if path not in paths:
        f = open(path,'w')
        f.write('##{}\n'.format(row['target']))
        f.write('**Found good fits for the following ions:**\n\n')
        f.write('Ion II 1400, 1405 using N components:\n')
        f.write('```\n')
        f.write('0 - MW\n')
        if 'MS' in row['region']:
            f.write('1 - Stream\n')
        elif 'LA' in row['region']:
            f.write('1 - Leading Arm\n')
        elif 'Bridge' in row['region']:
            f.write('1 - Bridge\n')
        elif 'LMC' in row['region']:
            f.write('1 - LMC\n')
        elif 'CHVC' in row['region']:
            f.write('1 - CHVC\n')
        else:
            f.write('1 - Stream\n')
        f.write('```\n\n\n')
        f.write('**Other Notes:**\n\n')
        f.close()

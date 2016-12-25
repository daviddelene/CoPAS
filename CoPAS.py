#!/usr/bin/env python

"""
NAME:
  CoPAS.py

PURPOSE:
  To facilitate the installation, setup, and integration of open source
  software and packages related to cloud physics, in-situ airborne data.

SYNTAX:
  CoPAS.py

NOTES:
  If available, script installs a binary distribution of the package.
  If no binary distribution is available, then a copy of the package repository
  is installed.

MODIFICATIONS:
  David Delene <delene@aero.und.edu> - 161224
    Written

  COPYRIGHT:
    2016 David Delene

    This program is distributed under terms of the GNU General Public License
 
    This file is part of Airborne Data Processing and Analysis (ADPAA).

    ADPAA is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    ADPAA is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ADPAA.  If not, see <http://www.gnu.org/licenses/>.

"""

import os
import sys
import tarfile
import urllib2

def help_message():
    print ('Syntax: CoPAS\n')

for param in sys.argv:
        if param.startswith('-h'):
                help_message()
                exit()

### Airborne Data Processing and Analysis (ADPAA) software package. ###
# Create directories.
print "Working on ADPAA"
if not os.path.isdir("ADPAA"):
    os.mkdir('ADPAA')
os.chdir('ADPAA')
if not os.path.isdir("binary_distributions"):
    os.mkdir('binary_distributions')
os.chdir('binary_distributions')

# Download tar file of binary package using progress bar.
url = "https://sourceforge.net/projects/adpaa/files/ADPAA.tar.gz"
file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "  Downloading ADPAA Binary Version: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()

# Extract distribution from compressed tar file.
print "  Extracting ADPAA distribution from compressed tar file"
tar = tarfile.open('ADPAA.tar.gz', "r:gz")
tar.extractall("..")
tar.close()
print "Finished ADPAA"

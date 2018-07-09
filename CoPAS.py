#!/usr/bin/env python

"""
NAME:
  CoPAS.py <https://github.com/daviddelene/CoPAS>

PURPOSE:
  To facilitate the installation, setup, and integration of open source
  software and packages related to cloud physics, in-situ airborne data.

Download/Clone CoPAS Distribution
  cd $HOME
  git clone https://github.com/daviddelene/CoPAS.git

EXECUTION EXAMPLE:
  mkdir ${HOME}/CoPAS_Packages
  cd ${HOME/CoPAS_Packages
  ${HOME}/COPAS/CoPAS.py

SYNTAX:
  CoPAS.py <-h|-s> <ADPAA> <ADTAE> <EGADS> <SAMAC> <SIMDATA> <SODA> <UIOPS> <nobinary> <notesting>

  If no parameter options, install all packages.
  
  <-h>    - Print Syntax message.
  <-s>    - Install source package in addition to binary package.
  ADPAA   - Install the ADPAA package.
  ADTAE   - Install the ADTAE package.
  EGADS   - install the EUFAR package.
  SAMAC   - Install the SAMAC package.
  SIMDATA - Download NCAR probe simulation data sets.
  SODA    - Install the SODA package.
  UIOPS   - Install the UIOPS package.
  <nobinary>  - Do not install binary packages.
  <notesting> - Do not test for support packages.

DEVELOPERS:
  David Delene <delene@aero.und.edu>
  Nick Gapp (njgapp) <nicholas.james.gapp@ndus.edu>
  Joseph Finlon (joefinlon) <finlon2@illinois.edu>

NOTES:
  If available, script installs a binary distribution of the package.
  If no binary distribution is available, then a copy of the package repository
  is installed.

  Program has three main parts:
    1.)  Tests to check for required python packages.
    2.)  Installing python packages.
    3.)  Cloning and update repositories.
  

MODIFICATIONS:
  David Delene <delene@aero.und.edu> - 2016/12/24
    Written.
  David Delene <delene@aero.und.edu> - 2016/12/26
    Added Cloning of ADTAE repository.
  David Delene <delene@aero.und.edu> - 2016/12/27
    Added Cloning of SODA repository.
  David Delene <delene@aero.und.edu> - 2017/01/12
    Added Cloning of EGADS, SAMAC, and UIOPS repository.
  David Delene <delene@aero.und.edu> - 2017/02/10
    Added nobinary and notesting options.
  David Delene <delene@aero.und.edu> - 2017/07/09
    Added information about Redhat install.
  David Delene <delene@aero.und.edu> - 2017/10/30
    Added AOSPY packae.
  David Delene <delene@aero.und.edu> - 2018/07/07
    Added SIMDATA probe simulation data set.
  David Delene <delene@aero.und.edu> - 2018/07/08
    Added pull (updating) of git repositories.

REFERENCES:
  Airborne Data Processing and Analysis (ADPAA)
    ADMINISTRATORS
      David Delene <delene@aero.und.edu> - Administrator
      Andrea Neumann
    CURRENT (2017/01/12) DEVELOPERS
      Cocos, Noah
      Ekness, Jamie
      Gapp, Nicholas
      Gupta, Siddhant
      Hibert, Kurt
      O'brien, Joseph
      Starzec, Mariusz
      Seyler, Scott
      Sorenson, Blake
      Wilson, Lance
   Current (2017/01/12) MEMBERS
      Bart, Nichole
      Butland, Alex
      Kruse, Christopher
      Mitchell, Robert
      Mulally, Daniel
      Sever, Gokhan
      Simelane, P.
      Uhlmann, Timm
    AVAILABILITY
      Repository - svn://svn.code.sf.net/p/adpaa
    COPYRIGHT
      GNU/GPL Version 3
    PLATFORM (Operatoring Systems Tested On)
      Redhat, Fedora, Ubuntu, Mint Linux (CPLOT/CPLOT2 - Windows)
    LANGUAGES
      IDL, Python 2, Perl, Bash, Csh, C, Fortran, Matlab, Scilab, Igor
    STATUS (December 27, 2016)
      3003 Commits, 12 Active Developers, 2 Administrator
    SCOPE
      Processes data from Science Engineering Associates (SEA) data
      acquisition systems, many instruments supported but does not
      process Optical Array Probe to produce size distributions.
      Does visualization, analysis and file conversion.


  Airborne Data Tesing and Evaluation (ADTAE)
    ADMINISTRATORS
      David Delene <delene@aero.und.edu> - Administrator
      Andrea Neumann
    CURRENT (2017/01/12) DEVELOPERS
      Cocos, Noah
      Ekness, Jamie
      Gapp, Nicholas
      Gupta, Siddhant
      Hibert, Kurt
      O'brien, Joseph
      Starzec, Mariusz
      Seyler, Scott
      Sorenson, Blake
      Wilson, Lance
    AVAILABILITY
      Repository - https://sourceforge.net/projects/adtae/
    COPYRIGHT
      GNU/GPL Version 3
    PLATFORM (Operatoring Systems Tested On)
      Redhat, Fedora, Ubuntu, Mint Linux and Windows
    LANGUAGES
      Python 2, but mostly just data files.
    STATUS (December 27, 2016)
      3 Commits, 12 Active Developers, 2 Administrator
    SCOPE
      The Airborne Data Testing and Evaluation (ADTAE)
      project develops open source resources to test and
      evaluate software used to process and analyse
      measurements from scientific instrument deployed on
      airborne platforms. Many of the resources are designed
      to work with the Airborne Data Processing and Analysis
      (ADPAA) software package (http://adpaa.sourceforge.net).

  Automated Climate Data Analysis and Management (AOSPY)
    AVAILABILITY
      PIP - pip install aospy
    LANGUAGES
      Works on Python 2.7, 3.4, 3.5, and 3.6.


  EUFAR General Airborne Data-processing Software (EGADS)
    DEVELOPERS
      Freer, Matt 
      Henry, Olivier
    AVAILABILITY
      Repository - https://github.com/eufarn7sp/egads-eufar
    COPYRIGHT
      New BSD License
    PLATFORM (Operatoring Systems Tested On)
      Linux, Mac and Windows
    LANGUAGES
      Python 2
    STATUS
      2 Active Developers
    SCOPE
      Toolbox and framework for processing Airborne Atmospheric Data.
      Includes meta-data and units. All algorithms are thoroughly documented
      in separate, referenceable PDF.


  Software for Airborne Measurements of Aerosol and Clouds (SAMAC)
    DEVELOPERS
      Gagne, Stephanie
      MacDonald, Landan
    AVAILABILITY
      Repository - https://github.com/StephGagne/SAMAC
    COPYRIGHT
      GNU/GPL Version 3
    PLATFORM (Operatoring Systems Tested On)
      Linux, Mac, Windows
    LANGUAGES
      Python 2.7 (Matplotlib, Scipy, Numpy, Basemap, H5py, Xlrd)  
    STATUS (December 27, 2016)
      +13,000+ Lines, 2 Developer
    SCOPE
      Analysis Package for Calculating, Displaying and Storing Segments from
      Processed Data Sets


  System for OAP Data Analsis (SIMDATA)
    DEVELOPERS
      Bansemer, Aaron
    AVAILABILITY
      FTP Site - ftp.ucar.edu/pub/mmm/bansemer/simulations
    COPYRIGHT
      None Provided
    PLATFORM (Operatoring Systems Tested On)
      Linux
    LANGUAGES
      NONE
    STATUS (July 9, 2018)
      Setup for July 2018 workshop.
    SCOPE
      Probe Simuluation data sets for DMT and SPEC probes.


  System for OAP Data Analsis (SODA)
    DEVELOPERS
      Bansemer, Aaron
    AVAILABILITY
      Repository - https://github.com/abansemer/soda
    COPYRIGHT
      BSD-3 License
        Free use, UCAR/NCAR retain copyright notice.  
    PLATFORM (Operatoring Systems Tested On)
      Linux and Windows, likely Macs
    LANGUAGES
      IDL (Bash Scripts)
    STATUS (December 27, 2016)
      +90,000 Lines, +1 Developer
    SCOPE
      GNU and script based analysis package for optical array
      probe data that uses shattering correction and other options
      to derive particle spectrum.


  University of Illinois OAP Processing Software (UIOPS)
    DEVELOPERS
      Current Developer: 
        Joseph A Finlong (finlon2@illinois.edu)
      Past Developer
        Wei Wu
    AVAILABILITY
      Curent Version
        Repository - https://github.com/joefinlon/UIOPS
      Past Version
        Repository - https://github.com/weiwu5/UIOPS
    COPYRIGHT
      GNU GPL V3
    PLATFORM (Operatoring Systems Tested On)
      Linux Windows, Mac (CGAL modern image processing)
    LANGUAGES
      Matlab (C++ Image processing, Python, Bash/Csh)
    STATUS (December 27, 2016)
      1 Developer
    SCOPE
      Analysis package for optical array probe data.


COPYRIGHT:
  2016, 2017, 2018 David Delene

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

# Import package with existing checking.
print "Importing Modules:"
import imp
print "  The imp module imported."

try:
    imp.find_module('git')
except ImportError, e:
    print "**  WARNING:  The python 'git' module does not exists."
    print "**    Please install (see suggestion below) and execute again."
    print "**    Redhat - sudo yum install GitPython"
    print "**    Fedora - sudo dnf install python2-GitPython"
    print "**    Ubuntu - sudo apt install python-git"
    pass
else:
    import git
    print "  The git module imported."

try:
    imp.find_module('os')
    import os
except ImportError, e:
    print "**  WARNING:  The python 'os' module does not exists."
    print "**    Please install (see suggestion below) and execute again."
    print "**    Redaht - sudo yum install python-libs"
    print "**    Fedora - sudo dnf install python-libs"
    pass
else:
    import os
    print "  The os module imported."

try:
    imp.find_module('pysvn')
    import pysvn
except ImportError, e:
    print "**  WARNING:  The python 'pysvn' module does not exists."
    print "**    Please install (see suggestion below) and execute again."
    print "**    Redhat - sudo yum install pysvn"
    print "**    Fedora - sudo dnf install pysvn"
    print "**    Ubuntu - sudo apt install python-svn"
    pass
else:
    import pysvn
    print "  The pysvn mdule imported."

try:
    imp.find_module('sys')
except ImportError, e:
    print "**  WARNInG:  The python 'sys' module does not exists."
    print "**    Please install (see suggestion below) and execute again."
    pass
else:
    import sys 
    print "  The sys mdule imported."

try:
    import tarfile
except ImportError, e:
    print "**  WARNING:  The python 'tarfile' module does not exists."
    print "**    Please install (see suggestion below) and execute again."
    print "**    Redhat - sudo yum install python-libs"
    print "**    Fedora - sudo dnf install python-libs"
    pass
else:
    import tarfile
    print "  The tarfile mdule imported."

try:
    import urllib2
except ImportError, e:
    print "**  WARNING:  The python 'urllib2' module does not exists."
    print "**    Please install (see suggestion below) and execute again."
    print "**     Redhat - sudo yum install python-libs"
    print "**     Fedora - sudo dnf install python-libs"
    pass
else:
    import urllib2
    print "  The urllib2 mdule imported."

try:
    import unittest2
except ImportError, e:
    print "**  WARNING:  The python 'unittest2' module does not exists."
    print "**    Please install (see suggestion below) and execute again."
    print "**      Fedora - sudo dnf install python2-unittest2"
    print "**      Ubuntu - sudo apt install python-unittest2"
    pass
else:
    import unittest2
    print "  The unittest2 mdule imported."

def help_message():
    print ('Syntax: CoPAS -h -s <ADPAA> <ADTAE> <EUFAR> <SAMAC> <SODA> <UIOPS> <nobinary> <notesting>')
    print ('  -h        Print help message.')
    print ('  -s        Include "source" code along with binary installation.')
    print ('  ADPAA     Process Airborne Data Processing and Analysis (ADPAA) package.')
    print ('  ADTAE     Process Airborne Data Testing and Evaluation (ADTAE) package.')
    print ('  EUFAR     Process EUFAR General Airborne Data-processing Software (EUFAR) package.')
    print ('  SAMAC     Software for Airborne Measurements of Aerosol and Clouds (SAMAC) package.')
    print ('  SIMDATA   Simulation probe data set.')
    print ('  SODA      System for OAP Data Analysis (SODA) package.')
    print ('  UIOPS     Process University of Illinois OAP Processing Software (UOIPS) package.')
    print ('  nobinary  Do not install binary packages.')
    print ('  notesting Do not test for support packages.')

# Define default options for package installation.
adpaa   = 0
adtae   = 0
aospy   = 0
binary  = 1
eufar   = 0
samac   = 0
simdata = 0
soda    = 0
source  = 0
testing = 1
uiops   = 0

# Check for help request.
for param in sys.argv:
    if param.startswith('-h'):
        help_message()
        exit()
    if param.startswith('-s'):
        source = 1
        # If no parameter options, install all packages.
        if (len(sys.argv) < 3):
            adpaa   = 1
            adtae   = 1
            eufar   = 1
            samac   = 1
            simdata = 1
            soda    = 1
            uiops   = 1
    else:
        # If no parameter options, install all packages.
        if (len(sys.argv) < 2):
            adpaa   = 1
            adtae   = 1
            eufar   = 1
            samac   = 1
            simdata = 1
            soda    = 1
            uiops   = 1

# Check for list of packages to install.
for param in sys.argv:
    if (param == 'ADPAA'):
        adpaa = 1
    if (param == 'adpaa'):
        adpaa = 1
    if (param == 'ADTAE'):
        adtae = 1
    if (param == 'adtae'):
        adtae = 1
    if (param == 'AOSPY'):
        aospy = 1
    if (param == 'aospy'):
        aospy = 1
    if (param == 'EUFAR'):
        eufar = 1
    if (param == 'eufar'):
        eufar = 1
    if (param == 'SAMAC'):
        samac = 1
    if (param == 'samac'):
        samac = 1
    if (param == 'SIMDATA'):
        simdata = 1
    if (param == 'simdata'):
        simdata = 1
    if (param == 'SODA'):
        soda = 1
    if (param == 'soda'):
        soda = 1
    if (param == 'UIOPS'):
        uiops = 1
    if (param == 'uiops'):
        uiops = 1

# Check for list of long name options.
for param in sys.argv:
    if (param == 'nobinary'):
        binary = 0
    if (param == 'notesting'):
        testing = 0

class Progress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print '{0}\r'.format(self._cur_line),

print "Install Packages:"




print "Finished install Packages:"

### Python for the Atmospheric and Oceanic Sciences (PyAOS). ###
if (aospy):
    try:
        import pip
    except ImportError, e:
        print "  The python 'pip' module does not exists."
        print "  Please install (see suggestion below) and execute again."
        pass
    else:
        import pip
        print "    Installing AOSPY package."
        print "    WARNING:  AOSPY installation requires sudo excutation of CoPAS, for example 'sudo ./CoPAS'."
        def install(package):
            pip.main(['install', package])
        if __name__ == '__main__':
            install('aospy')
        print "    Finsihed installing AOSPY package."


print "Cloning and Updating Repositories:"

### Airborne Data Processing and Analysis (ADPAA) software package. ###
if (adpaa):
    # Create directories.
    print "  Working on Airborne Data Processing and Analysis (ADPAA) package."
    if (binary):
        print "    Downloading binary version of ADPAA."
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
        print "    Downloading ADPAA Binary Version: %s Bytes: %s" % (file_name, file_size)

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
        print "   Extracting ADPAA distribution from compressed tar file."
        tar = tarfile.open('ADPAA.tar.gz', "r:gz")
        tar.extractall("..")
        tar.close()

        # Go back to base directory.
        os.chdir('../..')

    if (source):
        if not os.path.isdir("ADPAA"):
            print "    Cloning ADPAA source code from repository."
            if not os.path.isdir("ADPAA"):
                os.mkdir('ADPAA')
            os.chdir('ADPAA')
            client = pysvn.Client()
            client.checkout('svn://svn.code.sf.net/p/adpaa/code/trunk/src','src')
            os.chdir('..')
            print "    Finished cloning ADPAA source code from repository."
        else:
            # Updating existing ADPAA repository.
            print "    Updating existing ADPAA source code from repository."
            os.chdir('ADPAA')
            client = pysvn.Client()
            client.update('src')
            os.chdir('..')
            print "    Finished updating ADPAA source code from repository."
    if (testing):
        print "    Tesing for non-installed ADPAA support packages."
        try:
            import csv 
        except ImportError, e:
            print "    Required python 'csv' module is not installed."
            quit()
        try:
            import numpy 
        except ImportError, e:
            print "    Required python 'numpy' module is not installed."
            quit()
        try:
            import math
        except ImportError, e:
            print "    Required python 'math' module is not installed."
            quit()
        try:
            import sys
        except ImportError, e:
            print "    Required python 'sys' module is not installed."
            quit()
    print "    Finished tesing for non-installed ADPAA support packages."


### Airborne Data Testing and Evaluation (ADTAE) software package. ###
if (adtae):
    # Create main ADTAE directory.
    print "  Working on Airborne Data Testing and Evaluation (ADTAE) package."
    if not os.path.isdir("ADTAE"):
        os.mkdir('ADTAE')
        print "    Cloning ADTAE repository."
        repo = git.Repo.clone_from(
            'git://git.code.sf.net/p/adtae/code',
            'ADTAE',
            progress=Progress())
        print "    Finished cloning ADTAE repository."
    else:
        # Update the existing repository.
        print "    Updating ADTAE repository."
        repo = git.cmd.Git('ADTAE')
        repo.pull()
        print "    Finished with ADTAE."


### EUFAR General Airborne Data-processing Software (EUFAR). ###
if (eufar):
    # Create main EUFAR directory.
    print "  Working on EUFAR General Airborne Data-processing Software (EUFAR) package."
    if not os.path.isdir("EUFAR"):
        os.mkdir('EUFAR')
        print "    Cloning EUFAR repository."
        repo = git.Repo.clone_from(
            'https://github.com/eufarn7sp/egads-eufar',
            'EUFAR',
            progress=Progress())
    else:
        # Update the existing repository.
        print "    Updating EUFAR repository."
        repo = git.cmd.Git('EUFAR')
        repo.pull()
        print "    Finished with EUFAR."


### Software for Airborne Measurements of Aerosol and Clouds (SAMAC) ###
if (samac):
    # Create main SAMAC directory.
    print "  Software for Airborne Measurements of Aerosol and Clouds (SAMAC)."
    if not os.path.isdir("SAMAC"):
        print "    Cloning SAMAC repository."
        # Add in two space without return.
        sys.stdout.write('  ')
        sys.stdout.flush()
        repo = git.Repo.clone_from(
            'https://github.com/StephGagne/SAMAC',
            'SAMAC',
            progress=Progress())
        print "    Finished cloning SAMAC."
    else:
        # Update the existing repository.
        print "    Updating SAMAC repository."
        repo = git.cmd.Git('SAMAC')
        repo.pull()
        print "    Finished updating SAMAC repository."

### Simulation probe data (SIMDATA)  ###
if (simdata):
    # Get from ftp.ucar.edu/pub/mmm/bansemer/simulations/
    print "  Downloading simuation probe data set (SIMDATA)."
    print "  Finished downloading simuation probe data set (SIMDATA)."


### System for OAP Data Analysis (SODA) ###
if (soda):
    # Create main SODA directory.
    print "  System for OAP Data Analysis (SODA) package."
    if not os.path.isdir("SODA"):
        print "    Cloning SODA repository."
        repo = git.Repo.clone_from(
            'https://github.com/abansemer/soda2',
            'SODA',
            progress=Progress())
        print "    Finished cloning SODA repository."
    else:
        # Update the existing repository.
        print "    Updating SODA repository."
        repo = git.cmd.Git('SODA')
        repo.pull()
        print "    Finished with SODA."


### Process University of Illinois OAP Processing Software (UOIPS) package ###
if (uiops):
    # Create main UOIPS directory.
    print "  UIOPS  Process University of Illinois OAP Processing Software (UOIPS) package."
    if not os.path.isdir("UIOPS"):
        print "    Cloning UIOPS repository."
        repo = git.Repo.clone_from(
            'https://github.com/joefinlon/UIOPS',
            'UIOPS',
            progress=Progress())
        print "    Finished cloning UIPOS repository."
    else:
        # Update the existing repository.
        print "    Updating UIOPS repository."
        repo = git.cmd.Git('UIOPS')
        repo.pull()
        print "    Finished updating UIOPS."

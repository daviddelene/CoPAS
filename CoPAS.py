#!/usr/bin/env python3

"""
NAME:
  CoPAS.py <https://github.com/daviddelene/CoPAS>

PURPOSE:
  To facilitate the installation, setup, and integration of open source
  software and packages related to cloud physics, in-situ airborne data.

Download/Clone CoPAS Distribution
  cd $HOME
  git clone https://github.com/daviddelene/CoPAS.git

Setting up access to git on Linux.
  Github now requires additional authorization steps.
    Best to use git-credential-manager,
    https://github.com/GitCredentialManager/git-credential-manager/blob/main/README.md

  For linux OS, need "gpg" and "pass"; for example, sudo apt install git pass.
  Best to create a personal access token using gpg.

  Add export GCM_CREDENTIAL_STORE=gpg in ~/.bashrc

  create new GPG key pair
    - gpg --gen-key
  Initiaze pass with gpg key.
    - pass init <gpg-id>
  Everything should be automatic and the below should work.

Update the CoPAS.py File
  git commit CoPAS.py
  git push origin master

EXECUTION EXAMPLE:
  Get Help:
    CoPAS.py -h
  Test for Support Packages:
    CoPAS.py -t
  Install only the ADPAA package, binary and source pacakges:
    CoPAS.py -s ADPAA
  Install or update all package, onlye source versions:
    CoPAS.py -S

SYNTAX:
  CoPAS.py <-h|-s|-t> <ADPAA> <ADTAE> <DRILSDOWN> <EGADS> <SAMAC> <SIMDATA> <SODA> <UIOPS> <nobinary> <notesting>
  <-h>    - Print Syntax message.
  <-S>    - Install source package but no binary package.
  <-s>    - Install source package in addition to binary package.
  <-t>    - Test for necessary support packages.
  ADPAA     - Clone/pull the ADPAA SVN repository.
  ADTAE     - Clone/pull the ADTAE Git repository.
  DRILSDOWN - Clone/pull the DRILSDOWN repository.
  EGADS     - Install the EUFAR package.
  LROSE     - Install the Lidar Radar Open Software Environment (LROSE)
  SAMAC     - Install the SAMAC package.
  SIMDATA   - Download NCAR probe simulation data sets.
  SODA      - Install the SODA package.
  UIOPS     - Install the UIOPS package.
  <nobinary>  - Do not install binary packages.
  <notesting> - Do not test for support packages.

  No parameter on command line then Clone/pull all repositories.

DEVELOPERS:
  David Delene <delene@aero.und.edu>
  Nick Gapp (njgapp) <nicholas.james.gapp@ndus.edu>
  Joseph Finlon (joefinlon) <finlon2@illinois.edu>

NOTES:
  This script is the python 3 version, for python2 run CoPas_python2.py.

  If available, script installs a binary distribution of the package.
  If no binary distribution is available, then a copy of the package repository
  is installed.  If the -s option is used to install source, still need binary
  version of packages like ADPAA so don't have to compile and build the code.
  

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
  David Delene <delene@aero.und.edu> - 2018/07/08
    Added cloning of DRILSDOWN.
  David Delene <delene@aero.und.edu> - 2019/03/17
    Added -S and -t options.
    Added all_packages function.
    Updated print statements for both python 2 and 3.
    Replace urllib2 with urllib3 for python3 usage.
    Added cloning ADTAE using SOURCEFORGE_USER.
  David Delene <delene@aero.und.edu> - 2019/05/02
    Added LROSE/NetCDF
  David Delene <delene@aero.und.edu> - 2019/09/20
    Updated to using wget to get ADPAA.tar.gz.
    Added additional python module check.
    Changed to using python3.6 instead of just python3.
  David Delene <delene@aero.und.edu> - 2020/03/23
    Changed back to using python3 instead of python3.6, better on Aircraft.
  David Delene <delene@aero.und.edu> - 2021/02/08
    Changed to using pysvn instead of svn for python3, Getting source code now works.
  David Delene <delene@aero.und.edu> - 2022/08/27
    Changed to using import importlib.
    Added miepython.
    Added notes on GCM Credential.

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

  Drawing Rich Integrated Lat-lon-time Subsets from Dataservers Online into Working Notebooks (DRILSDOWN)
    ADMINISTRATORS
      Brian Mapes, mapes@miami.edu
    AVAILABILITY
      Repository - https://github.com/Unidata/drilsdown.git
    COPYRIGHT

    PLATFORM (Operatoring Systems Tested On)
      Fedora
    LANGUAGES
      Python
    STATUS (December 27, 2016)
      
    SCOPE
      The DRILSDOWN project facilitate access ro detailed
      visualizations (in the Integrated Data Viewer, IDV) of
      Cases of Interest (user-defined) within a Python-based geo-space x time
      statistical data analyses -- if the data for such visulaizations are
      available online in nice aggregated repositories.


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


  Lidar Radar Open Software Environment (LROSE)
    DEVELOPERS
      Mike Dixon
    AVAILABILITY
      Repository - https://github.com/NCAR/lrose-core
    COPYRIGHT
      BSD License - Copyright University Corporation for Atmospheric Research
    PLATFORM (Operatoring Systems Tested On)
      Linux, Mac, Windows (Linux Subsystem)
    LANGUAGES
      C++
    STATUS (May 2, 2019)
      Cor Relase 20190130
    SCOPE
      Mainly radar, Lidar data, but some satellite and model data.


  Miepython
    DEVELOPERS
      Scott Prahl
    AVAILABILITY
      Repository - https://github.com/scottprahl/miepython.git
    COPYRIGHT
      As-is
    PLATFORM (Operatoring Systems Tested On)
      Linux, Mac, Windows (Linux Subsystem)
    LANGUAGES
      Python
    STATUS (May 2, 2019)
      Documentation update April 2021
    SCOPE
      Mainly Mie scattering code.


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
  2016, 2017, 2018, 2019, 2020, 2021, 2022 David Delene

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

try:
    import sys
except ImportError:
    print ("    Required python 'sys' module is not installed.")
    quit()
 
# Define all default options values.
binary       = 1
source       = 0
testing      = 1
testing_only = 0

# Turn off all packages by default.
adpaa        = 0
adtae        = 0
aospy        = 0
drilsdown    = 0
eufar        = 0
lrose        = 0
miepython    = 0
samac        = 0
simdata      = 0
soda         = 0
uiops        = 0

# Routine to turn on/off all packages.
def all_packages(status):
    if status == 'On': 
        adpaa     = 1
        adtae     = 1
        drilsdown = 1
        eufar     = 1
        lrose     = 1
        miepython = 1
        samac     = 1
        simdata   = 1
        soda      = 1
        uiops     = 1
    else:
        adpaa     = 0
        adtae     = 0
        drilsdown = 0
        eufar     = 0
        lrose     = 0
        miepython = 0
        samac     = 0
        simdata   = 0
        soda      = 0
        uiops     = 0
    return (adpaa,adtae,drilsdown,eufar,lrose,miepython,samac,soda,uiops)

# Define the help/syntax message.
def help_message():
    print ("Syntax: CoPAS -h -s <ADPAA> <ADTAE> <EUFAR> <SAMAC> <LROSE> <MIEPYTHON> <SODA> <UIOPS> <nobinary> <notesting>")
    print ("  OPTIONS:")
    print ("    -h        Print help message.")
    print ("    -S        Include source code but no binary installation.")
    print ("    -s        Include source code in addition to binary installation.")
    print ("    -t        Only test for necessary support packages.")
    print ("  PACKAGES INCLUDED (Default - All Packages):")
    print ("    ADPAA     Process Airborne Data Processing and Analysis (ADPAA) package.")
    print ("    ADTAE     Process Airborne Data Testing and Evaluation (ADTAE) package.")
    print ("    EUFAR     Process EUFAR General Airborne Data-processing Software (EUFAR) package.")
    print ("    DRILSDOWN Process Drawing Rich Integrated Lat-lon-time Subsets from Dataservers Online into Working Notebooks (DRILSDOWN).")
    print ("    LROSE     Lidar Radar Open Software Environment (LROSE) package.")
    print ("    MIEPYTHON Mie scattering code written in python.")
    print ("    SAMAC     Software for Airborne Measurements of Aerosol and Clouds (SAMAC) package.")
    print ("    SIMDATA   Simulation probe data set.")
    print ("    SODA      System for OAP Data Analysis (SODA) package.")
    print ("    UIOPS     Process University of Illinois OAP Processing Software (UOIPS) package.")
    print ("  PREFERENCES:")
    print ("    nobinary  Do not install binary packages.")
    print ("    notesting Do not test for support packages.")
    print ("  ENIVIRONMENTAL VARIABLES:")
    print ("    SVN_USERNAME     Checks out svn repositories using the defiend username.")
    print ("    SOURCEFORGE_USER Checks out Sourceforge git repositories using defiend username.")

# Turn off all packages by default.
adpaa,adtae,drilsdown,eufar,lrose,miepython,samac,soda,uiops = all_packages('Off')

# Check for - command line options, for example -h.
for param in sys.argv:
    if param.startswith('-h'):
        help_message()
        exit()
    if param.startswith('-S'):
        source = 1
        binary = 0
        # If no parameter options, install all packages.
        if (len(sys.argv) < 3):
            adpaa,adtae,drilsdown,eufar,lrose,miepython,samac,soda,uiops = all_packages('On')
    if param.startswith('-s'):
        source = 1
        # If no parameter options, install all packages.
        if (len(sys.argv) < 3):
            adpaa,adtae,drilsdown,eufar,lrose,miepython,samac,soda,uiops = all_packages('On')
    else:
        # If no parameter options, install all packages.
        if (len(sys.argv) < 2):
            adpaa,adtae,drilsdown,eufar,lrose,miepython,samac,soda,uiops = all_packages('On')

    if param.startswith('-t'):
        testing_only  = 1

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
    if (param == 'DRILSDOWN'):
        drilsdown = 1
    if (param == 'drilsdown'):
        drilsdown = 1
    if (param == 'EUFAR'):
        eufar = 1
    if (param == 'eufar'):
        eufar = 1
    if (param == 'LROSE'):
        lrose = 1
    if (param == 'lrose'):
        lrose = 1
    if (param == 'MIEPYTHON'):
        miepython = 1
    if (param == 'miepython'):
        miepython = 1
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

# Import package with existing checking.
print ("Importing Modules:")
import importlib
print ("  The imp module imported.")

git_spec = importlib.util.find_spec("git")
if (git_spec != 'None'):
    import git
    print ("  The git module imported.")
else:
    print ("**  WARNING:  The python 'git' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**    Fedora - sudo dnf install python3-GitPython")
    print ("**    Ubuntu - sudo apt install python3-git")

numpy_spec = importlib.util.find_spec("git")
if (numpy_spec != 'None'):
    import numpy
else:
    print ("  The numpy module imported.")
    print ("**  WARNING:  The python 'numpy' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**    Redhat - sudo yum install python3-numpy")
    print ("**    Fedora - sudo dnf install python3-GitPython")
    print ("**    Ubuntu - sudo apt install python3-git")

os_spec = importlib.util.find_spec("os")
if (os_spec != 'None'):
    import os
    print ("  The os module imported.")
else:
    print ("**  WARNING:  The python 'os' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**    Redhat - sudo yum install python-libs")
    print ("**    Fedora - sudo dnf install python-libs")

### PIP required for AOSPY. ###
pip_spec = importlib.util.find_spec("pip")
if (pip_spec != 'None'):
    import pip
    print ("  The pip module imported.")
else:
    print ("  The python 'pip' module does not exists.")
    print ("  pip only required for AOSPY.")

requests_spec = importlib.util.find_spec("requests")
if (requests_spec != 'None'):
    import requests
    print ("  The requests module imported.")
else:
    print ("**  WARNING:  The python 'requests' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**    Redhat - sudo yum install python3-requests")
    print ("**    Fedora - sudo dnf install python3-requests")
    print ("**    Ubuntu - sudo apt install python3-requests")

pysvn_spec = importlib.util.find_spec("pysvn")
if (pysvn_spec != 'None'):
    import pysvn
    print ("  The pysvn module imported.")
else:
    print ("**  WARNING:  The python 'pysvn' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**    Redhat - sudo yum install python3-svn")
    print ("**    Fedora - sudo dnf install python3-svn")
    print ("**    Ubuntu - sudo apt install python3-svn")

shutil_spec = importlib.util.find_spec("shutil")
if (shutil_spec != 'None'):
    import shutil
    print ("  The shutil module imported.")
else:
    print ("**  WARNInG:  The python 'shutil' module does not exists.")

sys_spec = importlib.util.find_spec("sys")
if (sys_spec != 'None'):
    import sys 
    print ("  The sys module imported.")
else:
    print ("**  WARNInG:  The python 'sys' module does not exists.")

tarfile_spec = importlib.util.find_spec("tarfile")
if (tarfile_spec != 'None'):
    import tarfile
    print ("  The tarfile module imported.")
else:
    print ("**  WARNING:  The python 'tarfile' module does not exists.")

urllib3_spec = importlib.util.find_spec("urllib3")
if (urllib3_spec != 'None'):
    import urllib3
    print ("  The urllib3 module imported.")
else:
    print ("**  WARNING:  The python 'urllib3' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**     Redhat - sudo yum install python-urllibs3")
    print ("**     Fedora - sudo dnf install python3-urllibs3")

unittest2_spec = importlib.util.find_spec("unittest2")
if (unittest2_spec != 'None'):
    import unittest2
    print ("  The unittest2 module imported.")
else:
    print ("**  WARNING:  The python 'unittest2' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**      Redhat - sudo dnf install python3-unittest2")
    print ("**      Fedora - sudo dnf install python3-unittest2")
    print ("**      Ubuntu - sudo apt install python3-unittest2")

wget_spec = importlib.util.find_spec("wget")
if (wget_spec != 'None'):
    import wget
    print ("  The wget module imported.")
else:
    print ("**  WARNING:  The python 'wget' module does not exists.")
    print ("**    Please install (see suggestion below) and execute again.")
    print ("**      pip install wget")


# Exit if only want testing for support programs.
if testing_only:
    exit()

class Progress(git.remote.RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=''):
        print ('{0}\r'.format(self._cur_line))


print ("Cloning and Updating Repositories:")

### Airborne Data Processing and Analysis (ADPAA) software package. ###
if (adpaa):
    # Create directories.
    print ("  Working on Airborne Data Processing and Analysis (ADPAA) package.")
    if (binary):
        print ("    Downloading binary version of ADPAA.")
        if not os.path.isdir("ADPAA"):
            os.mkdir('ADPAA')
        os.chdir('ADPAA')
        if not os.path.isdir("binary_distributions"):
            os.mkdir('binary_distributions')
        os.chdir('binary_distributions')

        url = "http://sourceforge.net/projects/adpaa/files/ADPAA.tar.gz/download"
        file_name = "ADPAA.tar.gz"
        wget.download(url,file_name)

        # Extract distribution from compressed tar file.
        print ("   Extracting ADPAA distribution from compressed tar file.")
        tar = tarfile.open('ADPAA.tar.gz', "r:gz")
        tar.extractall("..")
        tar.close()

        # Go back to base directory.
        os.chdir('../..')

    if (source):
        if not os.path.isdir("ADPAA/src"):
            print ("    Cloning ADPAA source code from repository.")
            if not os.path.isdir("ADPAA"):
                os.mkdir('ADPAA')
            os.chdir('ADPAA')
            client = pysvn.Client()
            svn_username = os.environ.get('SVN_USERNAME')
            sourceforge_user = os.environ.get('SOURCEFORGE_USER')
            if svn_username is None:
                if sourceforge_user is None:
                    client.checkout('svn://svn.code.sf.net/p/adpaa/code/trunk/src','src')
                else:
                    client.checkout('svn+ssh://'+sourceforge_user+'@svn.code.sf.net/p/adpaa/code/trunk/src','src')
            else:
                client.checkout('svn+ssh://'+svn_username+'@svn.code.sf.net/p/adpaa/code/trunk/src','src')
            os.chdir('..')
            print ("    Finished cloning ADPAA source code from repository.")
        else:
            # Updating existing ADPAA repository.
            print ("    Updating existing ADPAA source code from repository.")
            os.chdir('ADPAA')
            client = pysvn.Client()
            client.update('src')
            os.chdir('..')
            print ("    Finished updating ADPAA source code from repository.")
    if (testing):
        print ("    Tesing for non-installed ADPAA support packages.")
        try:
            import csv 
        except ImportError:
            print ("    Required python 'csv' module is not installed.")
            quit()
        try:
            import numpy 
        except ImportError:
            print ("    Required python 'numpy' module is not installed.")
            quit()
        try:
            import math
        except ImportError:
            print ("    Required python 'math' module is not installed.")
            quit()
        try:
            import sys
        except ImportError:
            print ("    Required python 'sys' module is not installed.")
            quit()
    print ("    Finished tesing for non-installed ADPAA support packages.")


### Airborne Data Testing and Evaluation (ADTAE) software package. ###
if (adtae):
    # Create main ADTAE directory.
    print ("  Working on Airborne Data Testing and Evaluation (ADTAE) package.")
    if not os.path.isdir("ADTAE"):
        os.mkdir('ADTAE')
        print ("    Cloning ADTAE repository.")
        sourceforge_user = os.environ.get('SOURCEFORGE_USER')
        if sourceforge_user is None:
            repo = git.Repo.clone_from(
                'git://git.code.sf.net/p/adtae/code',
                'ADTAE',
                progress=Progress())
        else:
            repo = git.Repo.clone_from(
                'ssh://'+sourceforge_user+'@git.code.sf.net/p/adtae/code',
                'ADTAE')
        print ("    Finished cloning ADTAE repository.")
    else:
        # Update the existing repository.
        print ("    Updating ADTAE repository.")
        repo = git.cmd.Git('ADTAE')
        repo.pull()
        print ("    Finished with ADTAE.")

if (aospy):
    print ("    Installing AOSPY package.")
    print ("    WARNING:  AOSPY installation requires sudo excutation of CoPAS, for example 'sudo ./CoPAS'.")
    def install(package):
        pip.main(['install', package])
    if __name__ == '__main__':
        install('aospy')
    print ("    Finsihed installing AOSPY package.")


### Drawing Rich Integrated Lat-lon-time Subsets from Dataservers Online into Working Notebooks package. ###
if (drilsdown):
    # Create main DRILSDOWN directory.
    print ("  Working on DRILSDOWN package.")
    if not os.path.isdir("DRILSDOWN"):
        os.mkdir('DRILSDOWN')
        print ("    Cloning DRILSDOWN repository.")
        repo = git.Repo.clone_from(
            'git://github.com/Unidata/drilsdown.git',
            'DRILSDOWN',
            progress=Progress())
        print ("    Finished cloning DRILSDOWN repository.")
    else:
        # Update the existing repository.
        print ("    Updating GRILSDOWN repository.")
        repo = git.cmd.Git('DRILSDOWN')
        repo.pull()
        print ("    Finished with DRILSDOWN.")


### EUFAR General Airborne Data-processing Software (EUFAR). ###
if (eufar):
    # Create main EUFAR directory.
    print ("  Working on EUFAR General Airborne Data-processing Software (EUFAR) package.")
    if not os.path.isdir("EUFAR"):
        os.mkdir('EUFAR')
        print ("    Cloning EUFAR repository.")
        repo = git.Repo.clone_from(
            'https://github.com/eufarn7sp/egads-eufar',
            'EUFAR',
            progress=Progress())
    else:
        # Update the existing repository.
        print ("    Updating EUFAR repository.")
        repo = git.cmd.Git('EUFAR')
        repo.pull()
        print ("    Finished with EUFAR.")


### LROSE Lidar Radar Open Software Environment (LROSE). ###
if (lrose):
    # Create main LROSE directory.
    print ("  Working on the LROSE Lidar Radar Open Software Environment (LROSE).")
    if not os.path.isdir("LROSE"):
        os.mkdir('LROSE')
        print ("    Cloning LROSE repository.")
        repo = git.Repo.clone_from(
            'https://github.com/NCAR/lrose-core',
            'LROSE',
            progress=Progress())
    else:
        # Update the existing repository.
        print ("    Updating LROSE repository.")
        repo = git.cmd.Git('LROSE')
        repo.pull()
        print ("    Finished with LROSE.")

    # Create main NetCDF directory.
    print ("  Working on the NetCDF support for (LROSE).")
    if not os.path.isdir("NetCDF"):
        os.mkdir('NetCDF')
        print ("    Cloning NetCDF repository.")
        repo = git.Repo.clone_from(
            'https://github.com/NCAR/lrose-netcdf',
            'NetCDF',
            progress=Progress())
    else:
        # Update the existing repository.
        print ("    Updating NetCDF repository.")
        repo = git.cmd.Git('NetCDF')
        repo.pull()
        print ("    Finished with NetCDF.")

if (miepython):
    # Create main MiePython directory.
    print ("  Working on miepython).")
    if not os.path.isdir("miepython"):
        print ("    Cloning miepython repository.")
        repo = git.Repo.clone_from(
            'https://github.com/scottprahl/miepython.git',
            'miepython',
            progress=Progress())
    else:
        # Update the existing repository.
        print ("    Updating miepython repository.")
        repo = git.cmd.Git('miepython')
        repo.pull()
        print ("    Finished with miepython.")

### Software for Airborne Measurements of Aerosol and Clouds (SAMAC) ###
if (samac):
    # Create main SAMAC directory.
    print ("  Software for Airborne Measurements of Aerosol and Clouds (SAMAC).")
    if not os.path.isdir("SAMAC"):
        print ("    Cloning SAMAC repository.")
        # Add in two space without return.
        sys.stdout.write('  ')
        sys.stdout.flush()
        repo = git.Repo.clone_from(
            'https://github.com/StephGagne/SAMAC',
            'SAMAC',
            progress=Progress())
        print ("    Finished cloning SAMAC.")
    else:
        # Update the existing repository.
        print ("    Updating SAMAC repository.")
        repo = git.cmd.Git('SAMAC')
        repo.pull()
        print ("    Finished updating SAMAC repository.")

### Simulation probe data (SIMDATA)  ###
if (simdata):
    # Get from ftp.ucar.edu/pub/mmm/bansemer/simulations/
    print ("  Downloading simuation probe data set.")
    print ("  Finished downloading simuation probe data set.")


### System for OAP Data Analysis (SODA) ###
if (soda):
    # Create main SODA directory.
    print ("  System for OAP Data Analysis (SODA) package.")
    if not os.path.isdir("SODA"):
        print ("    Cloning SODA repository.")
        repo = git.Repo.clone_from(
            'https://github.com/abansemer/soda2',
            'SODA',
            progress=Progress())
        print ("    Finished cloning SODA repository.")
    else:
        # Update the existing repository.
        print ("    Updating SODA repository.")
        repo = git.cmd.Git('SODA')
        repo.pull()
        print ("    Finished with SODA.")


### Process University of Illinois OAP Processing Software (UOIPS) package ###
if (uiops):
    # Create main UOIPS directory.
    print ("  UIOPS  Process University of Illinois OAP Processing Software (UOIPS) package.")
    if not os.path.isdir("UIOPS"):
        print ("    Cloning UIOPS repository.")
        repo = git.Repo.clone_from(
            'https://github.com/joefinlon/UIOPS',
            'UIOPS',
            progress=Progress())
        print ("    Finished cloning UIPOS repository.")
    else:
        # Update the existing repository.
        print ("    Updating UIOPS repository.")
        repo = git.cmd.Git('UIOPS')
        repo.pull()
        print ("    Finished updating UIOPS.")

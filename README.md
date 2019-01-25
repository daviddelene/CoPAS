# CoPAS
Community Packages for Airborne Science (CoPAS) is a Github project designed to
facilitate the installation, setup, and integration of open source software and
packages related to cloud physics, in-situ airborne data.

Clone CoPAS Distribution
---------------------------------
- cd ${HOME}
- git clone https://github.com/daviddelene/CoPAS.git

Download Packages:
------------------
- cd ${HOME}/CoPAS
- ./CoPAS.py

Update (Submitting Files) Repository:
---------------
- git commit file
- git push origin master

Projects Supported:
-------------------
- Airborne Data Processing and Analysis (ADPAA)
    https://sourceforge.net/projects/adpaa/
- Airborne Data Testing and Evaluation (ADTAE)
    https://sourceforge.net/projects/adtae/
- EUFAR General Airborne Data-processing Software (EGADS)
    https://github.com/eufarn7sp/egads-eufar
- System for OAP Data Analsis (SODA)
    https://github.com/abansemer/soda
- University of Illinois OAP Processing Software (UIOPS)
    https://github.com/joefinlon/UIOPS

Setup ADPAA via CoPAS:
----------------------
- Website to Download or Clone CoPAS:
https://github.com/daviddelene/CoPAS.git
- Clone Repository:
git clone
https://github.com/daviddelene/CoPAS.git
- Setup Aircraft Software:
cd ~/CoPAS && ~/CoPAS/CoPAS.py
- Setup ADPAA on Linux:
~/CoPAS/ADPAA/bin/adpaa setup binary
- Setup Data Set:
cp –r ~/CoPAS/ADTAE/TestData/FlightData/20150728_153107 ~/20150728_153107-SandBox


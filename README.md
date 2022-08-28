# CoPAS
Community Packages for Airborne Science (CoPAS) is a Github project designed to
facilitate the installation, setup, and integration of open source software and
packages related to cloud physics, in-situ airborne data.

Clone CoPAS Distribution
---------------------------------
- cd ${HOME}
- git clone https://github.com/daviddelene/CoPAS.git

Setting up Python3.6 for CoPAS Distribution
---------------------------------
- cd ${HOME}/CoPAS 
- python3.6 -m venv env
- source env/bin/activate
- pip3.6 install -r ./requirements_CoPAS.txt

Execulting CoPAS to Download Packages:
------------------
- cd ${HOME}/CoPAS
- ./CoPAS.py

Update Python Requirements:
---------------
pip3.6 freeze > requirements_CoPAS.txt

Update (Submitting Files) Repository:
Notes:
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


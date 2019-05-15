##no obnoxious pycache files, let's build at run time
export PYTHONDONTWRITEBYTECODE=1;

##look for all of the code inside of the lib folder to make import easier
export PYTHONPATH=lib;

##call the master
python3 master.py;
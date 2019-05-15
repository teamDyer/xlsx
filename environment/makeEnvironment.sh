##path to the python you want to use (use 3.x)
python='/usr/bin/python3';

##make sure virtual environment is available
python3 -m pip install virtualenv;

##name of virtual environment
name='environment';

##create the virtual environment
virtualenv $name;

##activate the virtual environment
source $name/bin/activate;

##install yolk so you can see what packages were installed
pip install yolk3k;

##deactivate the virtual environment
deactivate;

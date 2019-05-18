##all libraries to pip install
libs=()
libs+=('yolk3k')  ##see installed packages
libs+=('pyopenxl') ##excel

##path to the python you want to use (use 3.x)
python="Python3.7_windows/python";

##upgrade to newest pip just in case
$python -m pip install --upgrade pip;

##make sure virtual environment is available
$python -m pip install virtualenv;

exit 1;

##name of virtual environment
name='glibc_2.23';

##create the virtual environment
virtualenv $name;

##activate the virtual environment
source $name/bin/activate;

##install all libs
for lib in ${libs[@]}; do
	pip install $lib;
done;

##deactivate the virtual environment
deactivate;

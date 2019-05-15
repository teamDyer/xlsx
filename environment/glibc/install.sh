####Sometimes whenever going between machines it is possible that a different version of GLIBC needs to be used.
####By grabbing and putting in the environment it should work reardless of machine. 

##glibc-2.25 takes ~3 minutes

##note here you can change the version
version="glibc-2.25"

##globals
code="$version""_source";
separator='-----\n-----\n-----\n';

##if the last command failed, then echo the phase and exit
status(){
	if [[ "$?" != "0" ]]; then 
		echo -ne "$separator Exiting early, experienced error during phase: '$1'" && exit 1;
	fi;
}

##save this for later use
base=`pwd`;

##gawk is required for the build
sudo apt-get install gawk;
status "Installing gawk";

##get the tar file
wget http://ftp.gnu.org/gnu/glibc/$version.tar.gz;
status "Getting tar file for '$version'";

##extract the contents
tar -zvxf $version.tar.gz && rm -rf $version.tar.gz;
status "Extracting the tar file contents";

##change the name of the extracted contents then make a directory for the libs with the previous name
mv $version $code && mkdir $version;
status "Changing the name of the source code and creating directory for built libs";

##create a directory for building in
cd $code && mkdir build && cd build;
status "Creating the build directory";

##configure the build and use the glibc directory as the base
../configure --prefix=$base/$version;
status "Configuring the build";

##make the library
make -j4;
status "Making the library";

##install the library
sudo make install;
status "Installing the library";

##remove the source code
cd $base;
rm -rf $code;
status "Removing the source code";

##SUCCESS
echo -ne "$separator SUCCESS!! Find the glibc binaries in '$base'"

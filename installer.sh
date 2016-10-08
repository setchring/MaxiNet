#!/bin/bash

echo "MaxiNet 1.0 installer"
echo ""
echo "This program installs MaxiNet 1.0 and all requirements to the home directory of your user"

if [ "$1" == "--help" ] || [ "$1" == "-h" ]
then
    echo ""
    echo "Invoke without any parameter to interactively install MaxiNet and its dependencies."
    echo "Use the -a parameter for complete and unguided installation."
    exit 0
fi


if [ "$1" == "-a" ]
then
    mininet="y"
    metis="y"
    pyro="y"
else
    
    read -n1 -r -p "Do you want to install Containernet? ([y]/n)" containernet
    
    if [ "$containernet" == "" ] || [ "$containernet" == "y" ] || [ "$containernet" == "Y" ]
    then
        containernet="y"
        echo ""
        echo "You choose to install Containernet. Warning: Use this option only on a clean OS without Mininet or Containernet!"
	mininet="n"
    else
        containernet="n"
	
	echo ""
        read -n1 -r -p "Do you want to install Mininet 2.2.1rc1? ([y]/n)" mininet

        if [ "$mininet" == "" ] || [ "$mininet" == "y" ] || [ "$mininet" == "Y" ]
        then
            mininet="y"
            echo ""
            echo "You choose to install Mininet. Warning: This will automatically remove existing directories ~/mininet, ~/loxigen, and ~/openflow"
        else
            mininet="n"
        fi
    fi
    echo ""

    read -n1 -r -p "Do you want to install Metis 5.1? ([y]/n)" metis

    if [ "$metis" == "" ] || [ "$metis" == "y" ] || [ "$metis" == "Y" ]
    then
        metis="y"
    else
        metis="n"
    fi
    echo ""

    read -n1 -r -p "Do you want to install Pyro 4.45? ([y]/n)" pyro

    if [ "$pyro" == "" ] || [ "$pyro" == "y" ] || [ "$pyro" == "Y" ]
    then
        pyro="y"
    else
        pyro="n"
    fi
    echo ""


    echo "----------------"
    echo ""
    echo "MaxiNet installer will now install: "
    if [ "$containernet" == "y" ]; then echo " -Containernet"; fi
    if [ "$mininet" == "y" ]; then echo " -Mininet 2.2.1rc1"; fi
    if [ "$metis" == "y" ]; then echo " -Metis 5.1"; fi
    if [ "$pyro" == "y" ]; then echo " -Pyro 4.45"; fi
    echo " -MaxiNet 1.0"
    echo ""

    read -n1 -r -p "Is this OK? Press ANY key to continue or CTRL+C to abort." abort

fi

echo "installing required dependencies."

sudo apt-get update
sudo apt-get install -y git autoconf screen cmake build-essential sysstat python-matplotlib uuid-runtime ansible

if [ "$containernet" == "y" ]
then
        sudo echo "localhost ansible_connection=local" >> /etc/ansible/hosts
        git clone https://github.com/setchring/containernet.git
	cd containernet/ansible
	sudo ansible-playbook install.yml
fi

if [ "$mininet" == "y" ]
then
	cd ~
	sudo rm -rf openflow &> /dev/null
	sudo rm -rf loxigen &> /dev/null
	sudo rm -rf pox &> /dev/null
	sudo rm -rf oftest &> /dev/null
	sudo rm -rf oflops &> /dev/null
	sudo rm -rf ryu &> /dev/null
	sudo rm -rf mininet &> /dev/null

	git clone git://github.com/mininet/mininet
	cd mininet
	git checkout -b 2.2.1rc1 2.2.1rc1
	cd util/
	./install.sh

	# the mininet installer sometimes crashes with a zipimport.ZipImportError.
	# In that case, we retry installation.
	if [ "$?" != "0" ]
	then
	    ./install.sh
	fi


fi

if [ "$metis" == "y" ]
then
	cd ~
	wget http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/metis-5.1.0.tar.gz
	tar -xzf metis-5.1.0.tar.gz
	rm metis-5.1.0.tar.gz
	cd metis-5.1.0
	make config
	make
	sudo make install
	cd ~
	rm -rf metis-5.1.0
fi

if [ "$pyro" == "y" ]
then
	sudo apt-get install -y python-pip
	sudo pip install -y Pyro4
fi


cd ~
sudo rm -rf MaxiNet &> /dev/null
git clone https://github.com/setchring/MaxiNet.git
cd MaxiNet
git checkout v1.0
sudo make install



sudo python3 -m pip install django
wget https://sourceforge.net/projects/pyusb/files/PyUSB%201.0/1.0.0/pyusb-1.0.0.tar.gz
tar xvf pyusb-1.0.0.tar.gz
rm -rf pyusb-1.0.0.tar.gz
cd pyusb-1.0.0
sudo python3 setup.py install
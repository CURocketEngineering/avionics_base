# What has/needs to be installed for a new headless pi

wd=$(pwd)
alias ins='sudo apt install' # ease

sudo apt-get update
ins python3-pip --fix-missing # pip!

# USB Relay
ins libhidapi-dev

# XBee
pip3 install digi-xbee
pip3 install psutil


apt update
apt upgrade
apt install wget -y
cd ~
wget https://github.com/digitalocean/doctl/releases/download/v1.101.0/doctl-1.101.0-linux-amd64.tar.gz
tar xf ~/doctl-1.101.0-linux-amd64.tar.gz
mv ~/doctl /usr/local/bin

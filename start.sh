echo -e "\e[1;31m"
figlet Zip Password cracker
echo -e "\e[1;34m Created By \e[1;32m"
toilet -f mono12 -F border shadow0null

echo " "
apt update
apt upgrade
pkg install python
pkg install python3
pkg install git
git clone https://github.com/shadow0null/Zip_password_cracker.git
pip install zipfile
pip install os
pip install colored
cd Zip_password_cracker
python3 Cracker.py
                 
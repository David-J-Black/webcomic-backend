!#/bin/bash

#setup script location
script_directory=$(dirname "$0")
working_directory="$( cd .. )"
cd "$script_directory/.."

echo " | Installing Python | "

sudo apt install -y python3 python3-pip python3.10-venv

python3 -m venv venv
source venv/bin/activate

# Check if the previous command succeeded
if [ $? -ne 0 ]; then
    echo Failed to activate venv
    exit 1
fi

pip3 install -r requirements.txt
deactivate
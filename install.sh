#!/bin/bash

export OS="$(uname)"
echo "$OS"
if [[ "$OS" == "Linux" ]]
then
GRAW_LINUX=1
elif [[ "$OS" == "Darwin" ]]
then
GRAW_LINUX=0
else
echo "Can only use install.sh on Unixoids"
exit
fi

mkdir /bin/graw
cp ./graw.py /bin/graw/graw
cd /bin/graw
echo "$PATH:/bin/graw" >> ~/.bashrc
exit

#! /bin/sh

echo ""
echo "updating your system :"
echo "----------------------"
echo ""

v=sudo apt-get update && sudo apt-get dist-upgrade

echo ""
echo "installing dependencies :"
echo "-------------------------"
echo ""

sudo pip install pynput
$v

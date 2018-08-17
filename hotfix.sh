#!/bin/sh
git clone https://github.com/Kajak2137/MabelBot2.0 -b alt ./tmp
rm ./tmp/hotfix.sh
mv ./tmp/* .
rm -rf ./tmp
python3.6 MabelBot.py

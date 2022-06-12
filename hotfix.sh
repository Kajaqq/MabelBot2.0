#!/bin/sh
git clone https://github.com/Kajaqq/MabelBot2.0  ./tmp
rm ./tmp/hotfix.sh
mv ./tmp/* .
rm -rf ./tmp
python MabelBot.py

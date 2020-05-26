#!/bin/bash

VENV="./env/"
DATA="./COVID-19-TweetIDs/"
ACTIVATE="./env/bin/activate"

if [ ! -d "$VENV" ]; then
    echo "venv for python3 not found, making a new one"
    echo ""
    python3 -m pip install --user virtualenv
    python3 -m venv env

elif [ ! -f "$ACTIVATE" ]
then

    rm -r "./env"
    python3 -m pip install --user virtualenv
    python3 -m venv env

else 
    echo "venv already created"
fi

echo "sourcing $ACTIVATE"
source "$ACTIVATE"
which python

echo ""
echo "installing dependancy"
echo ""

pip install --upgrade pip
python -m pip install -r requirements.txt


chmod 755 ./setup_only.sh

VENV="./env/"
DATA="./COVID-19-TweetIDs/"

if [ "$1" = "hydrated" ]
then

    echo "hydrated mode"

    if [ ! -d "$DATA" ]
    then

    echo "cloning hydrated data from github"
    git clone https://github.com/echen102/COVID-19-TweetIDs.git
    
    else
        echo "dehydrated data found, try to update"
        git -C COVID-19-TweetIDs/ pull
    fi

    . ./setup_only.sh
    python my_hydrated.py

elif [ "$1" = "realtime" ]
then

    echo "realtime mode"
    . ./setup_only.sh
    python stream_AU.py

else

    if [ ! "$1" = "" ]
    then
        echo "unknown parameters"
        exit 1
    fi

    echo "no parameter provided, only setup environment"
    . ./setup_only.sh
fi

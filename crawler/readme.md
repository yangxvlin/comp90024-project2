You should create your own config.json with your keys and search word.

it should looks like this

{"account":{"consumer_key": your_key,
           "consumer_secret": your_secret,
           "access_token": your_token,
           "access_token_secret": your_token},
"search_words":[
    "corona", 
    "outbreak", 
    "covid-19", 
    "quarantine", 
    "virus", 
    "morrison", 
    "scott morrison", 
    "scomor"]
}

Once done, run the following command to **ONLY** setup the environment

```
./setup
```

if you want to retrieve real time twitter, use

```
./setup realtime
```

if you want to keep hydrating the twitter, use
```
./setup hydrated
```

provide anything else as an argument will cause the script abort.

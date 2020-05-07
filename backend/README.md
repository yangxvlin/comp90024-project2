# Backend

## How to contact
### API
[Link](https://app.swaggerhub.com/apis-docs/yangxvlin/backend/1.0.0)

### cmd
#### scenario 1
```curl -X GET 127.0.0.1:5000/scenario1?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney&weekday=1,2,3&daytime_start=0&daytime_end=24&age_group=0,1,2,17```
#### scenario 2
```curl -X GET 127.0.0.1:5000/scenario2?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney&age_group=0,1,2,17```
#### scenario 3
```curl -X GET 127.0.0.1:5000/scenario3?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney```
#### scenario 4
```curl -X GET 127.0.0.1:5000/scenario4?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney```
#### scenario 5
```curl -X GET 127.0.0.1:5000/scenario5?lga=Greater Adelaide,Greater Melbourne,Greater Brisbane,Greater Sydney```

### curl to js
https://kigiri.github.io/fetch/

## How to run
### Ubuntu
1. ```cd backend```
2. ```python3 -m venv venv```
3. ```. venv/bin/activate```
4. ```pip install -r requirements.txt```
5. ```pip install flask```
6. ```flask run```

## generate requirements.txt
1. ```python3 -m venv venv```
2. ```pip freeze | grep -v "pkg-resources" > requirements.txt``` [Note](https://stackoverflow.com/a/40167445)

## Shell Scripts
- ```./run_flask_debug_mode.sh```  
  - To start flask app, it would enable the debug mode, it would ask for port
- ```./test_api_get.sh```
  - In this script, I send http GET request with fake json data to the flask backend. This script would ask for 2 inputs. 1. host url for the flask app, e.g. http://localhost/8000. 2. a id(int), only 1 and 2 are in memory, other id would be 404 error

## docker
1. ```docker build -t backend:latest```

## directory structure
```
.
念岸岸 ...
念岸岸 docs                    # Documentation files (alternatively `doc`)
岫   念岸岸 TOC.md              # Table of contents
岫   念岸岸 faq.md              # Frequently asked questions
岫   念岸岸 misc.md             # Miscellaneous information
岫   念岸岸 usage.md            # Getting started guide
岫   弩岸岸 ...                 # etc.
弩岸岸 ...
```

## Note
- [flask-ReSTful documentation](https://flask-restful.readthedocs.io/en/latest/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [Docker + Flask | A Simple Tutorial](https://medium.com/@doedotdev/docker-flask-a-simple-tutorial-bbcb2f4110b5)

### ReSTful API
achieved by flask-resutful and flask-httpauth

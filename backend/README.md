# Backend

## How to contact
### API
[Link](https://app.swaggerhub.com/apis-docs/yangxvlin/backend/1.0.0)

### cmd
#### scenario 1
```
<ip>/scenario1?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&weekday=1,2,3&daytime_start=0&daytime_end=24&age_group=0,1,2,17

:parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
:parameter: weekday: 0-6 monday to sunday
:parameter: daytime_start 0-24
:parameter: daytime_end 0-24
:parameter: age_group 0-17
```
#### scenario 2
see ```/templates```
1. ```<ip>/scenario2_mel```
2. ```<ip>/scenario2_ald```
3. ```<ip>/scenario2_brisbane```
4. ```<ip>/scenario2_syd```

#### scenario 3
```
<ip>/scenario3?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&year_start=2020&month_start=2&year_end=2020&month_end=5
        
:parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
:parameter: year_start: 2020
:parameter: month_start: 1-12
:parameter: year_end: 2020
:parameter: month_end: 1-12
```
#### scenario 4
```
<ip>/scenario4?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney&income=0,3,7,8,9,12,13,15&year_start=2020&month_start=2&day_start=1&year_end=2020&month_end=5&day_end=10
        
:parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
:parameter: income: 0-15
:parameter: year_start: 2020
:parameter: month_start: 1-12
:parameter: day_start: 1-31
:parameter: year_end: 2020
:parameter: month_end: 1-12
:parameter: day_end: 1-31
```
#### scenario 5
```
<ip>/scenario5?lga=Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney

:parameter: lga: [Greater_Adelaide,Greater_Melbourne,Greater_Brisbane,Greater_Sydney]
```

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

### windows
1. ```python backend.py -host 127.0.0.1 -port 5000```

## generate requirements.txt
1. ```python3 -m venv venv```
2. ```pip freeze | grep -v "pkg-resources" > requirements.txt``` [Note](https://stackoverflow.com/a/40167445)

## docker
1. ```docker-compose up -d``` to run the code immediately.
2. ```docker-compose down``` to shutdown the backend
3.  to modify the port number, see docker-compose.yml

## directory structure
```
| /AURIN
      - AURIN data
  /COVID-19
      - COVID-19 related data
  /templates
      - teample html
  /scenarios.py
      - major falsk ReSTful API get request
  /view_data.py
      - backend get data from database
```

## Note
- [flask-ReSTful documentation](https://flask-restful.readthedocs.io/en/latest/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [Docker + Flask | A Simple Tutorial](https://medium.com/@doedotdev/docker-flask-a-simple-tutorial-bbcb2f4110b5)

### ReSTful API
achieved by flask-resutful and flask-httpauth

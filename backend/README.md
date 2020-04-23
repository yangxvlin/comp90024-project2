# Backend

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


## docker
1. ```docker build -t backend:latest```

## directory structure
```
.
©À©¤©¤ ...
©À©¤©¤ docs                    # Documentation files (alternatively `doc`)
©¦   ©À©¤©¤ TOC.md              # Table of contents
©¦   ©À©¤©¤ faq.md              # Frequently asked questions
©¦   ©À©¤©¤ misc.md             # Miscellaneous information
©¦   ©À©¤©¤ usage.md            # Getting started guide
©¦   ©¸©¤©¤ ...                 # etc.
©¸©¤©¤ ...
```

## Note
- [flask-ReSTful documentation](https://flask-restful.readthedocs.io/en/latest/)
- [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
- [Docker + Flask | A Simple Tutorial](https://medium.com/@doedotdev/docker-flask-a-simple-tutorial-bbcb2f4110b5)

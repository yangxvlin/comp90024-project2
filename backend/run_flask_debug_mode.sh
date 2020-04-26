read -p "Enter server port: " word
FLASK_APP=backend.py FLASK_ENV=development flask run --port $word
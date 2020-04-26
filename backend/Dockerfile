# Dockerfile - this is a comment. Delete me if you want.
FROM rackspacedot/python37:latest
#ENV PORT "5000"
COPY . /
#RUN source /venv/bin/activate
RUN pip install -r requirements.txt
#RUN ./run_flask_debug_mode.sh
ENTRYPOINT ["python3"]
CMD ["backend.py"]

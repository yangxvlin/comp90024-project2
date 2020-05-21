# Dockerfile - this is a comment. Delete me if you want.
FROM rackspacedot/python37:latest
#ENV PORT "5000"
COPY . /
#RUN source /venv/bin/activate
RUN pip install -r requirements.txt
#RUN ./run_flask_debug_mode.sh
ENTRYPOINT ["python3"]
CMD ["backend.py"]


 http_proxy: http://wwwproxy.unimelb.edu.au:8000/
      https_proxy: http://wwwproxy.unimelb.edu.au:8000/
      HTTP_PROXY: http://wwwproxy.unimelb.edu.au:8000/
      HTTPS_PROXY: http://wwwproxy.unimelb.edu.au:8000/
      no_proxy: localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

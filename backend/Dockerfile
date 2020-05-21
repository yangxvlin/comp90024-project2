# Dockerfile - this is a comment. Delete me if you want.
FROM ubuntu:18.04 AS base

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

# update tools and dependency
RUN apt-get update \
    && apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion

# install anaconda
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O ~/anaconda.sh \
    && /bin/bash ~/anaconda.sh -b -p /opt/conda \
    && rm ~/anaconda.sh \
    && ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh \
    && echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc \
    && echo "conda activate base" >> ~/.bashrc

WORKDIR /usr/AURIN

COPY AURIN .

WORKDIR /usr/backend

#ENV PORT "5000"
COPY . .

RUN pip install -r requirements.txt

# install dependency to conda
RUN conda install -c plotly plotly-orca==1.2.1 psutil requests


FROM base

ENV flask_port 5000
ENV flask_host 0.0.0.0

EXPOSE $flask_port
#RUN ./run_flask_debug_mode.sh
ENTRYPOINT ["sh", "-c"]
CMD ["python backend.py -host $flask_host -port $flask_port"]

FROM python:3

WORKDIR /usr/src/app

RUN pip3 install virtualenv flask
RUN pip3 install -U flask-cors
RUN pip install pyreadline bpython

#CMD [ "bpython"]
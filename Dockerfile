FROM python:3.9

ENV FLASK_APP=modules

COPY requirements.txt /opt

RUN python3 -m pip install -r /opt/requirements.txt

COPY modules /opt/modules

WORKDIR /opt

CMD flask run --host 0.0.0.0 -p $PORT

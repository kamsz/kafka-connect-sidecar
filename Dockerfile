FROM python:3.7.1-alpine3.8

RUN pip install requests

COPY main.py /main.py

CMD [ "python", "/main.py" ]

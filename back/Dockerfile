FROM python:3.7
RUN mkdir /back
WORKDIR /back
COPY requirements.txt /back/
RUN pip install -r requirements.txt
COPY . /back/
ENTRYPOINT ["sh", "./entrypoint.sh"]

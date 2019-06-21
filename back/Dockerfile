FROM python:3.7
RUN mkdir /back
WORKDIR /back
COPY requirements.txt /back/
RUN pip install -r requirements.txt
COPY . /back/
CMD ["sh", "./initdb.sh"]
ENTRYPOINT ["gunicorn", "-c", "gunicorn.conf.py", "gist.app:app"]

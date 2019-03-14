FROM python:3.4-alpine

# Install required OS packages
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev && pip3 install --upgrade pip setuptools 
#RUN apt-get update
# Set some environment variables for PIP installation, db management and NewRelic
#ENV FLASK_CONFIG='development' 
ENV DATABASE_URL='postgres://postgres:pwd@localhost/project_psv'
# Expose a port for gunicorn to listen on
EXPOSE 8000

# Make a workdir and virtualenv
WORKDIR /code/project
RUN pip3 install virtualenv
RUN virtualenv flask
RUN . flask/bin/activate


# Install everything else
ADD ./setup.py /code/project
RUN pip3 install -e .

ADD . /code/project
CMD gunicorn run:appp --reload --config config_gunicorn.py --log-level info --log-file - --access-logfile -

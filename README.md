# Using pipenv

Local development testing for optimize version of docker images

```bash
brew install pipenv
brew upgrade pipenv
pipenv install pytest --dev
pipenv install flask
pipenv lock --requirements > requirements.txt
pipenv install python-dateutil
pipenv lock --requirements > requirements.txt
```

## Dockerfile

Optimize Dockerfile: Copy files at the end so that when source code changes all the docker steps before remain the same and we can leverage docker cache capabilities

```bash
FROM python:3.7

RUN pip install pipenv

COPY Pipfile* /tmp/

RUN cd /tmp && pipenv lock --requirements > requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY . /tmp/app

RUN pip install /tmp/app/

WORKDIR /tmp/app

ENTRYPOINT [ "python" ]
CMD ["src/app.py"]

```

## Running container

```bash
# build image
docker build -t flask-test-alex .
# verify image is created
docker images
# run the container
docker run -d -p 5000:5000 flask-test-alex
# verify container is running
docker ps -a
```

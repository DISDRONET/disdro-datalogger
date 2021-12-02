# Check this https://github.com/balenalabs/balena-sound/blob/master/core/sound-supervisor/Dockerfile.template
FROM balenalib/raspberrypi4-64-python:3.6
COPY requirements.txt /usr/src
WORKDIR /usr/src
RUN pip install -r requirements.txt
COPY . /usr/src
CMD ["python3", "disdrodl/main.py"]
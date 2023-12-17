FROM python:3.10.12
WORKDIR /app
COPY . .
RUN apt-get -y update
RUN apt-get install -y ffmpeg
RUN pip install --upgrade pip
RUN pip install spleeter
ENTRYPOINT ["python", "SpleeterTest.py"]
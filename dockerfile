From python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /CMS

WORKDIR /CMS

COPY . .

RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

ENTRYPOINT ["sh", "/wait-for-it.sh"]
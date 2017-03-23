FROM python:2.7.10-wheezy

MAINTAINER Taoge <wenter.wu@daocloud.io>


RUN pip install pip --upgrade \
	&& pip install gunicorn \
	&& pip install gevent 



RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app



COPY ./requirements.txt /usr/src/app/
RUN pip install  -r /usr/src/app/requirements.txt


COPY . /usr/src/app


EXPOSE 5000

CMD ["sh","run.sh"]


	


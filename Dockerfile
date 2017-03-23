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


EXPOSE 80


CMD ["gunicorn","-k","gevent","--max-requests","50000", \
	"--max-requests-jitter","50000","--access-logfile","-", "--error-logfile","-","-b", \
	"0.0.0.0:80","main:app"]


	


FROM nginx:1.9
MAINTAINER Taoge <wenter.wu@daocloud.io>


EXPOSE 80

CMD ["nginx","-g","daemon off;"]


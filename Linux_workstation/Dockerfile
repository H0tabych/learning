FROM ubuntu:latest
MAINTAINER GB_student
RUN apt-get update
RUN apt-get install nginx -y
RUN apt-get install php-fpm -y
RUN mkdir /run/php-fpm
VOLUME "/var/www/html"
EXPOSE 80
CMD /usr/sbin/nginx -g "daemon off;" ; php-fpm -D

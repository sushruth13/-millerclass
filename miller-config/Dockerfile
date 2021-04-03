
FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
ADD nginx.conf  /etc/nginx/nginx.conf
RUN apt update && apt upgrade -y && apt install vim -y
EXPOSE 80
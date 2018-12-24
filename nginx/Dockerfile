# FROM nginx:1.13.3
FROM nginx:stable-alpine

# RUN rm /etc/nginx/nginx.conf
# COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/

# RUN rm /etc/nginx/sites-enabled/default
# ADD sites-enabled/ /etc/nginx/sites-enabled
FROM python:3.6-alpine3.7

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.7/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.7/community" >> /etc/apk/repositories

# install chromedriver
RUN apk -U --no-cache add build-base chromium chromium-chromedriver ffmpeg
WORKDIR /root
ADD . .
RUN pip install falcon waitress requests decora-wifi
EXPOSE 8888
ENTRYPOINT [ "python", "server.py" ]
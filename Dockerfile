FROM alpine:edge

RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories
RUN apk add --no-cache --update \
    coreutils \
    bash \
    nodejs \
    build-base \
    bzip2-dev \
    curl \ 
    libpng-dev \ 
    openblas-dev \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    util-linux \
    libevent \
    jpeg-dev \
    libffi-dev \
    libpq \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    musl \
    openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-dev \
    openssl \
    jq \
    wget \
    python3 \
    python3-dev \
    readline-dev \
    sqlite \
    ffmpeg \
    sqlite-dev \
    chromium \
    chromium-chromedriver \
    zlib-dev \
    jpeg \
    megatools \
    freetype-dev \
    redis \
    imagemagick

ENV PATH="/app/bin:$PATH"
WORKDIR /app

RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN git clone https://github.com/janjongboom/alpine-opencv-docker.git && cd alpine-opencv-docker && mv opencv-prebuilt/cv2.so /usr/lib/python3.8/site-packages && mkdir /usr/local/include && mkdir /usr/local/include/opencv && mv opencv-prebuilt/include-opencv/* /usr/local/include/opencv && mkdir /usr/local/include/opencv2 && mv opencv-prebuilt/include-opencv2/* /usr/local/include/opencv2 && mv opencv-prebuilt/local-lib/* /usr/local/lib && cd .. && rm -rf alpine-opencv-docker
RUN python3 -c "import cv2"

RUN git clone https://github.com/Ayush1311/PAPERPLANE.git -b master /app

RUN pip3 install -r requirements.txt

COPY ./sample_config.env ./userbot.session* ./config.env* ./client_secrets.json* ./secret.json* /app/

CMD ["bash","init/start.sh"]

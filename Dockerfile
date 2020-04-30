FROM alpine:edge
RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories
RUN apk add --no-cache=true --update \
    coreutils \
    bash \
    nodejs \
    build-base \
    bzip2-dev \
    curl \
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
    libxslt-dev \
    linux-headers \
    musl \
    jq \
    wget \
    python3 \
    python3-dev \
    readline-dev \
    sqlite \
    ffmpeg \
    sqlite-dev \
    sudo \
    zlib-dev \
    jpeg \
    megatools \
    freetype-dev
RUN git clone https://github.com/Ayush1311/PAPERPLANE.git -b master /app
RUN mkdir /app/bin
WORKDIR /app
ENV PATH="/app/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt
COPY ./sample_config.env ./userbot.session* ./config.env* ./client_secrets.json* ./secret.json* /app/
CMD ["bash","init/start.sh"]

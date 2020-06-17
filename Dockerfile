FROM alpine:edge 

ENV LANG=C.UTF-8

# Add Edge repos
RUN echo -e "\n\
@edgemain http://nl.alpinelinux.org/alpine/edge/main\n\
@edgecomm http://nl.alpinelinux.org/alpine/edge/community\n\
@edgetest http://nl.alpinelinux.org/alpine/edge/testing"\
  >> /etc/apk/repositories
RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

# Install required packages
RUN apk update && apk upgrade && apk --no-cache add \
    coreutils \
    bash \
    nodejs \
    build-base \
    bzip2-dev \
    curl \
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
    fortune \
    cowsay \
    imagemagick \
    ca-certificates \
    clang-dev \
    clang \
    cmake \
    curl \
    ffmpeg-dev \
    ffmpeg-libs \
    gettext \
    lcms2-dev \
    libavc1394-dev \
    libc-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libressl-dev \
    libtbb@edgetest \
    libtbb-dev@edgetest \
    make \
    openblas@edgecomm \
    openblas-dev@edgecomm \
    openjpeg-dev \
    tiff-dev \
    unzip \
    zlib-dev


ENV PATH="/app/bin:$PATH"
WORKDIR /app

RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache


# Install NumPy
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h && \
  pip3 install numpy

RUN pip3 install opencv-python

RUN git clone https://github.com/Ayush1311/PAPERPLANE.git -b master /app

RUN pip3 install -r requirements.txt

COPY ./sample_config.env ./userbot.session* ./config.env* ./client_secrets.json* ./secret.json* /app/

CMD ["bash","init/start.sh"]

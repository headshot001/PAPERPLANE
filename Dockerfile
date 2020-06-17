FROM alpine:edge 

ENV LANG=C.UTF-8

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


ENV SRC_DIR=/tmp
ENV CC=/usr/bin/clang CXX=/usr/bin/clang++



RUN apk add --no-cache --virtual .build-deps \
        build-base \
        clang \
        clang-dev \
        cmake \
        git \
        wget \
        unzip 

RUN apk add --no-cache \
        jasper-dev \
        libavc1394-dev  \
        libdc1394-dev \
        libjpeg-turbo-dev \
        libpng-dev \
        libtbb \
        libtbb-dev \
        libwebp-dev \
        linux-headers \
        openblas-dev \
        tiff-dev 

    # fix for numpy compilation
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h \

    # install numpy
RUN pip install numpy==1.12.0 \

    # download opencv source
    && mkdir -p ${SRC_DIR} \
    && cd ${SRC_DIR} \
    && wget https://github.com/opencv/opencv/archive/3.2.0.zip \
    && unzip 3.2.0.zip \
    && mv opencv-3.2.0 opencv \
    && rm 3.2.0.zip \

    # download opnecv_contrib source
    && wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip \
    && unzip 3.2.0.zip \
    && mv opencv_contrib-3.2.0 opencv_contrib \
    && rm 3.2.0.zip \

    # build
    && mkdir -p ${SRC_DIR}/opencv/build \
    && cd ${SRC_DIR}/opencv/build \
    && cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules/ -D BUILD_DOCS=OFF .. \
    && make -j4 \
    && make install \
    && rm -rf ${SRC_DIR} \
    && ln /dev/null /dev/raw1394 \
    && apk del --purge .build-deps


ENV PATH="/app/bin:$PATH"
WORKDIR /app

RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

RUN git clone https://github.com/Ayush1311/PAPERPLANE.git -b master /app

RUN pip3 install -r requirements.txt

COPY ./sample_config.env ./userbot.session* ./config.env* ./client_secrets.json* ./secret.json* /app/

CMD ["bash","init/start.sh"]

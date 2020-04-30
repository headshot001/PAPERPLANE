#! /usr/bin/env bash
# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

apt-get update && add-apt-repository universe && apt-get install -y redis-server
redis-server --daemonize yes
python3 -m userbot

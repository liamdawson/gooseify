#!/usr/bin/env bash

mkdir -p build/layer/bin && \
  cd build/layer && \
  curl -fsSL https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    | tar -x --strip-components=1 --directory=bin '**/ffmpeg' '**/ffprobe'

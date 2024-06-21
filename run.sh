#!/bin/bash

# イメージ名を指定
IMAGE_NAME="dezero"

# ホストの共有フォルダとコンテナのマウントポイントを指定
HOST_DIR="/Users/mn/workspace/dezero/src"
CONTAINER_DIR="/workspace/src"

# Dockerコンテナを実行
echo "Running Docker container from image: $IMAGE_NAME"
docker run -it --rm -v $HOST_DIR:$CONTAINER_DIR $IMAGE_NAME

# 実行が成功したかをチェック
if [ $? -eq 0 ]; then
    echo "Docker container ran successfully."
else
    echo "Failed to run Docker container."
    exit 1
fi
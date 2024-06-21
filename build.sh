#!/bin/bash

# イメージ名を指定
IMAGE_NAME="dezero"

# Dockerイメージをビルド
echo "Building Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME .

# ビルドが成功したかをチェック
if [ $? -eq 0 ]; then
    echo "Docker image $IMAGE_NAME built successfully."
else
    echo "Failed to build Docker image $IMAGE_NAME."
    exit 1
fi
# ベースイメージとしてContinuumIOのAnaconda3イメージを使用
FROM continuumio/anaconda3

# 作成者情報
LABEL maintainer="your_email@example.com"

# 必要なパッケージのインストール
RUN apt-get update --fix-missing && \
    apt-get install -y git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの作成
RUN mkdir -p /workspace/src

# ホストの共有フォルダをマウントするためのVOLUME命令
VOLUME ["/workspace/src"]

# シェルの設定
SHELL ["/bin/bash", "-c"]

# コンテナのデフォルトコマンド
CMD ["bash"]
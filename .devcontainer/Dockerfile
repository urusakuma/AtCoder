FROM python:3.8-slim-bookworm

ARG USERNAME=vscode
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update \
    && groupadd --gid ${USER_GID} ${GROUPNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && apt-get -y install sudo \ 
    && echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

# Python3, PyPy3の環境想定
RUN apt-get update && \
    apt-get install -y python3-pip pypy3 nodejs npm

# pythonライブラリをインストール
COPY requirements.txt /tmp/
RUN python -m pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt

# コンテスト補助ツールをインストール
RUN pip3 install online-judge-tools \
    && npm install -g atcoder-cli \
    && pip3 install aclogin

# .config ディレクトリを作成して所有権を変更
RUN mkdir -p /home/$USERNAME/.config/atcoder-cli-nodejs/python \
    && chown -R $USERNAME:$GROUPNAME /home/$USERNAME/.config

# エイリアスを.bashrcに追加
COPY aliases.sh /home/$USERNAME/
RUN cat /home/$USERNAME/aliases.sh >> /home/$USERNAME/.bashrc

# atcoder-cliの設定ファイルをコピー
COPY main.py /home/$USERNAME/.config/atcoder-cli-nodejs/python/
COPY template.json /home/$USERNAME/.config/atcoder-cli-nodejs/python/

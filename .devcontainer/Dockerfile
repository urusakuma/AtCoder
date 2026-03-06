FROM python:3.11
ARG USERNAME=vscode
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

# aptでのインストール
RUN apt-get update \
    && apt-get install -y git nodejs npm \
    && rm -rf /var/lib/apt/lists/*

# ユーザー作成
RUN groupadd --gid ${USER_GID} ${GROUPNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}
# pipでのインストール
COPY .devcontainer/requirements.txt /tmp/
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm -f /tmp/requirements.txt

# npmでのインストール
RUN npm install -g atcoder-cli

# .config ディレクトリを作成して所有権を変更
RUN mkdir -p /home/$USERNAME/.config/atcoder-cli-nodejs/python \
    && chown -R $USERNAME:$GROUPNAME /home/$USERNAME/.config

# エイリアスを.bashrcに追加
COPY --chown=${USERNAME}:${GROUPNAME} .devcontainer/aliases.sh /tmp/aliases.sh
RUN cat /tmp/aliases.sh >> /home/$USERNAME/.bashrc

# atcoder-cliの設定ファイルをコピー
COPY --chown=${USERNAME}:${GROUPNAME} .devcontainer/main.py /home/${USERNAME}/.config/atcoder-cli-nodejs/python/
COPY --chown=${USERNAME}:${GROUPNAME} .devcontainer/template.json /home/${USERNAME}/.config/atcoder-cli-nodejs/python/
COPY --chown=${USERNAME}:${GROUPNAME} .devcontainer/config.json /home/${USERNAME}/.config/atcoder-cli-nodejs/

RUN rm -rf /tmp/*
#!/usr/bin/env bash
set -euo pipefail

if ! command -v apt-get >/dev/null 2>&1; then
  echo "このスクリプトは Debian/Ubuntu 系の apt 環境向けです。"
  exit 1
fi

if [ "$(id -u)" -eq 0 ]; then
  SUDO=""
else
  if ! command -v sudo >/dev/null 2>&1; then
    echo "sudo が見つかりません。root で実行してください。"
    exit 1
  fi
  SUDO="sudo"
fi

$SUDO apt-get update
$SUDO apt-get install -y ca-certificates curl gnupg lsb-release
$SUDO install -m 0755 -d /etc/apt/keyrings

if [ ! -f /etc/apt/keyrings/docker.gpg ]; then
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    | $SUDO gpg --dearmor -o /etc/apt/keyrings/docker.gpg
fi
$SUDO chmod a+r /etc/apt/keyrings/docker.gpg

. /etc/os-release
case "${ID}" in
  ubuntu|debian)
    DOCKER_REPO_OS="${ID}"
    ;;
  *)
    echo "未対応ディストリビューションです: ${ID}"
    exit 1
    ;;
esac

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/${DOCKER_REPO_OS} ${VERSION_CODENAME} stable" \
  | $SUDO tee /etc/apt/sources.list.d/docker.list >/dev/null

$SUDO apt-get update
$SUDO apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

if [ -n "${SUDO}" ]; then
  $SUDO usermod -aG docker "$USER" || true
  echo "インストール完了。docker グループ反映のため再ログインしてください。"
else
  echo "インストール完了。必要に応じて利用ユーザーを docker グループへ追加してください。"
fi

docker --version

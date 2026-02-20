# Jenkins Docker Deploy

Docker で Jenkins を起動するための最小構成です。  
`docker compose` だけで起動でき、データは named volume に永続化されます。

## 前提

- Docker / Docker Compose が使えること

Docker が未インストールなら、先に以下を実行してください（Ubuntu/Debian 系）。

```bash
bash scripts/install-docker-host.sh
```

## クイックスタート

1. 必要なら環境変数ファイルを用意

```bash
cp .env.example .env
```

2. Jenkins を起動

```bash
make up
```

3. 初期管理者パスワードを取得

```bash
make password
```

4. ブラウザでアクセス

```text
http://localhost:8080
```

## 主要コマンド

- 起動: `make up`
- 停止: `make down`
- 状態確認: `make ps`
- ログ確認: `make logs`
- イメージ再ビルド: `make rebuild`
- `sudo` が必要な環境で起動: `make DOCKER="sudo docker" up`

## 構成ファイル

- `compose.yml`: Jenkins コンテナ定義
- `Dockerfile`: Jenkins カスタムイメージ定義
- `plugins.txt`: 初期インストールする Jenkins プラグイン一覧
- `Makefile`: よく使う運用コマンド
- `scripts/install-docker-in-image.sh`: Jenkins イメージ内に Docker CLI を導入するスクリプト
- `scripts/install-docker-host.sh`: ホスト OS に Docker Engine / Compose を導入するスクリプト

## 永続化

Jenkins のデータは `jenkins_home` ボリュームに保存されます。  
`make down` だけでは削除されません。

## トラブルシュート

- Pipeline で `agent { docker { image '...' } }` が `docker: not found` で失敗する場合
  - このディレクトリの構成では Jenkins コンテナに Docker CLI を同梱し、`/var/run/docker.sock` をマウントして利用します
  - 設定変更後は再ビルドが必要です

```bash
make rebuild
make up
```

- `permission denied while trying to connect to the Docker daemon socket` が出る場合
  - 一時対応: `make DOCKER="sudo docker" up`
  - 恒久対応: ユーザーを `docker` グループに追加して再ログイン

```bash
sudo usermod -aG docker $USER
```

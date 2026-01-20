# pipeline-file の Jenkins ジョブ設定方法

このディレクトリの Jenkinsfile を使って、Jenkins の Pipeline ジョブを作成する手順です。

## 前提
- Jenkins に Pipeline / Git 関連プラグインが入っていること
- Jenkins からこのリポジトリにアクセスできること（HTTPS もしくは SSH）

## 共通の作成手順（Pipeline ジョブ）
1. Jenkins のトップ画面で「新規ジョブ作成」をクリック
2. ジョブ名を入力し、「Pipeline」を選択して作成
3. 「Pipeline」セクションで以下を設定
   - Definition: **Pipeline script from SCM**
   - SCM: **Git**
   - Repository URL: このリポジトリの URL
   - Credentials: 必要に応じて設定
   - Branch Specifier: `*/main`（main 以外なら適宜変更）
   - Script Path: 利用したい Jenkinsfile のパス
4. 「保存」
5. 「ビルド実行」

## Jenkinsfile ごとの設定

### Jenkinsfile-connected
- Script Path: `pipeline-file/Jenkinsfile-connected`
- 内容: 1〜100 の乱数を作って CSV 化し、10 倍した結果をログに出力
- 生成物: `random_number.csv`（成功/失敗に関係なくアーカイブ）

### Jenkinsfile-multiply-param
- Script Path: `pipeline-file/Jenkinsfile-multiply-param`
- 内容: パラメータ `INPUT_NUMBER` を受け取り、10 倍して出力
- 実行時パラメータ:
  - `INPUT_NUMBER`（1〜100 の数値）
- 注意: 1〜100 以外の値は `Validate` ステージで失敗

### Jenkinsfile-random-csv
- Script Path: `pipeline-file/Jenkinsfile-random-csv`
- 内容: 1〜100 の乱数リストを CSV に出力
- 生成物: `random_numbers.csv`（成功時のみアーカイブ）

## 補足
- `shuf` を使っているため、Linux 系エージェントでの実行を想定しています。
- Windows エージェントの場合は `shuf` を別手段に置き換える必要があります。

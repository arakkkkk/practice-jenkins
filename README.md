# Jenkinsを触っているプロジェクト

## Pipelineの作成
* [Jenkinsを勉強する - Pipelineを使ってみる](https://zenn.dev/kaq/articles/a2ce59864a03b0)
*



## 説明
* Jenkinsとは
    * Jenkinsおじさん
* メリット (一般的)
* 定期バッチ、運用自動化で主に使われている
* これが
    * 作業用の仮想マシンに接続
    * gitlabからスクリプトをダウンロード
    * pythonでスクリプトを実行 `python check_vm_state.py --vm_name=aravm`
    * ログを証跡として残す
* こうなる
    * Jenkinsにログイン
    * 自動化jobを開く
    * パラメータを入力して実行
    * ログは自動で残る
* メリット
    * Web GUIから実行可能
    * 個別の実行環境が不要 (実行環境に依存しない)
    * (定期実行も可能)
* やってみる
    * git repository作成
    * job作成
    * git連携
    * 実行
* やってみるjenkinsファイル
    * git repository作成
    * jenknisfile作成
    * git連携
    * 実行
* エンジニアはIaCが大好きなのでjobの設定もコードにしたがります。
* jenkinsファイルの書き方
* パイプライン実行

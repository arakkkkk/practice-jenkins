# SPEC: Jenkins Upstream/Downstream 連携ミニマム実装

## 1. 目的
Jenkins のパイプライン連携機能を検証するため、最小構成で以下を実現する。

- Upstream ジョブから Downstream ジョブを呼び出す
- Upstream で生成したペイロードを Downstream にパラメータとして引き渡す
- ペイロードの件数分だけ Downstream を繰り返し実行する

## 2. スコープ
本仕様の対象は以下 3 コンポーネント。

- Upstream ジョブ定義（Jenkins パイプライン）
- Downstream ジョブ定義（Jenkins パイプライン）
- ペイロード生成スクリプト（`script/payload.py`）

Jenkins のインフラ構築、認証設定、通知連携は対象外。

## 3. 用語
- Upstream: Downstream を起動する親ジョブ
- Downstream: Upstream からパラメータ付きで起動される子ジョブ
- payload: `payload.py` が出力する JSON 文字列（辞書オブジェクトの配列）

## 4. 機能要件

### 4.1 Upstream 要件
- `payload.py` を実行して標準出力を取得する
- 出力を JSON としてパースする
- JSON のトップレベルが配列であることを検証する
- 配列の各要素を 1 件ずつ処理し、Downstream ジョブを起動する
- Downstream 起動時に `title`, `name`, `value` の 3 パラメータを渡す

### 4.2 Downstream 要件
- `title`, `name`, `value` の 3 つの文字列パラメータを受け取る
- 3 パラメータが空でないことを検証する
- 受信した値を処理対象として実行できること（最小実装ではログ出力で可）

### 4.3 payload.py 要件
- JSON 配列を標準出力に 1 行で出力する
- 配列要素は辞書（オブジェクト）である
- 各辞書は `title`, `name`, `value` の 3 キーを持つ
- 配列件数 `N` に対し、Downstream が `N` 回起動される

## 5. データ仕様

### 5.1 payload フォーマット
```json
[
  {
    "title": "first",
    "name": "alice",
    "value": "10"
  }
]
```

### 5.2 パラメータマッピング
- `payload[i].title` -> Downstream `title`
- `payload[i].name` -> Downstream `name`
- `payload[i].value` -> Downstream `value`

## 6. 処理フロー
1. Upstream が開始される
2. Upstream が `python3 script/payload.py` を実行する
3. Upstream が payload(JSON) をパースして配列を走査する
4. 各要素ごとに Downstream を 1 回起動する
5. Downstream は受け取った 3 パラメータを検証し、処理を実行する

## 7. 例外・エラーハンドリング
- `payload.py` の出力が空: Upstream を失敗終了
- JSON パース不可: Upstream を失敗終了
- トップレベルが配列でない: Upstream を失敗終了
- 要素がオブジェクトでない、または必要キー不足: Upstream を失敗終了
- Downstream で必須パラメータが空: Downstream を失敗終了

## 8. 受け入れ条件（Acceptance Criteria）
- Upstream から Downstream が呼び出される
- `payload.py` が返す配列件数と Downstream 実行回数が一致する
- 各 Downstream 実行で `title`, `name`, `value` が正しく受け渡される
- 不正 payload 時に適切にジョブが失敗する

## 9. 最小実装方針
- Downstream の業務処理はログ出力に留める
- 実運用向け拡張（通知、リトライ制御、並列化、監査ログ）は別途検討する


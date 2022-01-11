# APIGateway.2

## リスク

- API Gatewayからアクセスするバックエンドサービスが、正当ではない呼び出し元からアクセスされても検知できないリスク

## 対策

- API Gatewayのコンソールでクライアント証明書を作成し、ステージに適用する
- <https://docs.aws.amazon.com/ja_jp/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>

### 実施時のTIP

- API Gatewayのステージを利用していないとこの項目は検出されない

## 対策を行わない場合のリスク軽減策

- API Gatewayからアクセスするバックエンドサービスが外部からアクセスできないよう構成する

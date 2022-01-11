# ELB.4

## リスク

- RFCに準拠していない不正なHTTPヘッダーを含むリクエストを処理することで、HTTP Desync攻撃が発生する可能性がある。

### 参考

- <https://docs.aws.amazon.com/ja_jp/elasticloadbalancing/latest/application/application-load-balancers.html>

## 対策

- 「無効なヘッダーフィールドを削除」を有効化する。
- 上記と合わせて、RFC 7230に準拠するHTTPリクエストとなるようにアプリケーションを修正する。

## 対策を行わない場合のリスク軽減策

- バックエンドの間の通信に HTTP/2 を利用したり、バックエンド接続の再利用を無効化する。
- 不正なHTTPヘッダを含むリスクエストがセキュリティリスクとならないか評価する。

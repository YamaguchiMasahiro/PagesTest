# ACM.1

## リスク

- 証明書の有効期限が切れると、TLS接続の検証に失敗してしまう。（有効期限が残り1ヶ月以内、もしくは期限切れ証明書について検出される）

## 対策

- 期限が切れる前に更新する。
- 使用していない証明書の場合、AWS Certificate Managerから削除する。

### 実施時のTIP

- AWS発行の証明書の場合、基本的に自動更新される
- 証明書の更新をDNS認証による自動更新に設定する
- <https://docs.aws.amazon.com/ja_jp/acm/latest/userguide/managed-renewal.html>

## 対策を行わない場合のリスク軽減策

- なし

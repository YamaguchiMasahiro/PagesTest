# RDS.10

## リスク

- RDSインスタンスへの接続にユーザ名・パスワードを使用すると、機密情報を安全に管理するための手間が発生し、漏洩するリスクが高い。

## 対策

- RDSインスタンスの設定にて、データベース認証に「パスワードとIAMデータベース認証」を選択する。データベースへアクセスするユーザーはパスワード無しで作成し、適切なIAMポリシーを付けたIAMロールを利用してデータベースアクセスする。
- <https://blog.serverworks.co.jp/rds-iamdblogin>

### 実施時のTIP

- IAM認証がサポートされているのはMySQL、PostgreSQL、Auroraのみである。

## 対策を行わない場合のリスク軽減策

- データベース接続情報をSecrets ManagerやSystems Manager Parameter StoreのSecureStringで安全に保存し、IAMポリシーでアクセス制限を最小限に絞る。

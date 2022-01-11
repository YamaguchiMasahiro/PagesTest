# RDS.9

## リスク

- データベースログを取得しない場合、セキュリティやアクセスの監査を行えなかったり、サービス停止等の障害調査を行えないリスクがある。

## 対策

- 各DBタイプに必要なパラメータ値を持つDB パラメータグループを作成する
- DBインスタンスにパラメータグループを割り当てる
- DBインスタンスでCloudWatch Logsへのログ出力を設定する

### 実施時のTIP

- アラート解消には以下のログ取得を有効にする必要がある
  - PostgreSQLの場合：PostgreSQLログとUpgradeログの両方
  - MySQLの場合：Errorログ、Generalログ、Slow queryログの3つ（Auditログは必須ではない）

## 対策を行わない場合のリスク軽減策

- 無し。
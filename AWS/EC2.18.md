# EC2.18

## リスク

- 80,443番以外のポートに対してインターネットからのアクセスを許可することで攻撃される。

## 対策

- 下記のいずれかを実施する。
  - 許可するポートを80,443番に限定する。
  - 80,443以外のポートを許可するSourceIPアドレスを限定する（0.0.0.0/0としない）。

### 実施時のTIP

- SG（セキュリティグループ）のIPアドレス設定を簡易化するツールを提供可能。

## 対策を行わない場合のリスク軽減策

- 無し。

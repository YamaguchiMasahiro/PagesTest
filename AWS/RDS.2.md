# RDS.2

## リスク

- Amazon RDSインスタンスにアタッチされたパブリックIPアドレスがインターネット上から攻撃され、RDS内の情報が漏洩する。

## 対策

- Amazon RDSインスタンスのパブリックアクセスをなしに設定する。

### 実施時のTIP

- 上記対応を実施しても、下記の手段で対応しやすくなる
- このような手段にて、利便性を損なわずプライベートIPのRDS、proxy内のマシンから接続可能である。
- <https://dev.classmethod.jp/articles/pc-to-rds/>
- 踏み台サーバーのSSHポート転送を利用する
- <https://dev.classmethod.jp/articles/rdp-via-bastion-server/>

## 対策を行わない場合のリスク軽減策

- セキュリティグループ等で接続元IPを制限する。

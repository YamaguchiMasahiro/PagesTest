# EC2.10

## リスク

- EC2がVPCの外側にあるAWSリソースにアクセスする場合に、VPCエンドポイントを使用せず、パブリックIPアドレスを使用することで不正アクセスされるリスクが高まる。

## 対策

- VPCエンドポイントを作成する。

## 対策を行わない場合のリスク軽減策

- 無し。

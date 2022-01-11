# EC2.15

## リスク

- EC2作成時に意図しないパブリックIPアドレスが割り当てされることで、不正アクセスのリスクが高くなる。

## 対策

- サブネットの「パブリック IPv4 アドレスを自動割り当て」をオフ（いいえ）に設定する。
  - ※作成済みのEC2インスタンスには影響しない。

## 対策を行わない場合のリスク軽減策

- 無し。
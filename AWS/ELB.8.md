# ELB.8

## リスク

- ELBのリスナーに設定する定義済みポリシーとして、「TLS-1-2-2017-01」以外を使用することで、セキュリティリスクのある暗号方式等（例えばTLS 1.1など）が使用される可能性がある。

### 参考

- <https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html>

### 実施時のTIP

- デフォルトでは「TLS-1-2-2017-01」が選択されたない可能性があるため、注意すること。

## 対策

- ELBのリスナーの定義済みポリシーとして「TLS-1-1-2017-01」を使用する。

## 対策を行わない場合のリスク軽減策

- 無し。

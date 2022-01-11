# ELB.3

## リスク

- 非暗号化通信は盗聴、改ざんのリスクが高い

## 対策

- Classic Load Balancerを使わず、Application Load BalancerかNetwork Load Balancerを使う
- Classic Load BalancerのリスナーポートをHTTPやTCPではなく、HTTPSかTLSのみに設定する

### 実施時のTIP

- Classic Load BalancerがInternal設定かどうかに関わらず検出される。

## 対策を行わない場合のリスク軽減策

- なし

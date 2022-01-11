# SSM.2

## リスク

- EC2インスタンスのパッチ適用状態が最新でないと、脆弱性により攻撃を受けるリスクが高まる。

## 対策

- Systems ManagerのRun CommandなどでEC2インスタンスのパッチを適用する。

### 実施時のTIP

- Systems Managerで管理されており、パッチのスキャンがされたことが前提で、スキャンの結果がNON_COMPLIANTだったEC2インスタンスのみ検出される。

## 対策を行わない場合のリスク軽減策

- EC2インスタンスが外部からアクセスされないよう対策を行う。（プライベートサブネットに配置する、セキュリティグループでアクセス元IPアドレスを制限する、など）
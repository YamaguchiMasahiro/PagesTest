# RDS.18

## リスク

- RDSインスタンスがVPC外に作成されるとパブリックアクセスが可能になり、データ窃取や改ざんのリスクが高まる。

## 対策

- RDSインスタンスをVPC内に移動する。

### 実施時のTIP

- 現状新しく作成されたAWSアカウントではVPC外にRDSインスタンスを作成することができなくなっているため、この項目が検出されることはなくなった。

## 対策を行わない場合のリスク軽減策

- なし
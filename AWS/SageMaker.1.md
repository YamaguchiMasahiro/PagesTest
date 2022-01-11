# SageMaker.1

## リスク

- SageMakerノートブックインスタンスに対して不正アクセスを起こる可能性がある。

## 対策

- 該当するSageMakerノートブックインスタンスを削除する。

### 実施時のTIP

- VPCあり（直接インターネット接続なし）の設定で、新規にSageMakerノートブックインスタンスを作成する。
- インターネットアクセスを継続するためにNATゲートウェイ かNATインスタンスを設定する。

## 対策を行わない場合のリスク軽減策

- SG（セキュリティグループ）等で接続元IPを制限する。
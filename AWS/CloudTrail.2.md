# CloudTrail.2

## リスク

- CloudTrailログファイルのセキュリティを”更に”強化するため、CloudTrailログファイルにAWS KMSキー（SSE-KMS）を使用して保存時の暗号化を行う。
※デフォルトでAES-256（SSE-S3）を用いた暗号化がされている

## 対策

- CloudTrailでログファイルのSSE-KMS暗号化を有効に設定する。

## 対策を行わない場合のリスク軽減策

- 無し。

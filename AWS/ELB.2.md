# ELB.2

## リスク

- 暗号化通信の信頼性を高めるため、ELBにおいてACM発行の証明書を利用すべき

## 対策

- ACMでSSL/TLS証明書を発行する
- Classic Load BalancerにACM発行のSSL/TLS証明書を関連付ける

## 対策を行わない場合のリスク軽減策

- 無し。

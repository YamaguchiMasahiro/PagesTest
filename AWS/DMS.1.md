# DMS.1

## リスク

- レプリケーションインスタンスに対してパブリックアクセスを許可することでインターネットから攻撃される。

## 対策

- （パブリックアクセスを許可した）既存のレプリケーションインスタンスを削除する。

### 実施時のTIP

- DB（ソース、ターゲット）がレプリケーションインスタンスにVPN、AWS Direct Connect、または VPC ピアリングを使用してアクセスできるようにする。
- パブリックアクセスを選択せずにレプリケーションインスタンスを再作成する。

## 対策を行わない場合のリスク軽減策

- 無し。
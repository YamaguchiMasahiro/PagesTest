# CodeBuild.2

## リスク

- 認証情報の漏洩は、意図しないデータの漏洩や不正なアクセスにつながる可能性がある。

## 対策

- CodeBuild プロジェクトからプレーンテキストの資格情報を含む環境変数を削除する。

### 実施時のTIP

- AWS Systems ManagerのParameter Storeに機密データを含むパラメータを作成し、環境変数の値としてパラメータ名を使用する。
- 以下の条件を両方満たす場合に本項目が検出される。
  - 1. CodeBuildプロジェクトの環境変数名が「AWS_ACCESS_KEY_ID」「AWS_SECRET_ACCESS_KEY」のどちらかである。
  - 2. CodeBuildプロジェクトの環境変数のタイプが「プレーンテキスト」「Secrets Manager」のどちらかである。（「パラメータ」の場合のみ検出されない）

## 対策を行わない場合のリスク軽減策

- 無し。

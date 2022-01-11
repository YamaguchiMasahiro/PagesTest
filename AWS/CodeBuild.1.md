# CodeBuild.1

## リスク

- GitHubやBitbucketの接続URLのパラメータにPersonal Access Tokenやパスワードが含まれていると漏えいのリスクが高い。

## 対策

- GitHubやBitbucketに接続する際にOAuthを利用する。

### 実施時のTIP

- URLパラメータにPersonal Access Tokenを含める方法はGitHubでも非推奨とされており、通常であればこの方法が使われるケースはないと思われる
- OAuthではなくPersonal Access Tokenやパスワードを利用した接続方法でも、URLパラメータにそれらが含まれていなければ、この項目は検出されない。

## 対策を行わない場合のリスク軽減策

- 無し

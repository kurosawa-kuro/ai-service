# 08 リリース Runbook

## リリース前

Markdown 台帳に「リリース」工程はない。`git status --short` で未コミットを確認する程度。

- `docs/tasks/active/` にリリース前の未完了 blocker が残っていないことを確認する。
- リリース対象 task の `Verification` に検証結果が残っていることを確認する。
- 未解決事項がある場合は、release blocker か follow-up かを task に明記する。

## デプロイ

TODO

## ロールバック

TODO

## リリース後タスク

- リリース後の確認事項は `docs/tasks/active/` または `docs/tasks/backlog/` に残す。
- 恒久的な運用手順になったものは `docs/runbooks/` へ昇格する。

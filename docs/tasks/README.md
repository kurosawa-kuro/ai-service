# タスク

軽い作業メモの置き場。「今日やること／次にやること／完了したこと」を雑に管理する。カタログ本体（`src/`）の正本ではない。

## 構成

| ディレクトリ | 用途 |
|---|---|
| `active/` | 進行中、または次にやること |
| `done/` | 完了メモ |
| `backlog/` | いつかやる候補（任意） |

## 運用（軽く）

- 迷ったら `active/` に一行メモを足す。フォーマットは自由。重い契約（Scope/Acceptance/検証レベル）は要らない。
- 確定した内容は task に溜めず、該当する `src/` の台帳や `docs/` に直接反映する。

## Active

| ファイル | 用途 |
|---|---|
| [active/refactoring-candidates.md](active/refactoring-candidates.md) | 残りのクリーンアップ候補 |

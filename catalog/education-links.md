# 教材化リンク

`ai-service` は、黒澤さん個人の AI サービス / 技術カタログ、評価ログ、用途別ルーティングの運用基盤。

`study-ai-tool` は、AIツール比較を学習・説明・教材化するための別リポジトリ。

```text
ai-service
  = 判断DB / 評価ログ / 使い分けルール

study-ai-tool
  = 教材 / 比較記事 / 説明資料
```

## 外部化先

| 用途 | パス |
|---|---|
| 教材・比較記事 | `/Users/kurosawa/Dev/study-ai-tool` |
| Claude Code 教材 | `/Users/kurosawa/Dev/study-ai-tool/claude-code/README.md` |
| Codex 教材 | `/Users/kurosawa/Dev/study-ai-tool/codex/README.md` |
| Cursor 教材 | `/Users/kurosawa/Dev/study-ai-tool/cursor/README.md` |
| GitHub Copilot 教材 | `/Users/kurosawa/Dev/study-ai-tool/github-copilot/README.md` |
| Devin 教材 | `/Users/kurosawa/Dev/study-ai-tool/devin/README.md` |
| DeepSeek 教材 | `/Users/kurosawa/Dev/study-ai-tool/deep-seek/README.md` |

## 教材化元として使うもの

| ai-service 側 | 教材化できる内容 |
|---|---|
| `catalog/services/*.md` | サービスごとの特徴、強み、弱み、黒澤用途 |
| `catalog/usecases/*.md` | 業務別・用途別の使い分け |
| `catalog/evaluations/*.md` | 実タスクでの比較結果、成功例、失敗例 |
| `catalog/routing-rules.md` | 最終的な使い分けルール |
| `catalog/candidates/*.md` | 今後紹介する候補、未検証の話題 |

## 昇格 / 逆流ルール

### ai-service から study-ai-tool へ

- 評価ログがあり、再利用判断が明確なものだけ教材化する。
- 読者向けには、実務文脈、使いどころ、破綻条件を中心に整理する。
- 未確認の料金、API、規約、最新機能は断定しない。
- 教材化したら、このファイルまたは該当サービス台帳に外部化先を追記する。

### study-ai-tool から ai-service へ

- 教材作成中に出た新しいツール候補は `catalog/candidates/` へ戻す。
- 実運用で使う可能性が出たら `catalog/services/` へ台帳化する。
- 教材上のランキングや推奨は、そのまま `routing-rules.md` へ入れない。評価ログを経由する。

## 現在の対応

| study-ai-tool | ai-service |
|---|---|
| `claude-code/README.md` | `catalog/services/claude-code.md` |
| `codex/README.md` | `catalog/services/codex-cli.md` |
| `cursor/README.md` | `catalog/services/cursor.md` |
| `github-copilot/README.md` | `catalog/services/github-copilot.md` |
| `deep-seek/README.md` | `catalog/candidates/category-shelves.md` |
| `devin/README.md` | `catalog/candidates/category-shelves.md` |

## 次にやること

- `study-ai-tool` の各ツール別 README へ、対応する `ai-service/catalog/services/*.md` への参照を追加する。
- `ai-service/catalog/evaluations/` に実評価ログが増えたら、教材化候補をこのファイルへ追記する。

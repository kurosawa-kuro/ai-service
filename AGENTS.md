# AGENTS.md

AI エージェント共通の作業ガイド（Codex / 他）。Claude Code 向けは `CLAUDE.md`。

黒澤さん個人の **AI サービス / 技術カタログ**。実ソースは `src/`（手書き Markdown 台帳）:
`src/services/`（サービス台帳）／ `src/usecases/`（用途逆引き）／ `src/evaluations/`（評価ログ）／ `src/candidates/`（候補）／ `src/routing-rules.md`（使い分け）／ `src/現在の契約.md`。

## 進め方

- 手書きで気軽に足す個人台帳。重いプロセス（承認ゲート・検証レベル・タスク契約・scope-creep 検出）は持たない。**ハーネスは AI を導くもので、owner を縛らない。**
- `src/services/<name>.md` は既存ファイルと同じ見出し構成で。料金 / API / CLI / MCP / ローカル可否は確認日つきで、不明は `未確認`。
- 秘密情報（API キー・接続文字列）はコミットしない。設定は `env/config.yaml`、ローカル秘密は `env/secret.yaml`（コミット禁止）。

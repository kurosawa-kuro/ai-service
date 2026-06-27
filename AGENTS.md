# AGENTS.md

AI コーディングエージェント（Claude Code / Codex / GitHub Copilot 等）共通の作業ガイド。
ツール固有の指示は各ツールのファイル（例: Claude Code は `CLAUDE.md`）に置く。

## Source of Truth

- 要件: `docs/01_requirements.md`
- アーキテクチャ: `docs/02_architecture.md`
- ドキュメント索引: `docs/00_index.md`
- ワークフロー: `docs/04_workflows.md`
- テスト方針: `docs/07_test_strategy.md`
- タスク管理: `docs/tasks/`

`docs/01_requirements.md` と `docs/02_architecture.md` を正とする。迷ったらこの 2 ファイルへ戻る。

## プロジェクト概要

黒澤さん個人の AI サービス / 技術カタログ。

増え続ける AI サービスを、単発の契約判断ではなく、比較可能な能力資産として管理する。サービス名ではなく、能力カテゴリ、用途、ハーネス適性、評価ログを中心に整理する。

## 現在の実装方針

- Phase 1 は Markdown + Git を中心に進める。
- カタログ本体は `catalog/` 配下に置く。
- サービス記録は `catalog/services/`。
- 用途別逆引きは `catalog/usecases/`。
- 評価ログは `catalog/evaluations/`。
- 使い分けルールは `catalog/routing-rules.md`。
- コードが必要な場合の実装先は `src/`。

DB、Web アプリ、検索、CLI、自動ルーティングは将来フェーズ。構造が固まる前に作り込みすぎない。

## 主要コマンド

```bash
make setup
make build
make run
make dev
make test
make fmt
make lint
```

未実装のコマンドがある場合は、作業内容に合わせて `Makefile` を更新する。

## 作業ルール

- 既存の docs を読んでから変更する。
- 仕様・構造・責務に関わる変更は、必要に応じて `docs/tasks/active/` に task を作る。
- サービス台帳は固定フォーマットで横比較できるように保つ。
- 評価ログは再現可能な根拠として残す。印象評価だけで更新しない。
- 用途ページは「第一候補 / 低コスト補助 / ローカル検証 / 判断ルール / 破綻条件」を持つ。
- 確定した仕様は task note に留めず、該当する docs へ反映する。

## セキュリティ

- カタログには API キー、実在アカウント情報、個人データを書かない。
- 非機密の設定は `env/config.yaml` に置く。
- ローカル秘密情報は `env/secret.yaml` に置き、コミットしない。
- 共有・本番の秘密情報は Doppler などの secret manager に置く。
- 機密に近い評価対象は、ローカル実行または契約上許可された環境に限定する。

## Codex / Claude Code

- `AGENTS.md` は Codex / 他エージェント共通ガイド。
- `CLAUDE.md` は Claude Code の司令塔。
- `.claude/rules/` と `.claude/skills/` は Claude Code 用。Codex が読む前提にしない。
- Codex 向けに永続させたい recurring な指摘やミス防止は、この `AGENTS.md` または nested `AGENTS.md` に小さく追加する。

## Harness（AI 制御一式）

- AI 制御の全体像は `.claude/README.md`（Kurosawa Thin Harness Architecture の実装）。
- アーキ本体は `docs/specs/kurosawa-thin-harness-architecture.md`、repo 固有の脅威モデルは `docs/specs/{capability-boundary,change-boundary,runtime-protocol,evidence-policy,judgment-memory}.md`。
- skills は classify-task → create-task → scan-decisions → plan-skeleton → execute-task → verify-completion → review-task のライフサイクル（16本、詳細は `.claude/README.md`）。
- permissions の ask/deny と保護パスは脅威モデルで決める。他プロジェクトの設定をそのまま移植しない。

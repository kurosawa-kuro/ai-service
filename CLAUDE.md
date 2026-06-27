# CLAUDE.md

このファイルは Claude Code がこのリポジトリで作業する際の最小ガイド。

## Source of Truth

- Requirements: `docs/01_requirements.md`
- Architecture: `docs/02_architecture.md`
- Documentation index: `docs/00_index.md`
- Workflows: `docs/04_workflows.md`
- Test strategy: `docs/07_test_strategy.md`
- Task notes: `docs/tasks/`

`docs/01_requirements.md` と `docs/02_architecture.md` を正とする。README やエージェント向けガイドに差分がある場合は、この 2 ファイルへ寄せる。

## プロジェクト概要

黒澤さん個人の AI サービス / 技術カタログ。

目的は、増え続ける AI サービスを「能力カテゴリ」「用途」「ハーネス適性」「評価ログ」で整理し、次回以降の選択判断に使える能力地図として育てること。

## 現在のアーキテクチャ

- Phase 1 は Markdown 台帳が中心。
- カタログ本体は `catalog/` 配下に置く。
- サービス単位の記録は `catalog/services/`。
- 用途からの逆引きは `catalog/usecases/`。
- 実タスクの評価ログは `catalog/evaluations/`。
- 使い分け判断の正本は `catalog/routing-rules.md`。
- コードが伴う場合のソースは `src/` 配下に置く。

早すぎる DB 化、Web アプリ化、網羅的な公式スペック転記を優先しない。構造が固まってから Supabase、検索、CLI、自動ルーティングへ進める。

## コマンド

```bash
make setup    # 初期セットアップ
make build    # ビルド
make run      # 実行
make dev      # 開発サーバー / watch
make test     # テスト
make fmt      # フォーマット
make lint     # 静的解析
```

コマンドが未実装の場合は、作業内容に合わせて `Makefile` を更新する。

## 作業ルール

- 推測で仕様を増やさず、まず `docs/01_requirements.md` と `docs/02_architecture.md` を確認する。
- 中規模以上の構造変更、責務移動、adapter 追加、共通化は、実装前に `docs/tasks/active/` へ task を作る。
- サービス台帳は同一フォーマットで横比較できるようにする。
- 評価は「賢い」「安い」などの印象ではなく、タスク、入力、結果、理由、再利用判断をログとして残す。
- 機密に近い内容はローカル実行または契約上許可された環境に限定する。
- カタログには実在のアカウント情報、API キー、個人データを書かない。
- 仕様変更は連動する `docs/` と必要な検証を同じ作業で更新する。

## 設定と秘密情報

- 非機密の設定は `env/config.yaml` に置く。
- ローカル秘密情報は `env/secret.yaml` に置き、コミットしない。
- 共有・本番の秘密情報は Doppler などの secret manager に置く。

## Claude Code 固有

- `.claude/rules/` と `.claude/skills/` は Claude Code 用。
- 一回性の作業計画は `docs/tasks/` に置く。
- 繰り返し使う Claude Code の作業手順は `.claude/skills/` に置く。
- Codex / 他エージェントにも共有したい永続ルールは `AGENTS.md` に置く。

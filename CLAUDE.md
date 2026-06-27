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

## ハーネス（AI 制御）

このリポジトリの AI エージェント制御一式は `.claude/README.md`（Kurosawa Thin Harness Architecture の実装）。アーキ本体は `docs/specs/kurosawa-thin-harness-architecture.md`（tool-agnostic マスター）、repo 固有の脅威モデルは `docs/specs/{runtime-protocol,capability-boundary,change-boundary,evidence-policy,judgment-memory}.md`。判断日誌は `docs/decisions/decision-log.md`、蒸留記憶は `docs/memory/`。

- **Scope invariant（常時）**: 作業中に Goal/Scope 外の変更・前提崩れ・追加副作用・docs と実装の矛盾を見つけたら即実装しない。`control-change` で分類するか follow-up task に残す。「ついで修正/共通化/改名」は scope creep。
- permissions（`.claude/settings.json`）は安全既定: 生インフラ/DBツールは ask、不可逆破壊のみ deny。このプロジェクトの脅威モデルに合わせ `docs/specs/capability-boundary.md` と一緒に調整する。

### AI Runtime Protocol（薄い・常時）

詳細は `.claude/README.md` と `docs/specs/runtime-protocol.md`、停止条件は同 §「停止して owner に確認する」。

1. Goal / Scope / Done を言い直す。
2. Weight Class を判定（Light / Standard / Heavy → `classify-task`）。Light は以降の重い手順をスキップしてよい。
3. owner-only 判断・保護 capability・allowed/forbidden paths を確認（`scan-decisions` / `capability-boundary.md` / `change-boundary.md`）。
4. Standard/Heavy は skeleton + TDD contract を先に（`plan-skeleton`）。
5. scope 内で最小変更を当てる。複数 attempt が要るなら停止条件付きで回す（`reconcile-task`）。
6. 必要 Evidence Level（≥2、本番は4）で検証（`verify-completion` / `evidence-policy.md`）。
7. scope 拡大・保護境界接触・二度違う理由で検証失敗 → 停止して owner へ。
8. 非自明な判断を下した時だけ記録（`log-decision`）。

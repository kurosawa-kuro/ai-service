# ai-service

AI サービス / 技術を、黒澤用途で比較可能な能力資産として管理する個人カタログ。

単発の「どれを契約するか」判断ではなく、能力カテゴリ、用途、ハーネス適性、評価ログを積み上げて、次回以降の選択根拠にする。

## 方針

- サービス名ではなく、能力カテゴリと用途から逆引きできる形で管理する。
- 公式スペックの網羅より、黒澤用途での勝ち筋、破綻条件、再利用判断を優先する。
- 最初から Web アプリや DB を作らず、Markdown + Git + 月次レビューで始める。
- API / CLI / MCP / ローカル実行など、自分のワークフローへ組み込めるかを重要な評価軸にする。

## 現在のフェーズ

Phase 1 の Markdown 台帳を構築する段階。

```text
src/
  ├── services/        # サービス単位の記録
  ├── usecases/        # 用途単位の逆引き
  ├── evaluations/     # 実タスクの評価ログ
  └── usecases/使い分けルール.md # 使い分け判断の正本
```

将来的には、構造が固まってから Supabase 化、検索 UI / CLI、自動ルーティングへ進める。

## 技術スタック

| レイヤー | 方針 |
|---|---|
| 台帳 | Markdown |
| バージョン管理 | Git |
| アプリケーションコード | `src/` |
| 設定 | `env/config.yaml`、環境変数 |
| 秘密情報 | `env/secret.yaml`、Doppler |
| DB / 検索 | 将来フェーズで検討 |

## 使い方

手書き Markdown 台帳。ビルド / テストはなし。`src/` を直接編集し、`git` で差分管理する。

設定は `env/config.yaml`（非機密）、`env/secret.yaml`（ローカル秘密情報）、Doppler（共有・本番秘密情報）で管理する。
`env/secret.yaml` は `.gitignore` で除外されるためコミットしない。

## ディレクトリ構成

```text
.
├── src/           # Markdown 台帳本体
├── docs/              # source-of-truth ドキュメント
├── env/               # 非機密設定とローカル秘密情報
├── AGENTS.md          # Codex / 各種エージェント共通ガイド
└── CLAUDE.md          # Claude Code 向けガイド
```

## ドキュメント

開発・運用の詳細は [`docs/00_index.md`](docs/00_index.md) を参照。

- [`docs/01_requirements.md`](docs/01_requirements.md) - 目的、範囲、ユースケース
- [`docs/02_architecture.md`](docs/02_architecture.md) - 成長フェーズ、構成、境界
- [`docs/04_workflows.md`](docs/04_workflows.md) - 作業開始、検証、終了フロー
- [`docs/07_test_strategy.md`](docs/07_test_strategy.md) - テスト方針

# ドキュメント索引

補助ドキュメントの索引。プロジェクトの**実ソース（カタログ本体）は `src/`**。エージェント向けガイドは `CLAUDE.md` / `AGENTS.md`、`docs/tasks/` は軽い作業メモ。

## カタログ入口（実ソース）

| パス | 役割 |
|---|---|
| [`../src/services/`](../src/services/) | サービス / 技術ごとの台帳 |
| [`../src/usecases/`](../src/usecases/) | 用途別の逆引き |
| [`../src/evaluations/`](../src/evaluations/) | 実タスクの評価ログ |
| [`../src/candidates/`](../src/candidates/) | 未検証候補の棚 |
| [`../src/usecases/使い分けルール.md`](../src/usecases/使い分けルール.md) | 使い分け判断の正本 |
| [`../src/contracts/現在の契約.md`](../src/contracts/現在の契約.md) | 今の契約 ／ [`../src/services/コーディングプラン比較.md`](../src/services/コーディングプラン比較.md) プラン比較 |

## 補助ドキュメント（軽い参照）

| ドキュメント | 役割 |
|---|---|
| [01_requirements.md](./01_requirements.md) | 目的・範囲・ユースケース |
| [02_architecture.md](./02_architecture.md) | 構成・能力カテゴリ・境界 |
| [03_domain_model.md](./03_domain_model.md) | 用語・概念 |
| [04_workflows.md](./04_workflows.md) | 運用フロー |
| [05_data_model.md](./05_data_model.md) | 台帳フォーマット |
| [tasks/README.md](./tasks/README.md) | 作業メモ |

> `06_error_policy` / `07_test_strategy` / `08_release_runbook` は旧コード運用の名残で、Markdown 台帳では実質未使用（残置）。

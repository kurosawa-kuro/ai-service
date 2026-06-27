# Catalog candidate placement

## Goal

貼り付けられた AI 個人カタログ構想を、正本、候補棚、生ログ、次アクションに分離して配置する。

## Context

ユーザー依頼: 「これを適切なファイル分離して配置できる？」

## Scope

- 確定モデルは `docs/03_domain_model.md` / `docs/05_data_model.md` へ反映する。
- 未検証候補は `catalog/candidates/` へ置く。
- 用途として固いものは `catalog/usecases/` と `catalog/routing-rules.md` へ反映する。
- 原文は `docs/archive/` に退避する。
- サービスの最新性検証はこのタスクでは行わない。

## Skeleton

- `docs/03_domain_model.md`
- `docs/05_data_model.md`
- `catalog/candidates/`
- `catalog/usecases/`
- `catalog/routing-rules.md`
- `docs/archive/`

## Plan

- 生ログを archive に保存する。
- 候補を能力カテゴリ別に分ける。
- 優先候補を別ファイル化する。
- コーディング用途とルーティングの初期ルールを配置する。
- テンプレートの項目不足を補う。
- テストを通す。

## Acceptance Criteria

- 貼り付け本文が archive に保存されている。
- 未検証候補が `catalog/candidates/` に配置されている。
- ドメイン用語と Markdown データモデルが TODO ではなくなっている。
- `make test` が成功する。

## Verification

- `make test` - 成功（7 tests）
- `find catalog docs/archive docs/tasks/active -maxdepth 3 -type f | sort` - 配置ファイルを確認
- `rg` - ドメイン / データモデル / カタログ / テンプレートの主要語句を確認

## Notes

- 候補棚は採用済み、契約対象、推奨対象を意味しない。
- 原文は `docs/archive/ai-catalog-growth-brainstorm-2026-06-27.md` に保存した。

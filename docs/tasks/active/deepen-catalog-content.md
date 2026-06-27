# Deepen catalog content

## Goal

`catalog/` をさらに充実させ、候補・サービス台帳・用途・評価計画の接続を強くする。

## Context

ユーザー依頼: 「内容を充実させなさい。」

## Scope

- `services/README.md` に横比較を追加する。
- 次候補を複数 `services/` へ昇格する。
- `evaluations/` に比較計画を追加する。
- `routing-rules.md` と `usecases/` を昇格済みサービスに合わせて更新する。
- `candidates/priority-seeds.md` の昇格状況を更新する。

## Skeleton

- `catalog/services/`
- `catalog/usecases/`
- `catalog/evaluations/`
- `catalog/candidates/`
- `catalog/routing-rules.md`

## Plan

- CLI / IDE / ローカル / 検索APIの代表候補を台帳化する。
- 評価計画を用途別に分ける。
- 横比較表を作る。
- ルーティングルールを更新する。
- テストとファイル一覧を確認する。

## Acceptance Criteria

- `catalog/services/` の登録数が増えている。
- `catalog/evaluations/` に比較計画が複数ある。
- `routing-rules.md` が新規台帳と整合している。
- `make test` が成功する。

## Verification

- `make test` - 成功（7 tests）
- `find catalog/services -type f | wc -l` - 19（README + 個別台帳18件）
- `find catalog/evaluations -type f | wc -l` - 6
- `find catalog/usecases -type f | wc -l` - 9（README + 用途8件）
- `rg` で Firecrawl の台帳・候補棚・用途ページ・サービス比較表の整合を確認

## Notes

- 最新料金・規約・API仕様は未検証。断定しない。
- `未確認` / `要確認` / `未評価` は、最新仕様や実評価を未検証として明示する状態。

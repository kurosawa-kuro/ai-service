# Enrich catalog content

## Goal

土台だけだった `catalog/` を、実際に使い始められる初期台帳へ充実させる。

## Context

ユーザー依頼: 「内容を充実させなさい。まだ、土台だけしかないので」

## Scope

- `catalog/README.md` を追加する。
- 代表サービス / 技術の初期台帳を追加する。
- 用途別逆引きを複数追加する。
- routing-rules を用途ごとに厚くする。
- candidates の昇格状況と次候補を整理する。
- evaluations に初期評価計画を追加する。

## Skeleton

- `catalog/services/*.md`
- `catalog/usecases/*.md`
- `catalog/evaluations/*.md`
- `catalog/candidates/*.md`
- `catalog/routing-rules.md`

## Plan

- 代表サービスを第一バッチとして登録する。
- 用途ページを増やす。
- 候補棚に昇格状況を追記する。
- 評価計画を作る。
- テストとファイル一覧を確認する。

## Acceptance Criteria

- `catalog/services/` に複数の初期台帳がある。
- `catalog/usecases/` に主要用途の逆引きがある。
- `catalog/evaluations/` に評価開始の入口がある。
- `catalog/routing-rules.md` から主要用途を引ける。
- `make test` が成功する。

## Verification

- `make test` - 成功（7 tests）
- `find catalog/services catalog/usecases catalog/evaluations catalog/candidates -type f | sort` - 追加ファイルを確認
- `rg -n "^- TODO$|TODO" catalog/usecases catalog/evaluations catalog/README.md catalog/candidates` - 用途・評価入口・候補棚に未処理 TODO がないことを確認

## Notes

- 各サービスの最新料金・規約・API詳細は未検証。初期仮説として記録する。
- サービス台帳の `未確認` は、最新仕様を断定しないため意図的に残している。

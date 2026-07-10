# Enrich catalog content

## Goal

土台だけだった `src/` を、実際に使い始められる初期台帳へ充実させる。

## Context

ユーザー依頼: 「内容を充実させなさい。まだ、土台だけしかないので」

## Scope

- `src/README.md` を追加する。
- 代表サービス / 技術の初期台帳を追加する。
- 用途別逆引きを複数追加する。
- routing-rules を用途ごとに厚くする。
- candidates の昇格状況と次候補を整理する。
- evaluations に初期評価計画を追加する。

## Skeleton

- `src/services/*.md`
- `src/usecases/*.md`
- `src/evaluations/*.md`
- `src/candidates/*.md`
- `src/使い分けルール.md`

## Plan

- 代表サービスを第一バッチとして登録する。
- 用途ページを増やす。
- 候補棚に昇格状況を追記する。
- 評価計画を作る。
- テストとファイル一覧を確認する。

## Acceptance Criteria

- `src/services/` に複数の初期台帳がある。
- `src/usecases/` に主要用途の逆引きがある。
- `src/evaluations/` に評価開始の入口がある。
- `src/使い分けルール.md` から主要用途を引ける。
- リンク・見出しフォーマットを目視確認する。

## Verification

- 目視確認 — OK
- `find src/services src/usecases src/evaluations src/candidates -type f | sort` - 追加ファイルを確認
- `rg -n "^- TODO$|TODO" src/usecases src/evaluations src/README.md src/candidates` - 用途・評価入口・候補棚に未処理 TODO がないことを確認

## Notes

- 各サービスの最新料金・規約・API詳細は未検証。初期仮説として記録する。
- サービス台帳の `未確認` は、最新仕様を断定しないため意図的に残している。

# Phase 1 catalog CLI

## Goal

Phase 1 の Markdown 台帳を、固定フォーマットで書き足せる最小 CLI として実装する。

## Context

`docs/01_requirements.md` と `docs/02_architecture.md` を正とする。
最初から DB / Web アプリを作らず、`src/` 配下の Markdown 台帳を育てる。

## Scope

- `src/` の初期ディレクトリと `routing-rules.md` を生成する。
- `21_サービス/*.md`、`22_用途/*.md`、`30_評価/*.md` の固定フォーマットを生成する。
- 能力カテゴリをコード上の定数として扱う。
- 標準ライブラリのみで動く CLI とテストを追加する。

## Skeleton

- `src/ai_src/`
- `tests/`
- `Makefile`

## Plan

- CLI コマンドを追加する。
- Markdown テンプレート生成ロジックを追加する。
- 既存ファイルを誤って上書きしない。
- ユニットテストと `make test` を通す。

## Acceptance Criteria

- `python -m ai_catalog init` で `src/` の Phase 1 構成を作れる。
- `new-service` でサービス台帳を固定フォーマット生成できる。
- `new-usecase` で用途逆引きページを固定フォーマット生成できる。
- `new-evaluation` で評価ログを固定フォーマット生成できる。
- `make test` が成功する。

## Verification

- `make build` - 成功
- `make test` - 成功（7 tests）
- `make lint` - 成功（7 tests）
- `make run` - CLI help 表示を確認
- 一時ディレクトリで `python -m ai_catalog --root <tmp> init` と `new-service` を実行し、`routing-rules.md` と `21_サービス/claude-code.md` の生成を確認

## Notes

- 実カタログ本体の `src/` は、`make catalog-init` または `python -m ai_catalog init` で生成する。

> **[2026-07-05 SUPERSEDED]** CLI (ai_catalog) は削除。手書き Markdown 台帳を src/ 直下で維持する方針に一本化（scaffold 不使用と判断）。

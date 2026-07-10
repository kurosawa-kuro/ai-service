# 04 ワークフロー

手書き Markdown 台帳の運用フロー。ビルド / テストはない。

## 作業

1. `src/` を直接編集する。サービス台帳 = `src/services/<name>.md`、用途逆引き = `src/usecases/`、評価ログ = `src/evaluations/`、使い分け = `src/使い分けルール.md`。
2. 迷ったら [tasks/README.md](./tasks/README.md) に一行メモを足す（重い契約は不要）。
3. 料金 / API / CLI / MCP / ローカル可否は書く時点で確認し、確認日を添える。不明は `未確認` のまま。

## 終了時

```bash
git diff --check   # 空白崩れの確認
git status --short
```

確定した内容は task に溜めず、`src/` の台帳へ直接反映する。

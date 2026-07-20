# 候補棚

未検証の AI サービス / 技術を置く場所。

ここにあるものは、採用済み、契約対象、推奨対象ではない。サービス台帳へ昇格する前に、最新情報、料金、利用規約、API / CLI / MCP / ローカル可否、黒澤用途での勝ち筋を確認する。

## 昇格フロー

```text
候補棚
  -> src/services/*.md へ登録
  -> src/usecases/*.md へ関連付け
  -> src/evaluations/*.md で検証
  -> src/usecases/使い分けルール.md に判断を反映
```

## ファイル

| ファイル | 用途 |
|---|---|
| `カテゴリ別候補棚.md` | 能力カテゴリ別の候補一覧 |
| `優先候補.md` | 次に台帳化する優先候補 |

## 候補の見方

| 状態 | 意味 |
|---|---|
| 未整理 | 名前だけ拾った状態 |
| 候補 | 能力カテゴリと用途が仮置きされた状態 |
| 昇格待ち | `services/` に台帳化する価値が高い状態 |
| 検証待ち | 台帳はあるが評価ログがない状態 |
| 継続候補 | 評価ログにより A / B 評価がついた状態 |
| 保留 | 価値はありそうだが、今すぐ検証しない状態 |

## 昇格時に確認すること

- 公式サイト / docs
- 料金、無料枠、API料金
- API / CLI / IDE / MCP / AGENTS.md / rules / hooks 対応
- ローカル実行可否
- 商用利用、データ利用、ログ保持、秘密情報の扱い
- 黒澤用途での勝ち筋
- 破綻条件
- 競合候補との差分

## 初期バッチ

まず `優先候補.md` のうち、次の 11 件を `services/` に昇格済み。

- Codex / Codex CLI
- Claude Code
- GitHub Copilot
- Cursor
- OpenRouter
- Ollama
- NotebookLM
- Perplexity
- Gamma
- ElevenLabs
- Langfuse

次の候補は、評価ログを作る前に台帳へ昇格する。

- Cline
- Aider
- OpenCode
- LM Studio
- Tavily
- Exa
- Firecrawl
- LangGraph
- LlamaIndex
- Midjourney
- Sora

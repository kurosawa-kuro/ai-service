# harness-routing

## 第一候補

- OpenRouter
- Codex / Codex CLI
- Claude Code
- LangGraph
- LlamaIndex
- Langfuse

## 低コスト補助

- GroqCloud
- Together AI
- Fireworks AI
- OpenRouter 経由の低価格モデル

## ローカル検証

- Ollama
- LocalAI
- Qdrant / Chroma / pgvector
- Open WebUI

## 判断ルール

- repo作業: Codex / Claude Code のような CLI エージェントを優先する。
- モデル比較: OpenRouter / GroqCloud / Together AI / Fireworks AI を候補にする。
- 状態を持つ長いワークフロー: LangGraph を候補にする。
- RAG / ナレッジ接続: LlamaIndex / LangChain / Haystack を候補にする。
- ログ・評価・コスト監視: Langfuse / Helicone / Promptfoo を候補にする。
- 将来の自作AIルーターは、評価ログと routing-rules を入力にする。

## 破綻条件

- ログや評価なしに自動ルーティングする。
- APIキーや顧客データを Markdown 台帳に書く。
- 複数ツールをつないだだけで品質が上がったと判断する。
- 権限管理なしでブラウザ操作 / PC操作 / 支払い操作を任せる。

## 関連評価ログ

- `catalog/evaluations/2026-06-initial-evaluation-plan.md`

# 優先候補

> 未検証候補。ここにあるものは、次にサービス台帳化する候補であり、採用済みではない。

## 最優先追加

- Codex / Codex CLI（昇格済み）
- Claude Code（昇格済み）
- Devin / Devin Desktop / Windsurf
- Cline（昇格済み）
- Aider（昇格済み）
- OpenCode（昇格済み）
- OpenRouter（昇格済み）
- GroqCloud
- Together AI
- Fireworks AI
- Ollama（昇格済み）
- LM Studio（昇格済み）
- MCP
- AGENTS.md
- LangGraph
- LlamaIndex
- CrewAI
- Dify
- Flowise
- Midjourney
- Sora
- Veo
- Runway
- ElevenLabs（昇格済み）
- Suno
- Gamma（昇格済み）
- NotebookLM（昇格済み）
- Tavily（昇格済み）
- Exa（昇格済み）
- Firecrawl（昇格済み）
- Langfuse（昇格済み）
- Helicone
- Promptfoo

## 昇格済みサービス

| サービス / 技術 | 台帳 | 主な用途 | 次に必要な評価 |
|---|---|---|---|
| Codex / Codex CLI | `catalog/services/codex-cli.md` | repo実装、docs同期 | Claude Code との実装比較 |
| Claude Code | `catalog/services/claude-code.md` | 設計、レビュー、PM判断 | Codex との役割分担 |
| GitHub Copilot | `catalog/services/github-copilot.md` | IDE補完 | 補完品質と開発速度 |
| Cursor | `catalog/services/cursor.md` | AI IDE / エージェント実験 | CLI勢との競合確認 |
| Cline | `catalog/services/cline.md` | VS Code OSSエージェント | 承認フロー、差分品質 |
| Aider | `catalog/services/aider.md` | Git差分前提CLIペアプロ | Codex との局所修正比較 |
| OpenCode | `catalog/services/opencode.md` | ターミナル系エージェント | Codex / Aider との差分 |
| OpenRouter | `catalog/services/openrouter.md` | APIルーター | 料金、ログ、規約、モデル差分 |
| Ollama | `catalog/services/ollama.md` | ローカルLLM | Apple Silicon 上の速度と品質 |
| LM Studio | `catalog/services/lm-studio.md` | GUIローカルLLM | Ollama との差分 |
| NotebookLM | `catalog/services/notebooklm.md` | 手元資料調査 | PDF / 講座資料での精度 |
| Perplexity | `catalog/services/perplexity.md` | 出典つき調査 | 出典品質と一次情報到達性 |
| Tavily | `catalog/services/tavily.md` | エージェント向け検索API | APIレスポンス品質 |
| Exa | `catalog/services/exa.md` | セマンティック検索API | 技術調査 / ニュース検索精度 |
| Firecrawl | `catalog/services/firecrawl.md` | Web抽出 / クロール | HTML抽出品質、RAG投入しやすさ |
| Gamma | `catalog/services/gamma.md` | スライド初稿 | 日本語資料の修正容易性 |
| ElevenLabs | `catalog/services/elevenlabs.md` | ナレーション | 日本語品質、利用権、API |
| Langfuse | `catalog/services/langfuse.md` | LLM評価 / 監視 | self-host、ログ保持、SDK |

## 次の昇格候補

| 優先 | 候補 | 理由 |
|---|---|---|
| 1 | LangGraph | 状態を持つエージェントワークフロー枠 |
| 2 | LlamaIndex | RAG / データ接続枠 |
| 3 | Midjourney | 講座・発信用画像生成枠 |
| 4 | Sora | 動画生成枠 |
| 5 | Helicone | LLM APIログ / コスト監視枠 |
| 6 | Promptfoo | プロンプト / LLMテスト枠 |
| 7 | Dify | AIアプリ / ワークフロー構築枠 |
| 8 | Flowise | ノーコードLLMフロー枠 |
| 9 | Suno | 音楽生成枠 |

## 黒澤用途で価値が高い 5 分類

| 分類 | 候補 |
|---|---|
| CLI / ハーネス系 | Codex / Claude Code / Cline / Aider / OpenCode |
| APIルーター系 | OpenRouter / GroqCloud / Together AI / Fireworks AI |
| RAG・ナレッジ系 | LlamaIndex / pgvector / Qdrant / GraphRAG |
| 調査・ニュース系 | Perplexity / NotebookLM / Tavily / Exa / Firecrawl |
| 講座・発信系 | Gamma / Midjourney / Sora / Veo / Runway / ElevenLabs / Suno |

## 次の作業

1. 昇格済みサービスに評価ログを 1 件ずつ作る。
2. 次の昇格候補から 5 件を `catalog/services/*.md` に追加する。
3. `catalog/usecases/*.md` と `catalog/routing-rules.md` に関連付ける。
4. 月次レビューで A / B / C と観察ポイントを更新する。

# 能力カテゴリ別の候補棚

> 未検証候補。最新性、料金、利用規約、API / CLI / MCP / ローカル可否は、サービス台帳へ昇格するタイミングで確認する。

## 01_基盤モデル / 02_チャットAI

| 名称 | 位置づけ |
|---|---|
| ChatGPT | 汎用チャットAI、基盤モデル利用 |
| Claude | 長文設計、レビュー、PM判断 |
| Gemini | Google系チャットAI / マルチモーダル |
| DeepSeek | 低コスト、OSS / API系候補 |
| Qwen | 中国系モデル、OSS / ローカル検証候補 |
| Grok / xAI | X連携、リアルタイム寄り。Grok 4.5（2026-07-08）は出力 $6 の低コスト大量実装候補（未検証） |
| Mistral / Le Chat / Mistral API | 欧州系、商用API、オープンウェイト |
| Meta Llama | ローカル / OSS系の基準モデル |
| Cohere Command系 | RAG、企業向け、長文・検索拡張 |
| z.ai GLM | 中国系オープンモデル。GLM-5.2（2026-06-16）は 1M コンテキスト・MIT・エージェント基盤候補。ホスト環境（Coding Plan / API / OpenRouter）前提（未検証） |
| Moonshot Kimi | 長文・中国系モデル |
| MiniMax | テキスト・音声・動画系も含む中国系AI |
| Tencent Hunyuan | 中国大手モデル |
| Baidu ERNIE | 中国大手モデル |
| Yi / 01.AI | オープンモデル系 |
| Nous Research | OSS / 研究者向けモデル |
| Databricks DBRX系 | 企業データ基盤寄りモデル |

## 03_検索・リサーチ

| 名称 | 位置づけ |
|---|---|
| Perplexity | AI検索、出典つき調査 |
| Genspark | AI検索・調査・ページ生成 |
| You.com | 検索AI・チャット検索 |
| Phind | 開発者向け検索・技術調査 |
| Consensus | 論文・研究検索 |
| Elicit | 論文レビュー・研究支援 |
| SciSpace | 論文読解・要約 |
| NotebookLM | 手元資料・PDF・ノートを使う調査AI |
| Tavily API | AIエージェント向け検索API |
| Exa.ai | セマンティック検索API |
| Firecrawl | Webクロール・LLM向け抽出 |
| Linkup | エージェント向けWeb検索API |
| Kagi Assistant | 検索品質重視のAI検索 |

## 04_コーディングエージェント / 05_CLI・IDE・ハーネス

| 名称 | 位置づけ |
|---|---|
| OpenAI Codex / Codex CLI | CLI / クラウド / VS Codeエージェント |
| Claude Code | ターミナル / IDE / ブラウザ対応コーディングエージェント |
| GitHub Copilot | IDE補完、Agent、レビュー、GitHub連携 |
| Cursor | AI IDE、エージェント実験 |
| Devin | 自律型ソフトウェアエンジニア |
| Devin Desktop / Windsurf | IDE / エージェント統合系 |
| Replit Agent | ブラウザIDE + アプリ生成 |
| Sourcegraph Cody / Amp | 大規模コードベース理解・企業コード検索 |
| Cline | VS Code拡張型OSSエージェント |
| Roo Code | Cline派生・エージェント型VS Code拡張 |
| Aider | CLI型ペアプロ、Git差分運用 |
| OpenCode | CLI / ターミナル派向けエージェント |
| OpenHands | OSS自律開発エージェント |
| Continue.dev | OSS補完・チャット・IDE連携 |
| Tabnine | 企業向けコード補完 |
| JetBrains AI Assistant | JetBrains IDE向け |
| Augment Code | 大規模コードベース文脈・企業開発 |
| Factory AI / Droid系 | コーディングエージェント運用 |
| Zed AI | 高速エディタ + AI補助 |

## 06_APIルーター・推論基盤

| 名称 | 位置づけ |
|---|---|
| OpenRouter | 複数モデルAPIの統一入口 |
| GroqCloud | 高速推論 |
| Together AI | OSSモデルのサーバーレス推論・学習 |
| Fireworks AI | OSSモデルの高速推論・ファインチューニング |
| Replicate | 画像・動画・音声・LLMモデル実行 |
| Hugging Face Inference Providers | モデル配布・推論・Spaces |
| Baseten | モデルデプロイ基盤 |
| Modal | Python / AIワークロード実行基盤 |
| Lambda Labs | GPUクラウド |
| CoreWeave | GPUクラウド |
| Cerebras Inference | 超高速推論 |
| NVIDIA NIM | NVIDIA系推論・企業導入 |
| AWS Bedrock | AWS上のマルチモデル基盤 |
| Azure AI Foundry | Microsoft / Azure AI基盤 |
| Google Vertex AI | Google Cloud AI基盤 |
| Cloudflare Workers AI | エッジ推論・軽量AI |

## 07_ローカルLLM

| 名称 | 位置づけ |
|---|---|
| Ollama | ローカルLLM実行の定番 |
| LM Studio | GUIでローカルモデル実行 |
| llama.cpp | 軽量ローカル推論の基礎技術 |
| vLLM | 高速サーバー推論 |
| SGLang | 推論最適化・エージェント実行 |
| Text Generation Inference / TGI | Hugging Face系推論サーバー |
| MLX / MLX-LM | Apple Silicon向けローカル推論 |
| KoboldCpp | ローカルLLM実行 |
| GPT4All | ローカルAIアプリ |
| LocalAI | OpenAI互換ローカルAPI |
| Open WebUI | ローカル / 自前LLM用Web UI |
| Jan | ローカルAIアシスタント |
| AnythingLLM | ローカルRAG / ワークスペース |

## 08_RAG・ナレッジDB

| 名称 | 位置づけ |
|---|---|
| Pinecone | マネージドベクトルDB |
| Weaviate | OSS / マネージドベクトルDB |
| Qdrant | Rust製ベクトルDB |
| Milvus / Zilliz | 大規模ベクトルDB |
| Chroma | ローカル / 軽量RAG |
| pgvector | PostgreSQL拡張でベクトル検索 |
| LanceDB | ローカル / 組み込み系ベクトルDB |
| Elasticsearch Vector Search | 既存検索基盤拡張 |
| OpenSearch Vector Engine | AWS / OpenSearch系 |
| GraphRAG | グラフ構造を使うRAG |
| Knowledge Graph RAG | エンティティ関係を使うRAG |
| Reranker | 検索結果の再順位付け |
| Hybrid Search | キーワード検索 + ベクトル検索 |
| Embedding Model | 文書・コード・ニュースのベクトル化 |

## 09_画像生成

| 名称 | 位置づけ |
|---|---|
| Midjourney | 高品質イメージ生成 |
| DALL-E / GPT Image | ChatGPT連携の画像生成 |
| Ideogram | 文字入り画像・ポスター系 |
| Leonardo AI | 画像生成・素材制作 |
| Stable Diffusion / SDXL / Flux | OSS / ローカル画像生成 |
| Black Forest Labs Flux | 高品質OSS / 商用画像生成 |
| Adobe Firefly | 商用デザイン・Adobe連携 |
| Canva AI | Canva内AIデザイン |
| Krea AI | リアルタイム画像生成・補正 |
| Magnific AI | 画像アップスケール |
| Freepik AI | 素材・画像生成 |
| Recraft | ベクター / ブランド素材生成 |

## 10_動画生成

| 名称 | 位置づけ |
|---|---|
| Sora | OpenAI系動画生成 |
| Google Veo | Google / DeepMind系動画生成 |
| Runway Gen系 | 動画生成・編集・映画的表現 |
| Luma Dream Machine | テキスト / 画像から動画生成 |
| Pika | 動画生成・編集 |
| Kling | 中国系動画生成 |
| Hailuo / MiniMax Video | 中国系動画生成 |
| PixVerse | AI動画生成 |
| Haiper | AI動画生成 |
| Higgsfield | SNS動画・人物演出 |
| HeyGen | アバター動画・翻訳動画 |
| Synthesia | 企業向けアバター動画 |
| D-ID | 顔アニメーション・アバター |
| Descript | 動画 / 音声編集AI |
| CapCut AI | SNS動画編集 |
| Filmora AI | 一般向け動画編集AI |

## 11_音声・音楽

| 名称 | 位置づけ |
|---|---|
| ElevenLabs | 音声合成・音声複製・吹替・音声エージェント |
| Suno | 音楽生成 |
| Udio | 音楽生成 |
| Mubert | BGM生成 |
| Stable Audio | 音楽・効果音生成 |
| AIVA | 作曲AI |
| Speechify | 読み上げ |
| Murf AI | ナレーション |
| PlayHT | 音声合成 |
| Resemble AI | 音声複製・音声変換 |
| Deepgram | 音声認識API |
| AssemblyAI | 音声認識・要約API |
| Whisper / Whisper API | 音声文字起こし |
| Cartesia | 低遅延TTS / 音声エージェント |
| Hume AI | 感情・音声AI |
| GPT-Live | OpenAI の full-duplex 音声モデル（2026-07-08 発表）。対話担当と推論担当を分離。API 提供予定（未検証） |

## 12_プレゼン・資料

| 名称 | 位置づけ |
|---|---|
| Gamma | AIスライド生成 |
| Tome | プレゼン生成 |
| Beautiful.ai | プレゼン自動デザイン |
| Canva AI | デザイン・スライド |
| Microsoft Copilot for Microsoft 365 | Word / Excel / PowerPoint / Outlook連携 |
| Google Workspace Gemini | Docs / Sheets / Slides / Gmail連携 |
| Notion AI | ナレッジ・議事録・文章 |
| Coda AI | ドキュメント / 業務DB |
| Mem AI | 個人ナレッジ |
| Craft AI | 文書作成 |
| Grammarly | 英文・文章補正 |
| DeepL Write / DeepL Pro | 翻訳・文章補正 |
| Napkin AI | 図解生成 |
| Whimsical AI | 図解・フローチャート |
| Miro AI | ホワイトボード・企画整理 |
| FigJam AI | デザイン / 企画ボード |

## 13_PM・業務自動化

| 名称 | 位置づけ |
|---|---|
| Linear AI | Issue / 開発管理 |
| Jira AI / Atlassian Intelligence | チケット・プロジェクト管理 |
| ClickUp AI | タスク管理 |
| Asana Intelligence | PM補助 |
| Slack AI | 会話検索・要約 |
| Microsoft Teams Copilot | 会議要約・アクション整理 |
| Fathom | 会議録画・要約 |
| Fireflies.ai | 会議文字起こし |
| tl;dv | 会議録画・要約 |
| Otter.ai | 議事録 |
| Zapier AI | SaaS自動化 |
| Make AI | ワークフロー自動化 |
| n8n + AI nodes | 自前ワークフロー自動化 |
| Dify | AIアプリ / ワークフロー構築 |
| Flowise | ノーコードLLMフロー |
| Langflow | LLMフロー構築 |

## 14_ブラウザ操作・自律実行

| 名称 | 位置づけ |
|---|---|
| Manus系AI | 自律タスク実行AI |
| ChatGPT Work | OpenAI の職場向け汎用エージェント（2026-07-09 発表）。Gmail / Drive / Slack / CRM / ローカルファイル横断。デスクトップ中心（未検証） |
| Gemini Spark | Google のデスクトップエージェント（2026-06-30 macOS 搭載）。Workspace 連携・条件監視・カスタム MCP。米国 AI Ultra ベータ、日本未展開（未検証） |
| Claude Cowork | Anthropic の職場エージェント。2026-07 上旬に Web / モバイル拡張、Max プラン先行（未検証） |
| OpenAI Operator / Computer Use系 | ブラウザ・PC操作 |
| Anthropic Computer Use | 画面操作型エージェント |
| Browser-use | OSSブラウザ操作エージェント |
| Stagehand | AIブラウザ自動化 |
| Playwright MCP | ブラウザ操作をAIに渡す |
| MultiOn | ブラウザ自動操作 |
| Adept系 | PC操作AIの系譜 |
| Rabbit / device agent系 | デバイス操作AI |

## 15_評価・監視・セキュリティ

| 名称 | 位置づけ |
|---|---|
| LangSmith | LangChain / LangGraph系のトレース・評価 |
| Helicone | LLM APIログ・コスト監視 |
| Langfuse | OSS LLM Observability |
| Arize Phoenix | LLM評価・観測 |
| Weights & Biases Weave | LLMアプリ評価 |
| Promptfoo | プロンプト / LLMテスト |
| OpenAI Evals | 評価基盤 |
| Ragas | RAG評価 |
| Giskard | AIテスト・リスク評価 |
| TruLens | RAG / LLM評価 |
| Guardrails AI | 出力制御・検証 |
| Lakera | Prompt Injection対策 |
| Protect AI | AIセキュリティ |
| HiddenLayer | AIモデル防御 |
| Lasso Security | LLMアプリセキュリティ |
| Aporia | AIガードレール |
| Humanloop | プロンプト管理・評価 |
| Leanstral 1.5 | Mistral の Lean 4 形式検証モデル（2026-07-02、Apache 2.0）。定理証明・コード特性の数学的証明・未知バグ発見（未検証） |

## ハーネス / 標準技術

| 名称 | 位置づけ |
|---|---|
| MCP / Model Context Protocol | AIと外部ツール・DB・APIを接続する標準 |
| AGENTS.md | リポジトリ内でAIエージェントに指示を渡す標準ファイル |
| Claude Skills | Claude Code / Claude用のタスク別能力拡張 |
| Codex Agent Skills | Codex用のタスク別ワークフロー拡張 |
| OpenAI Agents SDK | エージェント、ツール、ハンドオフ、状態管理 |
| LangChain | LLMアプリ / ツール連携フレームワーク |
| LangGraph | 状態を持つ長時間エージェント・ワークフロー |
| LlamaIndex | RAG、文書検索、データ接続、エージェント |
| CrewAI | 複数エージェントの役割分担・チーム化 |
| AutoGen | Microsoft系マルチエージェント |
| Semantic Kernel | Microsoft系AIオーケストレーション |
| Haystack | RAG / 検索アプリ基盤 |
| DSPy | プロンプト / パイプライン最適化 |
| Pydantic AI | Python型安全エージェント |
| Mastra | TypeScript系エージェントフレームワーク |
| Composio | エージェント用ツール統合 |
| Zapier MCP / Zapier AI Actions | SaaS操作自動化 |
| Mistral Studio（Prompt / Skill 管理） | Prompt / Skill をバージョン・所有者・実行履歴・ロールバックつきの本番資産として管理（2026-07-09）。Project as Code の参考思想。ただし owner を縛る官僚機構化はしない（未検証） |
| Computer Use | 画面操作型エージェント技術 |

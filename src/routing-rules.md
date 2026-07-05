# routing-rules

用途から AI サービス / 技術を選ぶための使い分け判断の正本。

## 基本方針

- 能力カテゴリ、用途、ハーネス適性、評価ログを根拠に選ぶ。
- 印象評価だけでルーティングしない。
- 機密に近い内容はローカル実行または契約上許可された環境に限定する。
- 「契約を増やす / 減らす」ではなく、増え続ける AI を比較可能な能力資産として扱う。
- 価格だけで判断しない。API / CLI / MCP / AGENTS.md / ローカル可否 / ログの残しやすさを必ず見る。

## ルール

| 用途 | 第一候補 | 低コスト補助 | ローカル検証 | 判断ルール | 破綻条件 |
|---|---|---|---|---|---|
| coding | Claude Code / Codex / Aider / Cline / GitHub Copilot / Cursor | DeepSeek / Qwen / OpenCode | Ollama + Qwen系 / Ollama + DeepSeek系 / LM Studio | 大規模リファクタリングは Claude Code / Codex、局所修正は Aider、VS Code実験は Cline / Cursor、IDE補完は Copilot | 同じファイルを複数AIに同時修正させる。AGENTS.md なしで任せる。差分レビューなしでマージする。 |
| research | Perplexity / NotebookLM / Tavily / Exa | You.com / Phind | ローカルRAG | 人間が読む入口は Perplexity / NotebookLM、エージェント検索は Tavily / Exa、Web抽出は Firecrawl 候補 | 出典未確認のまま意思決定する。最新情報をモデル記憶だけに頼る。 |
| local-secret | Ollama / LM Studio / LocalAI | 小型OSSモデル | Apple Silicon / ローカルGPU | 秘匿・低コスト大量処理は Ollama / LM Studio から検証し、品質が足りない場合だけ外部モデルへ匿名化して渡す | 個人情報や秘密情報を契約上不明な外部サービスへ渡す。 |
| harness-routing | OpenRouter / Codex / Claude Code / LangGraph / LlamaIndex | GroqCloud / Together AI / Fireworks AI | Ollama / LocalAI / Qdrant / Chroma | 自作AIルーターは評価ログと routing-rules を入力にする。ログ・評価・コスト監視を先に設計する | ログなしで自動ルーティングする。APIキーや秘密情報を台帳に書く。 |
| course-content | Claude / ChatGPT / Gamma / NotebookLM / Midjourney / ElevenLabs | Canva AI / DeepSeek / Qwen / Suno | Ollama / ローカルRAG | 構成、資料、画像、音声を分けて選ぶ。最終成果物は事実確認と利用権確認を行う | AI生成内容を事実確認なしで教材化する。商用利用条件を確認しない。 |
| presentation | Gamma / Claude / ChatGPT / Canva AI / NotebookLM | Tome / Beautiful.ai / Napkin AI / Whimsical AI | Ollama / ローカルRAG | 骨子はLLM、初稿は資料生成AI、図解は図解AI、最終版は人間が整える | 見た目だけで採用する。数字や固有名詞を確認しない。 |
| pm-automation | Claude / ChatGPT / Notion AI / Linear AI / Jira AI / Slack AI | ClickUp AI / Asana Intelligence / Fireflies / tl;dv | ローカルRAG / Ollama | 判断整理、会議要約、Issue整理、SaaS自動化を分けて管理する | AI要約を合意事項として扱う。権限設計なしに自動化する。 |
| trading-research | Perplexity / NotebookLM / Tavily / Exa / Claude / ChatGPT | You.com / Kagi Assistant | ローカルRAG / Ollama | 最新ニュース、手元メモ、材料整理、一次ソース確認を分ける | AI要約だけで売買判断する。出典時刻を確認しない。 |

# サービス台帳

サービス / 技術ごとの記録。ここにあるだけでは採用済みではない。
実タスクの評価ログがつき、`routing-rules.md` に反映されて初めて判断材料になる。

## 横比較

> **モバイル / Android** 列は非 iOS（Android 主）視点の判断軸。値は best-effort（✓=対応 / △=web・別アプリ経由 / ✗=PC 専用 / —=API / 要確認）。アプリ有無は変わるので確定は要確認。

| サービス / 技術 | 主カテゴリ | 主用途 | ハーネス適性 | 現評価 | モバイル | Android | 次に見ること |
|---|---|---|---|---|---|---|---|
| Codex / Codex CLI | 04 / 05 | repo実装、docs同期 | 高 | A | △ ChatGPTアプリ | ✓ ChatGPTアプリ | Claude Code との役割分担 |
| Claude Code | 04 / 05 | 設計、レビュー、PM判断 | 高 | A候補 | △ Claudeアプリ | ✓ Claudeアプリ | 実装速度、制限、Codex比較 |
| GitHub Copilot | 04 / 05 | IDE補完 | 中〜高 | B候補 | ✓ GitHub Mobile | ✓ | Agent / Review / MCP 実用性 |
| Cursor | 04 / 05 | AI IDE、複数ファイル編集 | 中〜高 | A候補 | △ モバイル化加速中 | 要確認 | Git 代替化・モバイル対応の実力、CLI 勢との役割分担 |
| Cline | 04 / 05 | VS Code OSSエージェント | 中〜高候補 | 未評価 | ✗ PC専用 | ✗ | ローカル承認フロー、差分品質 |
| Aider | 04 / 05 | Git差分前提のCLIペアプロ | 高候補 | 未評価 | ✗ CLI | ✗ | 既存repoでの編集安定性 |
| OpenCode | 04 / 05 | ターミナル派エージェント | 中〜高候補 | 未評価 | ✗ CLI | ✗ | Codex / Aider との差分 |
| OpenRouter | 06 | APIルーター、モデル比較 | 高候補 | A候補 | △ web/API | △ web | 料金、ログ、規約 |
| Ollama | 07 | ローカルLLM | 中〜高 | A候補 | ✗ PC | ✗ | Apple Silicon上の速度・品質 |
| LM Studio | 07 | GUIローカルLLM | 中候補 | 未評価 | ✗ PC | ✗ | Ollama との差分、モデル管理 |
| NotebookLM | 03 / 08 | 手元資料調査 | 中 | A候補 | ✓ アプリ | ✓ | PDF / 講座資料での精度 |
| Perplexity | 03 | 出典つき調査 | 中 | A候補 | ✓ アプリ | ✓ | 出典品質、一次情報到達 |
| Tavily | 03 | エージェント向け検索API | 高候補 | 未評価 | — API | — API | APIレスポンス品質 |
| Exa | 03 | セマンティック検索API | 高候補 | 未評価 | — API | — API | 技術調査 / ニュース検索精度 |
| Firecrawl | 03 | Web抽出 / クロール | 高候補 | 未評価 | — API | — API | HTML抽出品質、コスト |
| Gamma | 12 | スライド初稿 | 中 | B候補 | △ web | 要確認 | 日本語品質、修正容易性 |
| ElevenLabs | 11 | ナレーション | 中〜高候補 | B候補 | △ アプリ有 | 要確認 | 日本語品質、商用利用、API |
| Langfuse | 15 | LLM評価 / 監視 | 高候補 | B候補 | △ web | △ web | self-host、ログ保持、SDK |

## 優先評価順

1. Codex / Claude Code / Aider / Cline / OpenCode を同じ repo 作業で比較する。
2. Perplexity / NotebookLM / Tavily / Exa / Firecrawl を同じ調査テーマで比較する。
3. Ollama / LM Studio を同じローカル要約タスクで比較する。
4. OpenRouter / Langfuse を小さな API ルーティング実験で組み合わせる。
5. Gamma / ElevenLabs / Midjourney / Sora を講座素材生成で評価する。

## 台帳更新ルール

- 料金、API、CLI、MCP、利用規約は確認日を入れて更新する。
- `未確認` は消すための TODO ではなく、断定を避けるための状態。
- 評価ログが増えたら `継続評価` と `routing-rules.md` を更新する。

# サービス台帳

サービス / 技術ごとの記録。ここにあるだけでは採用済みではない。
実タスクの評価ログがつき、`../12_使い分けルール.md` に反映されて初めて判断材料になる。

## ファイル名と重要順

サービス記事は **`NN_<既存名>.md`** の2桁連番で、黒澤用途で重要な順に並べる（2026-09-06）。先頭4件は owner 指定。以降は現行の主力、API・ローカル基盤、代替エージェント、調査、その他の用途をもとに配置した。番号は評価ランクや契約の有無とは別。

`README.md` はディレクトリの案内として扱う。新規追加や重要順の変更時は、番号とリポジトリ内の参照リンクを一緒に更新する。

運営法人の**所在法域**は番号の後の `cn-` 等で示す（例: `05_cn-deepseek.md`）。データ越境・規約・規制リスクを判断するための既存区分を保持する。

| 番号の後の接頭辞 | 意味 |
|---|---|
| `cn-` | 中国系プロバイダ（国際版がシンガポール法人でも、本体が中国のもの） |
| （なし） | 欧米系。順次 `us-` 等へ整理予定 |

| 番号 | サービス | 配置の理由 |
|---|---|---|
| 01 | [Codex / Codex CLI](01_codex-cli.md) | owner 指定・repo 実装と docs 同期 |
| 02 | [Claude Code](02_claude-code.md) | owner 指定・設計とレビュー |
| 03 | [Cursor](03_cursor.md) | owner 指定・IDE と遠隔実装 |
| 04 | [GitHub Copilot](04_github-copilot.md) | owner 指定・GitHub / IDE / CLI |
| 05 | [DeepSeek](05_cn-deepseek.md) | 一般 LLM 処理の現行主力 |
| 06 | [OpenRouter](06_openrouter.md) | モデル切替・API ルーティング基盤 |
| 07 | [Ollama](07_ollama.md) | ローカル実行の基準候補 |
| 08 | [Qwen](08_cn-qwen.md) | 代替 API・ローカルモデルの候補 |
| 09 | [GLM](09_cn-glm.md) | コーディング用バックエンドの候補 |
| 10 | [OpenCode](10_opencode.md) | モデルを選べる CLI の比較候補 |
| 11 | [Aider](11_aider.md) | Git 差分を軸にした CLI の比較候補 |
| 12 | [Cline](12_cline.md) | VS Code 内エージェントの比較候補 |
| 13 | [NotebookLM](13_notebooklm.md) | 手元資料・教材の調査候補 |
| 14 | [Perplexity](14_perplexity.md) | 出典付き調査の候補 |
| 15 | [Firecrawl](15_firecrawl.md) | 調査・RAG 用の Web 抽出候補 |
| 16 | [Tavily](16_tavily.md) | エージェント向け検索 API 候補 |
| 17 | [Exa](17_exa.md) | 技術調査の検索 API 候補 |
| 18 | [LM Studio](18_lm-studio.md) | ローカル実行の GUI 比較候補 |
| 19 | [Kimi](19_cn-kimi.md) | 長文・コード処理の代替候補 |
| 20 | [Langfuse](20_langfuse.md) | 評価・費用・ログの観測基盤候補 |
| 21 | [Gamma](21_gamma.md) | 講座・営業資料の初稿候補 |
| 22 | [ElevenLabs](22_elevenlabs.md) | 講座・発信素材の音声候補 |
| 23 | [MiniMax](23_cn-minimax.md) | マルチモーダル用途の継続調査候補 |

## 中国系プロバイダ（2026-07-20 新規台帳化）

**主力の DeepSeek をはじめ実戦投入されているのに台帳が存在しなかった。** その是正。

| サービス | 評価 | 学習利用 | 保存先 | 入力単価/1M | 特記 |
|---|---|---|---|---|---|
| [cn-deepseek](05_cn-deepseek.md) | 能力=**A（主力）** / 規約=不可 | ⚠️ 除外の明言なし | 中国固定 | **$0.435**（Pro） | **主な LLM 処理のメイン**。cache hit で約1/120 |
| [cn-qwen](08_cn-qwen.md) | A候補 | ✅ しない | **選択可（東京）** | $2.50（割引中） | 業務適格性が高い。MCP 標準搭載 |
| [cn-glm](09_cn-glm.md) | A候補 | ✅ **しない（契約明記）** | シンガポール | $1.40 | **規約最強・MIT**。⚠️ 親会社が米 Entity List |
| [cn-kimi](19_cn-kimi.md) | 能力=フロンティア圏内 / 規約=不可 | ⚠️ **既定で使う** | 未確認 | $3.00 | AA Index 57 でオープンウェイト最上位。制限理由は規約であって能力ではない |
| [cn-minimax](23_cn-minimax.md) | 保留 | ⚠️ 既定で使う | **米国** | $0.30 | マルチモーダル。⚠️ MIT ではない |

> **評価は能力軸と規約軸を分ける。** DeepSeek と Kimi は**オープンウェイトを出す高速追従者**で、
> Anthropic 側に追従を止める手段がない（[20_モデル/モデル階層.md](../20_モデル/モデル階層.md)）。
> 能力はフロンティア圏内にあり、用途を制限しているのは規約であって性能ではない。

### 用途別の使い分け（規約ベース）

```text
コスト最優先・公開情報        → DeepSeek
秘匿寄り・業務コード          → GLM（非保存）または Qwen（東京リージョン）
顧客データ・受託案件          → 中国系を使わない。ローカル(Ollama)か西側へ
動画・音声素材                → MiniMax（要規約照会）
```

> ⚠️ **二次情報の汚染に注意**: この領域は SEO コンテンツファームによる**捏造ベンチ数値**が流通している
> （例:「Kimi K3 = Terminal-Bench 2.1 で 88.3、世界2位」→ 公式リーダーボードに Kimi のエントリは存在しない）。
> **一次情報以外を台帳に採用しない。**

## 横比較

> **モバイル / Android** 列は非 iOS（Android 主）視点の判断軸。値は best-effort（✓=対応 / △=web・別アプリ経由 / ✗=PC 専用 / —=API / 要確認）。アプリ有無は変わるので確定は要確認。

2026-09-06: Codex / Claude Code / GitHub Copilot / Cursor の4行を公式情報で更新。出典・条件・未検証事項は各サービス台帳を参照。その他の行は今回未再確認。

| サービス / 技術 | 主カテゴリ | 主用途 | ハーネス適性 | 現評価 | モバイル | Android | 次に見ること |
|---|---|---|---|---|---|---|---|
| [Codex / Codex CLI](01_codex-cli.md) | 04 / 05 | repo実装、docs同期、CLI / SDK | 高 | A | △ ChatGPT Remote（接続PC必須） | Remote の個別配布は未確認 | Astra / Terra / Luna の費用差、Work との共有枠 |
| [Claude Code](02_claude-code.md) | 04 / 05 | 設計、レビュー、実装、CLI / SDK | 高 | A候補 | △ Remote Control（有料・接続PC必須） | △ Claudeアプリ / Web経由 | Pro の完了率、Fable 5.1 の従量費用 |
| [Cursor](03_cursor.md) | 04 / 05 | IDE、CLI / SDK、遠隔実装 | 高候補 | A候補 | ✓ iOSアプリ（有料対象プラン） | アプリは計画中 / Web別経路 | 2プールの費用、Origin初期beta、self-hosted |
| [GitHub Copilot](04_github-copilot.md) | 04 / 05 | IDE補完、CLI / SDK、Issue→PR | 高候補 | B候補 | ✓ GitHub Mobile | ✓ | 解約済み。CLI / cloud agent の再評価、AI credits |
| [OpenRouter](06_openrouter.md) | 06 | APIルーター、モデル比較 | 高候補 | A候補 | △ web/API | △ web | 料金、ログ、規約 |
| [Ollama](07_ollama.md) | 07 | ローカルLLM | 中〜高 | A候補 | ✗ PC | ✗ | Apple Silicon上の速度・品質 |
| [OpenCode](10_opencode.md) | 04 / 05 | ターミナル派エージェント | 中〜高候補 | 未評価 | ✗ CLI | ✗ | Codex / Aider との差分 |
| [Aider](11_aider.md) | 04 / 05 | Git差分前提のCLIペアプロ | 高候補 | 未評価 | ✗ CLI | ✗ | 既存repoでの編集安定性 |
| [Cline](12_cline.md) | 04 / 05 | VS Code OSSエージェント | 中〜高候補 | 未評価 | ✗ PC専用 | ✗ | ローカル承認フロー、差分品質 |
| [NotebookLM](13_notebooklm.md) | 03 / 08 | 手元資料調査 | 中 | A候補 | ✓ アプリ | ✓ | PDF / 講座資料での精度 |
| [Perplexity](14_perplexity.md) | 03 | 出典つき調査 | 中 | A候補 | ✓ アプリ | ✓ | 出典品質、一次情報到達 |
| [Firecrawl](15_firecrawl.md) | 03 | Web抽出 / クロール | 高候補 | 未評価 | — API | — API | HTML抽出品質、コスト |
| [Tavily](16_tavily.md) | 03 | エージェント向け検索API | 高候補 | 未評価 | — API | — API | APIレスポンス品質 |
| [Exa](17_exa.md) | 03 | セマンティック検索API | 高候補 | 未評価 | — API | — API | 技術調査 / ニュース検索精度 |
| [LM Studio](18_lm-studio.md) | 07 | GUIローカルLLM | 中候補 | 未評価 | ✗ PC | ✗ | Ollama との差分、モデル管理 |
| [Langfuse](20_langfuse.md) | 15 | LLM評価 / 監視 | 高候補 | B候補 | △ web | △ web | self-host、ログ保持、SDK |
| [Gamma](21_gamma.md) | 12 | スライド初稿 | 中 | B候補 | △ web | 要確認 | 日本語品質、修正容易性 |
| [ElevenLabs](22_elevenlabs.md) | 11 | ナレーション | 中〜高候補 | B候補 | △ アプリ有 | 要確認 | 日本語品質、商用利用、API |

## 優先評価順

1. Codex / Claude Code / Aider / Cline / OpenCode を同じ repo 作業で比較する。
2. Perplexity / NotebookLM / Tavily / Exa / Firecrawl を同じ調査テーマで比較する。
3. Ollama / LM Studio を同じローカル要約タスクで比較する。
4. OpenRouter / Langfuse を小さな API ルーティング実験で組み合わせる。
5. Gamma / ElevenLabs / Midjourney / Sora を講座素材生成で評価する。

## 台帳更新ルール

- 料金、API、CLI、MCP、利用規約は確認日を入れて更新する。
- `未確認` は消すための TODO ではなく、断定を避けるための状態。
- 評価ログが増えたら `継続評価` と `12_使い分けルール.md` を更新する。

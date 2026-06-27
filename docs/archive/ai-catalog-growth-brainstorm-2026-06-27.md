ちがうちがう
まず「契約を増やす/減らす」ではなく、

絞るのは無意味

これからどんどん増えるので

なので、個人カタログとしてどう成長させるべきか
思考時間: 12s
1. 結論

はい、ここは 「AIサービスを絞る」話ではなく、増え続けるAIを自分の武器庫として管理する話です。

黒澤さんが作るべきなのは、単なる一覧表ではなく、

AIサービス個人カタログ + 評価ログ + 使い分けルール + ハーネス接続台帳

です。

イメージはこれです。

AIサービス一覧
  ↓
特徴・料金・API・CLI・ローカル可否
  ↓
用途別評価
  ↓
実際に使ったログ
  ↓
黒澤さん専用の使い分け判断
  ↓
将来的には自作ルーター / Supabase / Markdown / CLI化

つまり、目的は **「どれを契約するか」ではなく、「増え続けるAIを比較可能な資産に変えること」**です。

2. 理由

AIサービスは今後も増えます。

だから、毎回こう考えると破綻します。

ChatGPTとClaudeどっちがいい？
CursorとCopilotどっちがいい？
DeepSeekとQwenどっちがいい？
Geminiは必要？
Perplexityは残す？

これは単発判断です。
増え続ける世界では弱いです。

強い整理はこうです。

このAIは、どの能力カテゴリに属するか？
自分のどの業務に効くか？
API/CLI/ハーネスに接続できるか？
無料枠で検証できるか？
有料化するなら何を回収するか？
過去の検証結果はどうだったか？

つまり、AIサービスを サブスク一覧として見るのではなく、
能力コンポーネントのカタログとして見るべきです。

3. 有力シナリオ
シナリオA：まずMarkdown台帳で始める

最初はこれで十分です。

/ai-catalog
  ├── services/
  │   ├── chatgpt.md
  │   ├── claude.md
  │   ├── deepseek.md
  │   ├── qwen.md
  │   ├── cursor.md
  │   ├── github-copilot.md
  │   ├── gemini.md
  │   └── perplexity.md
  │
  ├── usecases/
  │   ├── thinking.md
  │   ├── coding.md
  │   ├── trading.md
  │   ├── presentation.md
  │   ├── consulting-pm.md
  │   └── research.md
  │
  ├── evaluations/
  │   ├── 2026-06-chatgpt-vs-claude-coding.md
  │   ├── 2026-06-deepseek-lowcost-test.md
  │   └── 2026-06-perplexity-research-test.md
  │
  └── routing-rules.md

この段階では、完璧なDBより 書き足せること が重要です。

シナリオB：評価軸を固定する

各AIサービスは、同じフォーマットで記録します。

# Claude

## 基本
- 種別: 有料 / API / CLI
- 主用途: 長文設計、コードレビュー、PM判断
- ローカル可否: 不可
- API: あり
- CLI: Claude Code
- ハーネス適性: 高

## 強み
- 長文の構造化
- コードレビュー
- PM/リーダー業務の言語化
- 仕様の矛盾発見

## 弱み
- 料金が重くなりやすい
- 最新情報は別途検索が必要
- 速度・制限の影響を受ける

## 黒澤用途
- ハーネス設計
- PM判断
- 技術文書レビュー
- 実装方針の壁打ち

## 検証ログ
- 2026-06-27: コードレビュー精度 高
- 2026-06-27: スライド文章の自然さ 中〜高

## 継続評価
- 評価: A
- 理由: 思考・レビュー用途で代替しにくい

ポイントは、公式スペックより「黒澤用途でどうだったか」を残すことです。

シナリオC：用途側から逆引きできるようにする

AIサービス単位だけだと、数が増えたときに迷います。

なので、用途別ページを作ります。

# 用途: プログラム生成

## 第一候補
- Claude Code
- Codex
- GitHub Copilot
- Cursor

## 低コスト補助
- DeepSeek
- Qwen

## ローカル検証
- Ollama + Qwen系
- Ollama + DeepSeek系

## 判断ルール
- 大規模リファクタリング: Claude Code / Codex
- IDE内補完: Copilot
- エージェント実験: Cursor
- 安価な雑レビュー: DeepSeek / Qwen
- 機密に近い内容: ローカル or 契約上許可された環境

## 破綻条件
- 同じファイルを複数AIに同時修正させる
- rules/AGENTS.mdなしで任せる
- 差分レビューなしでマージする

これを作ると、AIが30個に増えても管理できます。

4. 破綻条件
破綻条件1：サービス名ベースで管理する

これは弱いです。

ChatGPT
Claude
Gemini
DeepSeek
Qwen
Cursor
Copilot
Perplexity

この並べ方だけだと、増えるたびに混乱します。

強いのは、能力カテゴリで分類することです。

思考系
検索系
コード生成系
IDE統合系
CLIエージェント系
API低コスト系
ローカル系
画像/動画/スライド系
音声系
自動化/ワークフロー系
破綻条件2：料金表だけ作る

価格は重要ですが、価格表だけでは武器になりません。

必要なのは、

価格
無料枠
API有無
CLI有無
ハーネス対応
ローカル可否
実務での勝ち筋
黒澤用途での評価

です。

特に重要なのは ハーネス対応 です。

今後のAIサービス評価では、

良いモデルか？

よりも、

自分のワークフローに組み込めるか？
rules / AGENTS.md / MCP / CLI / API / hooks に接続できるか？
ログが残せるか？
再現性があるか？

の方が重要になります。

破綻条件3：評価ログを残さない

AIは印象で評価するとブレます。

たとえば、

Claudeは賢い
DeepSeekは安い
Geminiは微妙
Cursorは便利

これは感想です。

残すべきはこうです。

タスク: Next.jsの認証実装レビュー
入力: app router + middleware + cookie session
結果: Claude A / ChatGPT B+ / DeepSeek B
理由: Claudeは設計矛盾を拾った。DeepSeekは安いが指摘が浅い。
再利用: 認証レビューはClaude優先。

これが積み上がると、黒澤さん専用のAI知能マップになります。

5. 実務・行動への影響

まず作るべき最小構成はこれです。

# AIサービス個人カタログ

## 分類
- 思考整理
- プログラム生成
- コードレビュー
- 最新情報調査
- トレード材料整理
- プレゼン/スライド
- コンサル/PM/リーダー業務
- 低コスト大量処理
- ローカル/秘匿処理
- CLI/ハーネス
- API連携
- 画像/動画/音声

## 各サービスに記録する項目
- サービス名
- 提供会社
- 無料/有料/ローカル
- 月額
- 無料枠
- API有無
- CLI有無
- IDE連携
- MCP対応
- AGENTS.md / rules / hooks 対応
- ローカル実行可否
- 得意用途
- 苦手用途
- 黒澤用途での評価
- 実験ログ
- 継続観察ポイント

そして、カタログの成長段階はこうです。

Phase 1: Markdown台帳
  ↓
Phase 2: 用途別インデックス
  ↓
Phase 3: 評価ログ蓄積
  ↓
Phase 4: Supabase化
  ↓
Phase 5: Streamlit/CLIで検索
  ↓
Phase 6: 自動ルーティング

黒澤さん向けには、最初から完璧なWebアプリにしない方がいいです。

まずは、

Markdown + Git管理 + 月次レビュー

で始める。

その後、

Supabase
Streamlit
ローカルCLI
Discord通知

に拡張する。

特に重要なのは、AIサービスを「契約管理」ではなく「能力地図」として育てることです。

最終的にはこうなります。

黒澤AIカタログ
  = AIサービス一覧
  + 価格/API/CLI情報
  + ハーネス適性
  + 用途別ルーティング
  + 実験ログ
  + 黒澤さん専用の判断基準

この方向なら、AIサービスが10個から50個に増えても、混乱ではなく資産になります。

他にも話題のAIサービス、技術を一旦書き出し依頼

ChatGPT
Claude
Gemini
DeepSeek
Qwen
Cursor
Copilot
Perplexity

これは「採用判断」ではなく、カタログの見出し候補を一気に広げる用途で整理します。サービス名だけでなく、後で評価軸にしやすい技術カテゴリも混ぜて書き出します。

この一覧は「今すぐ使う候補」ではなく、黒澤さん用カタログの棚を先に作るための素材として出します。特に今後は、モデル名より CLI・MCP・AGENTS.md・APIルーター・ローカル実行 が重要になります。

思考時間: 1m 16s
1. 結論

黒澤さんのAI個人カタログは、まずこの8系統から始めるのが良いです。

既存登録済み
- ChatGPT
- Claude
- Gemini
- DeepSeek
- Qwen
- Cursor
- GitHub Copilot
- Perplexity

ただし、今後のカタログでは サービス名だけでなく、技術カテゴリも別枠で持つべきです。
理由は、今後の差分が「モデル性能」よりも、CLI / ハーネス / MCP / APIルーター / ローカル実行 / エージェント運用に移っているためです。

2. 追加で書き出すべきAIサービス・技術
A. 大規模モデル・チャットAI系

まず、ChatGPT / Claude / Gemini / DeepSeek / Qwen と同じ棚に入れる候補です。

名称	位置づけ
Grok / xAI	X連携、リアルタイム寄り、APIあり
Mistral / Le Chat / Mistral API	欧州系、商用API、オープンウェイト系も強い
Meta Llama	ローカル・OSS系の基準モデル
Cohere Command系	RAG、企業向け、長文・検索拡張用途
z.ai GLM	中国系オープンモデル、コード・長文文脈で話題
Moonshot Kimi	長文・中国系モデル枠
MiniMax	テキスト・音声・動画系も含む中国系AI
Tencent Hunyuan	中国大手モデル枠
Baidu ERNIE	中国大手モデル枠
Yi / 01.AI	オープンモデル系
Nous Research	OSS/研究者向けモデル系
Databricks DBRX系	企業データ基盤寄りモデル

xAIはGrok APIで reasoning・voice・vision・image/video などを掲げており、Mistralはモデル/API/コード支援を持ち、Meta Llamaは公式Hugging Face組織でモデル群を配布しています。CohereはCommand R/R+を長文・RAG・ツール利用向けに位置づけています。

B. コーディングエージェント / IDE / CLI系

黒澤さんのカタログでは、ここが最重要棚です。
ChatGPTやClaudeとは別に、Codex / Claude Code / Copilot Agent / Cursor / Devin系を独立管理した方がいいです。

名称	位置づけ
OpenAI Codex / Codex CLI	ChatGPT系のCLI/クラウド/VS Codeエージェント
Claude Code	Anthropic系のターミナル/IDE/ブラウザ対応コーディングエージェント
Devin	自律型ソフトウェアエンジニア系
Devin Desktop / Windsurf	Windsurf系IDEがDevin Desktop側へ統合・改名方向
Replit Agent	ブラウザIDE + アプリ生成
Sourcegraph Cody / Amp	大規模コードベース理解・企業コード検索寄り
Cline	VS Code拡張型OSSエージェント
Roo Code	Cline派生・エージェント型VS Code拡張
Aider	CLI型ペアプロ、Git差分運用と相性が良い
OpenCode	CLI/ターミナル派向けエージェント
OpenHands	OSS自律開発エージェント
Continue.dev	OSS補完・チャット・IDE連携
Tabnine	企業向けコード補完
JetBrains AI Assistant	JetBrains IDE利用者向け
Augment Code	大規模コードベース文脈・企業開発向け
Factory AI / Droid系	コーディングエージェント運用系
Zed AI	高速エディタ + AI補助

Codex CLIはローカル端末でコードを読み、変更し、実行できるRust製オープンソースのコーディングエージェントとして説明されています。Claude Codeもコードベースを読み取り、ファイル編集・コマンド実行・開発ツール統合を行うエージェント型ツールです。

GitHub CopilotはMCPサーバーをリポジトリに設定でき、Copilot cloud agentやコードレビューが外部ツール・データソースへアクセスできます。Windsurf/Codeium側はDevin Desktopへの移行・統合を案内しており、Cascadeによる自律的な複数ファイル編集・コマンド実行が特徴です。

C. ノーコード / アプリ生成 / UI生成系

これは「プログラム生成」と似ていますが、人間がコードを書く前に画面やMVPを作る棚です。

名称	位置づけ
Vercel v0	UI/React/Next.js生成
Lovable	自然言語からWebアプリ生成
Bolt.new / StackBlitz	ブラウザ上でアプリ生成・編集
Replit Agent	アプリ生成・デプロイまで一体型
Firebase Studio	Google/Firebase系アプリ生成
Base44	ノーコード/AIアプリ生成
Tempo	UI生成・フロントエンド寄り
Framer AI	Webサイト生成
Webflow AI	ノーコードWeb制作
Create.xyz	プロトタイプ生成

黒澤さん用途では、これは本命開発環境ではなく、講座用デモ・MVP叩き台・UI案の高速生成としてカタログ化するのが良いです。

D. 検索 / 調査 / リサーチAI系

Perplexityの横に置く棚です。

名称	位置づけ
Genspark	AI検索・調査・ページ生成系
You.com	検索AI・チャット検索
Phind	開発者向け検索・技術調査
Consensus	論文・研究検索
Elicit	論文レビュー・研究支援
SciSpace	論文読解・要約
NotebookLM	手元資料・PDF・ノートを使う調査AI
Tavily API	AIエージェント向け検索API
Exa.ai	セマンティック検索API
Firecrawl	Webクロール・LLM向け抽出
Linkup	エージェント向けWeb検索API
Kagi Assistant	検索品質重視のAI検索

この棚は、トレード・世界情勢・AIニュース・技術調査で重要です。
ポイントは 「チャットAI」ではなく「出典取得エンジン」として評価することです。

E. APIルーター / 推論基盤 / モデルホスティング系

これは黒澤さんの自作AIルーター構想に直結します。

名称	位置づけ
OpenRouter	複数モデルAPIを一つの入口で使う
GroqCloud	高速推論
Together AI	OSSモデルのサーバーレス推論・学習
Fireworks AI	OSSモデルの高速推論・ファインチューニング
Replicate	画像・動画・音声・LLMモデル実行
Hugging Face Inference Providers	モデル配布・推論・Spaces
Baseten	モデルデプロイ基盤
Modal	Python/AIワークロード実行基盤
Lambda Labs	GPUクラウド
CoreWeave	GPUクラウド
Cerebras Inference	超高速推論系
NVIDIA NIM	NVIDIA系推論・企業導入
AWS Bedrock	AWS上のマルチモデル基盤
Azure AI Foundry	Microsoft/Azure AI基盤
Google Vertex AI	Google Cloud AI基盤
Cloudflare Workers AI	エッジ推論・軽量AI

Together AIはOSSモデルをオンデマンドで実行できるAIクラウド、Fireworks AIはOSS LLMや画像モデルの高速推論・ファインチューニング基盤として説明されています。

F. ローカルLLM / OSS実行環境系

「無料」「ローカル」「秘匿」「検証」の棚です。

名称	位置づけ
Ollama	ローカルLLM実行の定番
LM Studio	GUIでローカルモデル実行
llama.cpp	軽量ローカル推論の基礎技術
vLLM	高速サーバー推論
SGLang	推論最適化・エージェント実行
Text Generation Inference / TGI	Hugging Face系推論サーバー
MLX / MLX-LM	Apple Silicon向けローカル推論
KoboldCpp	ローカルLLM実行
GPT4All	ローカルAIアプリ
LocalAI	OpenAI互換ローカルAPI
Open WebUI	ローカル/自前LLM用Web UI
Jan	ローカルAIアシスタント
AnythingLLM	ローカルRAG/ワークスペース

この棚は、すぐ収益化というより 保険・検証・機密処理・低コスト大量処理 のために持つ価値があります。

G. エージェント基盤 / ハーネス / 標準技術系

ここは黒澤さんの「AIカタログ」の中核です。
サービス名より重要です。

技術	位置づけ
MCP / Model Context Protocol	AIと外部ツール・DB・APIを接続する標準
AGENTS.md	リポジトリ内でAIエージェントに指示を渡す標準ファイル
Claude Skills	Claude Code/Claude用のタスク別能力拡張
Codex Agent Skills	Codex用のタスク別ワークフロー拡張
OpenAI Agents SDK	エージェント、ツール、ハンドオフ、状態管理
LangChain	LLMアプリ/ツール連携フレームワーク
LangGraph	状態を持つ長時間エージェント・ワークフロー
LlamaIndex	RAG、文書検索、データ接続、エージェント
CrewAI	複数エージェントの役割分担・チーム化
AutoGen	Microsoft系マルチエージェント研究/実装
Semantic Kernel	Microsoft系AIオーケストレーション
Haystack	RAG/検索アプリ基盤
DSPy	プロンプト/パイプライン最適化
Pydantic AI	Python型安全エージェント
Mastra	TypeScript系エージェントフレームワーク
Composio	エージェント用ツール統合
Zapier MCP / Zapier AI Actions	SaaS操作自動化
Browser-use	ブラウザ操作エージェント
Playwright MCP	ブラウザ自動操作をAIに渡す
Computer Use	画面操作型エージェント技術

MCPはAIアプリを外部システムへ接続するオープン標準で、ClaudeやChatGPTがファイル・DB・検索・ワークフローなどに接続する「USB-C」のようなものとして説明されています。CodexはAGENTS.mdを読み、グローバル指示とプロジェクト固有指示を重ねられる設計です。

OpenAI Agents SDKは、エージェント、ツール、ハンドオフ、ガードレール、状態管理をコードで扱うためのSDKです。LangGraphは状態を持つ長時間エージェントや人間承認を含む実行に向き、LlamaIndexはRAGパイプラインをツールとして使うエージェント構築に使えます。

CrewAIは、複数エージェントを役割ごとに編成してフローを組むためのフレームワークとして説明されています。

H. RAG / ベクトルDB / ナレッジ管理系

黒澤さんの「What / Why DB」「AI講座」「業務委託営業資料」「ニュース監視」に直結します。

名称	位置づけ
Pinecone	マネージドベクトルDB
Weaviate	OSS/マネージドベクトルDB
Qdrant	Rust製ベクトルDB
Milvus / Zilliz	大規模ベクトルDB
Chroma	ローカル/軽量RAG
pgvector	PostgreSQL拡張でベクトル検索
LanceDB	ローカル/組み込み系ベクトルDB
Elasticsearch Vector Search	既存検索基盤拡張
OpenSearch Vector Engine	AWS/OpenSearch系
GraphRAG	グラフ構造を使うRAG
Knowledge Graph RAG	エンティティ関係を使うRAG
Reranker	検索結果の再順位付け
Hybrid Search	キーワード検索 + ベクトル検索
Embedding Model	文書・コード・ニュースのベクトル化

ここはAIサービスというより、自分の情報資産をAIで使える形にする基盤です。

I. 画像生成 / デザイン系

プレゼン・YouTubeスライド・講座素材で重要です。

名称	位置づけ
Midjourney	高品質イメージ生成
DALL·E / GPT Image	ChatGPT連携の画像生成
Ideogram	文字入り画像・ポスター系
Leonardo AI	画像生成・素材制作
Stable Diffusion / SDXL / Flux	OSS/ローカル画像生成
Black Forest Labs Flux	高品質OSS/商用画像生成
Adobe Firefly	商用デザイン・Adobe連携
Canva AI	Canva内AIデザイン
Krea AI	リアルタイム画像生成・補正
Magnific AI	画像アップスケール
Freepik AI	素材・画像生成
Recraft	ベクター/ブランド素材生成

Midjourneyは画像・動画生成のクリエイティブツールとして公式ドキュメントを持ち、Adobe/Canva系とは別に「絵作り特化」の棚で管理する価値があります。

J. 動画生成 / 動画編集AI系

YouTubeスライド、講座、SNS短尺に直結する棚です。

名称	位置づけ
Sora	OpenAI系動画生成
Google Veo	Google/DeepMind系動画生成
Runway Gen系	動画生成・編集・映画的表現
Luma Dream Machine	テキスト/画像から動画生成
Pika	動画生成・編集
Kling	中国系動画生成
Hailuo / MiniMax Video	中国系動画生成
PixVerse	AI動画生成
Haiper	AI動画生成
Higgsfield	SNS動画・人物演出系
HeyGen	アバター動画・翻訳動画
Synthesia	企業向けアバター動画
D-ID	顔アニメーション・アバター
Descript	動画/音声編集AI
CapCut AI	SNS動画編集
Filmora AI	一般向け動画編集AI

OpenAIはSoraを動画生成モデルとして説明し、GoogleはVeo 3.1を高品質動画生成・ネイティブ音声つきモデルとして提供しています。Runway Gen-4/4.5は、キャラクターやシーンの一貫性・映像制御を強調しています。

K. 音声 / 音楽 / ナレーション系

AI講座やYouTube素材にかなり使える棚です。

名称	位置づけ
ElevenLabs	音声合成・音声複製・吹替・音声エージェント
Suno	音楽生成
Udio	音楽生成
Mubert	BGM生成
Stable Audio	音楽・効果音生成
AIVA	作曲AI
Speechify	読み上げ
Murf AI	ナレーション
PlayHT	音声合成
Resemble AI	音声複製・音声変換
Deepgram	音声認識API
AssemblyAI	音声認識・要約API
Whisper / Whisper API	音声文字起こし
Cartesia	低遅延TTS/音声エージェント
Hume AI	感情・音声AI

ElevenLabsはTTS、STT、音声複製、会話エージェント、生成音声インフラを提供しており、APIもあります。

L. プレゼン / ドキュメント / オフィスAI系

黒澤さんの講座・営業資料・PM資料に直結します。

名称	位置づけ
Gamma	AIスライド生成
Tome	プレゼン生成
Beautiful.ai	プレゼン自動デザイン
Canva AI	デザイン・スライド
Microsoft Copilot for Microsoft 365	Word/Excel/PowerPoint/Outlook連携
Google Workspace Gemini	Docs/Sheets/Slides/Gmail連携
Notion AI	ナレッジ・議事録・文章
Coda AI	ドキュメント/業務DB
Mem AI	個人ナレッジ
Craft AI	文書作成
Grammarly	英文・文章補正
DeepL Write / DeepL Pro	翻訳・文章補正
Napkin AI	図解生成
Whimsical AI	図解・フローチャート
Miro AI	ホワイトボード・企画整理
FigJam AI	デザイン/企画ボード

ここは「AIモデル」ではなく、成果物生成AIとして別棚にした方が管理しやすいです。

M. PM / コンサル / 業務自動化系

コンサルPMリーダー業務に効く棚です。

名称	位置づけ
Notion AI	ナレッジ・議事録・タスク整理
Linear AI	Issue/開発管理
Jira AI / Atlassian Intelligence	チケット・プロジェクト管理
ClickUp AI	タスク管理
Asana Intelligence	PM補助
Slack AI	会話検索・要約
Microsoft Teams Copilot	会議要約・アクション整理
Fathom	会議録画・要約
Fireflies.ai	会議文字起こし
tl;dv	会議録画・要約
Otter.ai	議事録
Zapier AI	SaaS自動化
Make AI	ワークフロー自動化
n8n + AI nodes	自前ワークフロー自動化
Dify	AIアプリ/ワークフロー構築
Flowise	ノーコードLLMフロー
Langflow	LLMフロー構築

黒澤さんの場合、ここは「便利ツール」ではなく、顧問・PM・業務委託営業体制の再現性を高める棚です。

N. ブラウザ操作 / 自律実行 / PC操作系

今後かなり重要になる棚です。

名称	位置づけ
Manus系AI	自律タスク実行AIの代表格
OpenAI Operator / Computer Use系	ブラウザ・PC操作
Anthropic Computer Use	画面操作型エージェント
Browser-use	OSSブラウザ操作エージェント
Stagehand	AIブラウザ自動化
Playwright MCP	ブラウザ操作をAIに渡す
MultiOn	ブラウザ自動操作
Adept系	PC操作AIの系譜
Rabbit / device agent系	デバイス操作AI

ここは危険も大きいです。
ログ、権限、支払い操作禁止、確認フローが必須です。

O. AI評価 / 監視 / セキュリティ / ガバナンス系

ハーネスを成長させるなら、ここを後回しにしない方がいいです。

名称	位置づけ
LangSmith	LangChain/LangGraph系のトレース・評価
Helicone	LLM APIログ・コスト監視
Langfuse	OSS LLM Observability
Arize Phoenix	LLM評価・観測
Weights & Biases Weave	LLMアプリ評価
Promptfoo	プロンプト/LLMテスト
OpenAI Evals	評価基盤
Ragas	RAG評価
Giskard	AIテスト・リスク評価
TruLens	RAG/LLM評価
Guardrails AI	出力制御・検証
Lakera	Prompt Injection対策
Protect AI	AIセキュリティ
HiddenLayer	AIモデル防御
Lasso Security	LLMアプリセキュリティ
Aporia	AIガードレール
Humanloop	プロンプト管理・評価

AIを使うだけなら不要ですが、自作エージェント・顧客向けAI基盤・業務自動化に行くなら必須棚です。

3. 有力シナリオ

黒澤さんのカタログは、最終的にこういう分類に育てるのが良いです。

AI個人カタログ
├── 01_基盤モデル
├── 02_チャットAI
├── 03_検索・リサーチAI
├── 04_コーディングエージェント
├── 05_CLI・IDE・ハーネス
├── 06_APIルーター・推論基盤
├── 07_ローカルLLM
├── 08_RAG・ナレッジDB
├── 09_画像生成
├── 10_動画生成
├── 11_音声・音楽
├── 12_プレゼン・資料
├── 13_PM・業務自動化
├── 14_ブラウザ操作・自律実行
├── 15_評価・監視・セキュリティ
└── 16_トレード調査・市場分析

この構造にすれば、AIサービスが50個、100個に増えても破綻しません。

4. 破綻条件

一番まずいのは、こういう一覧にすることです。

ChatGPT
Claude
Gemini
DeepSeek
Qwen
Cursor
Copilot
Perplexity
Grok
Mistral
...

これは増えた瞬間に崩れます。

正しくは、

サービス名
用途
入力データ
API
CLI
MCP
AGENTS.md
ローカル可否
無料枠
有料枠
ハーネス適性
実験ログ
黒澤用途での勝ち筋

で管理することです。

特に破綻しやすいのは、コーディングAIを全部「コード生成」として一括りにすることです。
実際には、

補完
チャット
差分修正
CLI実行
リポジトリ全体理解
Issue駆動
PR作成
レビュー
テスト生成
ドキュメント更新
MCP接続

で全然違います。

5. 実務・行動への影響

まず、次に追加するカタログ候補はこのあたりが優先です。

最優先追加
- Codex / Codex CLI
- Claude Code
- Devin / Devin Desktop / Windsurf
- Cline
- Aider
- OpenCode
- OpenRouter
- GroqCloud
- Together AI
- Fireworks AI
- Ollama
- LM Studio
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
- ElevenLabs
- Suno
- Gamma
- NotebookLM
- Tavily
- Exa
- Firecrawl
- Langfuse
- Helicone
- Promptfoo

黒澤さん向けに、特に価値が高いのはこの5分類です。

1. CLI/ハーネス系
   Codex / Claude Code / Cline / Aider / OpenCode

2. APIルーター系
   OpenRouter / Groq / Together / Fireworks

3. RAG・ナレッジ系
   LlamaIndex / pgvector / Qdrant / GraphRAG

4. 調査・ニュース系
   Perplexity / NotebookLM / Tavily / Exa / Firecrawl

5. 講座・発信系
   Gamma / Midjourney / Sora / Veo / Runway / ElevenLabs / Suno

この方向で作ると、AIサービスが乱立しても「増えて困る」ではなく、黒澤さん専用のAI武器庫が育つ形になります。
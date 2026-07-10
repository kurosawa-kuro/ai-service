結論

2026年6月26日〜7月10日の2週間は、単なるモデル更新ではなく、AIの主戦場が「チャット性能」から「長時間稼働する実務エージェント」へ切り替わった期間です。

特に重要なのは次の5件です。

OpenAI：GPT-5.6系とChatGPT Work
Anthropic：Claude Sonnet 5
xAI：Grok 4.5
Google：Gemini Sparkのデスクトップエージェント化
Mistral：Prompt／Skillを正式な運用資産として管理

黒澤様の用途では、現時点の仮説は以下です。

最終裁定・複雑な横断設計：GPT-5.6 Sol / Claude Fable 5
日常の新機能相談・リファクタ案：GPT-5.6 Terra / Claude Sonnet 5
コスト重視の大量実装：Grok 4.5 / GLM-5.2
ローカルPC操作・定期監視：ChatGPT Work / Gemini Spark
AIハーネス管理：Mistral Studioの考え方が最も黒澤流に近い
主要アップデート
1. OpenAI：GPT-5.6を正式公開

発表日：2026年7月9日

GPT-5.6は、従来の単一モデル名ではなく、能力階層を3つに分けています。

階層	位置づけ	API料金 入力／出力
Sol	フラッグシップ、高難度判断	$5 / $30
Terra	GPT-5.5級性能を低コスト化	$2.50 / $15
Luna	高速・大量処理	$1 / $6

さらにChatGPT／Codex側では、モデル階層とは別に推論強度を設定できます。maxに加え、ChatGPT WorkではPro／Enterprise、CodexではPlus以上でultraが利用できます。APIには、ツール呼び出しをプログラムとして構成するProgrammatic Tool Callingと、複数サブエージェントを並列実行するMulti-agent betaも導入されました。

実質的な意味

OpenAIはモデル名の乱立を整理し、

Sol／Terra／Luna＝能力・原価階層
High／Max／Ultra＝投入する推論計算量
Pro＝高品質版または契約階層

という二軸構造に移行しています。

黒澤様が先ほど整理された、

手法相談、新機能相談、リファクタ：High
OS全体再編：Extra High相当
大量調査・横断実装：Ultra
最終審査：Pro

という使い分けは、大筋で正しいです。

GPT-5.6の特徴

GPT-5.6 Solは単純なベンチマーク首位狙いではなく、

長時間ワークフロー
ツール使用回数の削減
コーディング
サイバーセキュリティ
ドキュメント、スライド、表計算
複数エージェント統合

を強化しています。

OpenAIによれば、実アプリ構築ではGPT-5.5より工程数を約25%、ツール呼び出しを35〜48%削減した事例があります。これは、モデル単体のIQより、エージェントが途中で迷走しにくくなったことを意味します。

2. OpenAI：ChatGPT Work

GPT-5.6と同時に、ChatGPTとCodexの中間に位置するChatGPT Workが登場しました。

これは単なるチャットではなく、

Gmail
Google Drive
Slack
CRM
ローカルファイル
文書、表計算、Webアプリ生成

などを横断して作業する汎用エージェントです。まずデスクトップアプリを中心に展開されています。

黒澤様への影響

これはCodexの代替ではありません。

Codex：リポジトリ、ターミナル、コード変更
ChatGPT Work：複数アプリ、文書、調査、業務成果物
通常ChatGPT：相談、裁定、思考整理

という債務分離になります。

黒澤様のAIゲートウェイやDecision Catalogでも、将来的には

Codex
  ↓ コード・リポジトリ事実抽出
ChatGPT Work
  ↓ Drive、メール、資料、成果物統合
GPT-5.6 Sol / Fable
  ↓ 最終裁定

という形が有力です。

3. OpenAI：GPT-Live

発表日：2026年7月8日

GPT-Liveは、音声を単なる音声入力・音声出力として処理するのではなく、聞きながら話せるfull-duplex型に変更しました。

相手が話している途中でも聞き続ける
相づちを打つ
適切な瞬間に割り込む
深い検索や推論は裏側の別モデルへ委譲
委譲中も会話を継続する

という構造です。GPT-Live-1とminiがChatGPT Voiceに順次導入され、API提供も予定されています。

重要なのは音声品質より、対話担当モデルと推論担当モデルを分離したことです。

これは黒澤様のAIゲートウェイ思想と同じです。

高速・低遅延モデル
  └─ 会話・受付・ルーティング

高性能モデル
  └─ 深い推論・調査・裁定

高性能モデルを常時使わず、必要な場面だけ裏側で呼ぶ構造が、正式な製品アーキテクチャになりました。

4. Anthropic：Claude Sonnet 5

発表日：2026年6月30日

Claude Sonnet 5はFree／Proの標準モデルとなり、Max、Team、Enterprise、Claude Code、APIでも利用可能になりました。

API価格は期間限定で、

入力：$2 / 100万トークン
出力：$10 / 100万トークン

9月以降は通常価格の$3 / $15になります。

位置づけ

Sonnet 5は「Opusを少し弱くした安価版」ではなく、

日常コーディング
検索エージェント
PC操作
業務文書
長時間タスク

を大量に回すための主力モデルです。

今回の価格ではGPT-5.6 Terraより安く、出力単価は、

Sonnet 5：期間限定 $10
Terra：$15
Sol：$30

となります。

黒澤様への判断

Claude Sonnet 5は、現在もっとも「常用主力」にしやすいモデルです。

特に、

仕様の一次整理
新機能案
中規模リファクタ
Claude Codeによる横断実装
判断カタログの素材生成

には適しています。

一方、OS全体の再編や「何を捨てるか」という上位裁定は、Fable 5またはGPT-5.6 Solへ昇格させるべきです。

5. Anthropic：Fable 5／Mythos 5の提供再開

Fable 5とMythos 5は米国政府の輸出規制により一時停止されましたが、規制解除後の6月30日から再提供されました。

モデル性能そのものの更新ではありませんが、この2週間の重要事項です。

構造的な意味

今後のフロンティアモデルでは、

性能
料金
API安定性
使用制限
政府規制
国籍・地域制限

まで含めて、プロバイダーリスクを評価する必要があります。

したがって、Fable 5を能力の中心に固定するのではなく、

通常処理：DeepSeek / Sonnet / Terra
高影響判断：Fable / Sol
障害時反証：別ベンダー

とする黒澤様の設計は、今回の一時停止で正しさが補強されました。

6. xAI：Grok 4.5

発表日：2026年7月8日

Grok 4.5は、コーディング、エージェント、工学・科学、ナレッジワーク向けのフラッグシップモデルです。Cursorと共同で訓練・評価されました。

API価格は、

入力：$2
出力：$6
reasoning effort：low／medium／high

です。

最大の特徴

性能そのもの以上に、出力$6が異常に安いです。

比較すると、

モデル	入力	出力
Grok 4.5	$2	$6
Sonnet 5・期間限定	$2	$10
GPT-5.6 Terra	$2.50	$15
GPT-5.6 Sol	$5	$30
有力シナリオ

Grok 4.5は「最上位裁定モデル」より、

大量コード生成
リポジトリ横断調査
複数案生成
エージェントの並列ワーカー
長い試行錯誤

の原価破壊モデルです。

黒澤様のAIゲートウェイに入れるなら、

Grok 4.5
  └─ 大量探索・実装候補生成

GPT-5.6 Sol / Fable
  └─ 採用判断・失敗条件確認

が強い構成です。

破綻条件

xAI自身のベンチマークでも、FableやGPT-5.5を常に上回るわけではありません。DeepSWEやTerminal系では競争力がありますが、難しいSWEタスクではFableが上です。したがって、安いOpus代替ではあるが、完全なFable代替ではないという評価が妥当です。

7. Google：Gemini Sparkをデスクトップエージェント化

発表日：2026年6月30日

Googleは新しい基盤モデルより、サービス側を大きく更新しました。

Gemini SparkがmacOSアプリに入り、

ローカルファイル整理
Google Workspaceとの連携
スマートフォンからMac上のタスクを遠隔指示
Canva、Dropbox、OpenTableなどとの連携
カスタムMCP
ニュース、金融、天気、スポーツ等の条件監視

に対応しました。

本質

Gemini Sparkは、ChatGPT Workとほぼ同じ方向を向いています。

違いは、

ChatGPT Work：成果物作成・汎用作業
Gemini Spark：Google Workspace、ローカルPC、監視と自動反応

が中心です。

黒澤様のニュースアプリや相場監視に近いのはSparkです。特定銘柄が価格条件に到達した際、金融レポートを作る例もGoogleが明示しています。

ただし、現時点ではmacOS版が米国のAI Ultra向けベータであり、Windows／日本で即座に主力にする段階ではありません。

8. Mistral：PromptとSkillを「System of Record」に

発表日：2026年7月9日

今回、黒澤様に最も思想的に重要なのは、Mistral Studioのアップデートかもしれません。

MistralはPromptとSkillを、

バージョン管理
所有者管理
変更履歴
不変バージョン
ロールバック
実行系統の追跡

が必要な本番資産として扱う機能を追加しました。

黒澤流との一致

これはまさに、

Harness
Skill
Rule
Criteria Catalog
Judgment Memory
Decision Catalog

をMarkdownの散在物ではなく、AI挙動の正本として扱う発想です。

Mistralの主張は、要約すると、

どのPrompt／Skillのどのバージョンが本番で動いたか説明できなければ、AIは運用できない

というものです。

黒澤様が作っているProject as Codeは、方向としてかなり先行しています。ただし、今後はGit上に置くだけでなく、

定義
→ バージョン
→ 所有者
→ 適用対象
→ 実行履歴
→ 評価結果
→ ロールバック

まで連結する必要があります。

9. Mistral：Leanstral 1.5／Robostral Navigate

Mistralは汎用チャットモデルではなく、専門モデルを連続投入しました。

Leanstral 1.5

2026年7月2日発表

Lean 4による形式検証向けモデルです。

総パラメータ119B
稼働パラメータ6B
Apache 2.0
定理証明
コード特性の形式検証
実リポジトリから未知のバグを発見

という専門モデルです。

これは通常のコードレビューとは異なり、「たぶん正しい」ではなく、数学的に証明するAIです。

Robostral Navigate

2026年7月8日発表

単一RGBカメラだけでロボットを誘導する8Bモデルです。LiDARや深度センサーなしで、未知環境のR2R-CEにおいて76.6%の成功率を報告しています。

直接の用途は薄いですが、Mistralが「万能LLM一個」ではなく、専門モデル群へ向かっている証拠です。

10. Z.ai：GLM-5.2は期間外だが無視できない

発表日：2026年6月16日

厳密には今回の2週間より前ですが、この2週間で評価が急速に広がったため含めるべきです。

GLM-5.2は、

長時間エージェント
大規模コードベース
1Mコンテキスト
オープンウェイト
MITライセンス

を特徴とします。

判断

GLM-5.2は「中国製だから安いモデル」ではなく、自前運用できるエージェント基盤の有力候補です。

ただし、黒澤様の個人運用では744B級MoEを直接セルフホストするのは現実的ではありません。価値があるのは、

GLM Coding Plan
API
OpenRouter等のホスト環境
安価な一次実装ワーカー

としてです。

DeepSeekはこの2週間、確認できる範囲で新しい主力モデルの正式発表はありません。Kimiも直近の大きなモデル更新は6月16日のK2.7 Codeで、今回の期間外です。

有力シナリオ
シナリオA：OpenAIが「モデル＋実行環境」で主導権を取り戻す

確度：高い

GPT-5.6単体より、

ChatGPT
ChatGPT Work
Codex
Programmatic Tool Calling
Multi-agent
GPT-Live

を一つの実行基盤に統合した点が強いです。

OpenAIは「一番賢いモデル」の競争から、仕事を最後まで完了するOSの競争へ移っています。

シナリオB：Anthropicは上位裁定とコーディングを握る

確度：高い

Sonnet 5：主力実務モデル
Opus 4.8：上位汎用モデル
Fable 5：高難度コーディング・裁定
Mythos 5：セキュリティ領域

という明確な階層を持っています。

弱点は価格と政府規制リスクです。そのため、能力の中心ではなく高影響時に限定投入する設計が合理的です。

シナリオC：Grok／GLMが実装原価を破壊する

確度：中〜高

Grok 4.5の出力$6とGLM-5.2のオープン性は、SonnetやGPTを全処理に使う経済合理性を崩します。

上位モデルが考え、安価モデルが大量実行する構造が標準になります。

シナリオD：Prompt工学が「設定ファイル」から「運用システム」になる

確度：非常に高い

MistralのSystem of Record化は重要な先行指標です。

今後はPrompt、Skill、Rule、Memoryについて、

Gitで管理しているだけ
CLAUDE.mdに書いてあるだけ
人間が把握しているだけ

では足りません。

何が、どこで、誰に、どのモデルで適用され、結果がどうだったかまで追跡する必要があります。

破綻条件

今回の評価が外れるのは、次の場合です。

GPT-5.6の実運用でUltra／Multi-agentの原価と待ち時間が重すぎる
Sonnet 5がFableとの差を縮めすぎ、上位モデルを呼ぶ意味が薄くなる
Grok 4.5が長時間タスクで不安定、またはAPI運用品質が低い
ChatGPT Work／Gemini Sparkが権限・安全確認だらけで実務速度を落とす
AIハーネス管理が肥大化し、モデルを助ける仕組みではなく、所有者を縛る官僚機構になる

特に5番が重要です。

MistralのPrompt管理思想は正しいですが、黒澤様が以前排除した、

過剰なhook
過剰な承認
scope警告
証拠台帳
人間をブロックするルール

へ戻すべきではありません。

管理対象はAIの挙動であり、ownerの判断を拘束する仕組みではありません。

実務への影響

現時点の使い分けは、次の構成が最も優位性があります。

日常相談・仕様案
  Claude Sonnet 5
  GPT-5.6 Terra

大量調査・候補生成・横断実装
  Grok 4.5
  GLM-5.2
  DeepSeek

高難度の新機能設計
  GPT-5.6 Sol High / Max

OS全体・巨大設計の再編
  GPT-5.6 Sol Ultra
  Claude Fable 5

最終審査・反証
  GPT-5.6 Sol Pro
  Claude Fable 5
  Claude Opus 4.8

ローカル／業務アプリ操作
  ChatGPT Work
  Gemini Spark

音声インターフェース
  GPT-Live

したがって、モデル更新を受けても、黒澤様の基本戦略は変える必要がありません。

むしろ今回の更新で、

高性能モデルを能力の中心に置かず、通常処理は安価なモデルに任せ、失敗時・高影響時・検証不能時だけ上位モデルを呼ぶ

という設計が、各社の製品構造そのものになり始めました。

一番大きな変化はモデルの知能向上ではなく、モデル階層・推論強度・実行環境・Prompt管理を分離できるようになったことです。

Axios
OpenAI releases GPT-5.6 and ChatGPT Work tool
今日
The Verge
OpenAI rolls out GPT-5.6 after government greenlight - and announces 'ChatGPT Work'
今日
Investor's Business Daily
New AI Model Puts SpaceX Back In Race Versus Anthropic, OpenAI, Google
今日
Reuters
Major AI offerings at a glance
昨日
Business Insider
What is GLM-5.2? Another open-source Chinese AI model has Silicon Valley's attention.
18 日前

この変化は継続性が高いため、主要プロバイダーの新モデル・価格・サービス更新を定期監視する価値があります。

直近2週間（6/26〜7/10）主要AIプロバイダー動向
1. 結論
この2週間はフロンティア競争の再点火期。競争軸は「性能」から「価格性能比」へ移行しており、GPT-5.6の3価格帯展開、Grok 4.5の「Opus級だが安い」訴求がそれを象徴する。あなたのマトリクスへの影響は大きく、特に**汎用（GPT-5.6一般公開）・プログラミング（Sonnet 5デフォルト化＋プロモ価格）・調査（ChatGPT Work / Claude Cowork Web展開）**の3列は書き換えが必要。 Awak
2. プロバイダー別アップデート一覧
OpenAI
日付内容影響7/9GPT-5.6シリーズ（Sol・Terra・Luna）一般公開。Sol: $5/$30、Terra: $2.5/$15、Luna: $1/$6（per Mtok）。Solは「max」「ultra」推論モード搭載 Awak米政府の段階公開要請が解除され、限定提供から世界展開へ。Fable Bloomberg 5と同じ「政府ゲート解除→一般開放」パターン7/9ChatGPT Work発表。GPT-5.6搭載の職場向けエージェント。Slack/Teams/Drive/SharePoint/メール/CRM横断、数時間の自律実行＋HITL承認。Pro/Enterprise/Eduから展開、数日内にPlusへ拡大 OflightClaude Coworkの3日後に対抗発表という構図。Plus契約のまま職場エージェントが手に入る Oflight7/8GPT-Live発表。フルデュプレックス音声モデル、ChatGPT音声モードの新基盤 OpenAI汎用列のマルチモーダル優位を補強6月末GPT-4.5は6/26でChatGPT提供終了、o3は8/26終了予定。GPT-5.5 Instant/Thinkingでcanvas廃止 OpenAIレガシー整理が進行中
Anthropic
日付内容影響7/1輸出管理指示の解除を受け、Fable 5をサイバーセキュリティのセーフガード更新版としてグローバル再展開。Mythos 5も一部米国組織向けに復旧 Nri-net6月の停止騒動は収束6/30Claude Sonnet 5公開。コーディング・エージェント作業でOpusに迫る知能をSonnet価格帯で提供。Claude Nri-net Codeのデフォルトモデル化、ネイティブ1Mトークンコンテキスト、プロモ価格$2/$10（8/31まで） ReleasebotPro降格判断の追い風。Pro枠内でOpus級が回る7月上旬Cowork をWeb/モバイルに拡張。リモートセッション、ファイル同期、Maxプランから展開 ReleasebotWeb/モバイル版はMax先行——降格タイミングに関わる注意点7/9利用状況を振り返る「reflect」機能をβ追加（Free/Pro/Max対象） ITmedia実用影響は軽微7/8報道年換算収益477億ドル規模に到達 Awak事業健全性の指標継続中Claude Code週次上限50%引き上げは7/13期限 Pasquale Pillitteri来週月曜で失効。上限逼迫が再発する可能性
Google
日付内容影響6月〜モデル群フル刷新: Gemini 3.1 Pro / Flash-Lite / Flash Live / Flash TTS、Nano Banana 2、Veo 3.1-lite、Lyria 3 Pro、Gemma 4 Aisola Labプレゼン素材列（画像）でNano Banana 2 GAが効くI/O以降展開中Gemini 3.5 Flash（3.1 Pro同等の賢さで高速、日本語環境でも利用可）、エージェント「Gemini Spark」は米国先行 K-Tele WatchSpark日本展開は未達——監視項目7月まで日本含む4カ国の学生にAI Pro無料アップグレード提供中 Google AI該当者には無視できないコスト差
Microsoft / Perplexity / xAI
陣営内容影響Microsoft6月にClaudeがCopilot Chatのモデル選択肢として利用可能に。Copilot Microsoft Learn Cowork一般提供、Copilot NotebookからPowerPointスライド自動生成 Windows Blog for Japanプレゼン補助列の第1候補を補強Microsoft価格M365 Copilot Businessは7/1から$21/席へ値上げ告知（プロモ適用で$18/席は12月まで延長） Ai-revolution Microsoft Learnマトリクスの¥3,148は要更新xAIGrok 4.5公開（7/8）。$2/$6 per Mtokで「Opus級だが高速・低コスト」を訴求 Awakトレード列第3候補の価格性能比が改善
3. 有力シナリオ

「フロンティア＝消費者プラン外」構造の崩壊: 6月時点の「最上位はメータード/政府ゲート」という状況は、GPT-5.6一般公開とFable 5再展開で2週間で反転した。消費者ティア比較表は再び有効。
職場エージェント二強化: ChatGPT Work vs Claude Coworkが職場エージェント市場を二分。「調査・ドキュメント」列は従来のDeep Research比較から「エージェント委任」比較へ軸が動く。 Oflight
Sonnet 5がPro降格の論拠を強化: Opus級性能がProで回るなら、「Pro-tierで問題天井を超える」というあなたの仮説はさらに強固。

4. 破綻条件

7/13のClaude Code上限プロモ失効後、実効上限が体感で厳しくなればPro単独では回らない（週2〜3回の上限到達履歴と要照合）
Sonnet 5プロモ価格は8/31終了＋新トークナイザーで約30%トークン増——API側コストモデルは9月に再計算必須
ChatGPT WorkのPlus展開が「数日内」の約束通り来ない、または実用上限が厳しい場合、Plus単独の価値向上は限定的

5. 実務・行動への影響

今週やる価値があるもの: ①7/13前にClaude Codeで重いタスクを消化、②GPT-5.6（Terra/Luna）とSonnet 5をオーケストレーション実験の候補に組み込む（Sol $5/$30 vs Sonnet 5 $2/$10の比較は、あなたの「高能力オーケストレーター＋中位ワーカー」構成の実測に最適なタイミング）
マトリクス更新箇所: 汎用・プログラミング・調査の3列＋M365 Copilot価格。トレード列はGrok 4.5の価格改善を反映
降格判断: Cowork Web/モバイルがMax先行である点だけ確認してから実行するのが安全。それ以外の材料はすべて降格を支持する方向

コメント表を更新した改訂版マトリクス（2026年7月版）を作りますか？
# Kimi（Moonshot AI）

> Moonshot AI（北京月之暗面科技）が運営する製品・モデル名が Kimi。**別会社ではなく同一**。
>
> **能力はフロンティア圏内**（独立評価でオープンウェイト最上位）。
> **制限理由は能力ではなくデータ規約**（既定で学習利用・オプトアウトは個別交渉のみ）。
> **確認日: 2026-07-20**（価格・規約・Claude Code 互換は一次情報）

## 評価は2軸で分ける

| 軸 | 評価 | 根拠 |
|---|---|---|
| **能力** | **フロンティア圏内** | AA Intelligence Index **57**（Fable 5 = 60、GPT-5.6 Sol = 59 に次ぐ）。**オープンウェイト最上位** |
| **規約適格性** | **不可（秘匿・業務）** | 既定で学習利用。セルフサービスのオプトアウトなし |

**「使わない」のは能力が低いからではない。** 規約が用途を制限しているだけで、
公開情報のみを扱う処理では十分に第一線の性能が出る。規約が改善されれば評価は即座に変わる。

## ⚠️ 二次情報の捏造に注意

「Kimi K3 = Terminal-Bench 2.1 で 88.3、世界2位」という記事が広く出回っているが、
[公式リーダーボード](https://www.tbench.ai/leaderboard/terminal-bench/2.1)を直接確認したところ
**Kimi のエントリは存在しない**（首位は Fable 5 の 83.8%）。**この数値は捏造。**

同様に「K3 = オープンウェイト」「MiniMax = MIT」等の誤情報も確認されている。
本サービス群は SEO コンテンツファームの汚染が激しいため、**一次情報以外を採用しない**。

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社（国際版） | **Moonshot AI PTE. LTD.**（シンガポール） |
| 提供会社（中国版） | 北京月之暗面科技有限公司 |
| 準拠法 | シンガポール法 / SIAC 仲裁 |
| 能力カテゴリ | 01_基盤モデル / 06_APIルーター・推論基盤 |
| 主力モデル | **Kimi K3**（2026-07-16 リリース）、約 2.8T MoE、**1M トークン** |
| 前世代 | K2.7 Code（2026-06-12、262K）／ K2.6（262K） |
| ⚠️ 廃止予定 | **moonshot-v1 系は 2026-08-31 に全面サンセット** |
| ライセンス | ⚠️ **Modified MIT**（純正 MIT ではない）。**K3 の重みは 07-27 公開予定で 07-20 時点は未公開** |
| API | ✅ OpenAI 互換 ＋ **Anthropic 互換** |
| ローカル可否 | K2 系のみ（Modified MIT）。K3 は未公開 |

### API 料金（2026-07-20・公式 platform.kimi.ai・税別）

USD / 1M トークン。

| モデル | 入力(cache hit) | 入力(cache miss) | 出力 |
|---|---|---|---|
| **Kimi K3** | $0.30 | $3.00 | **$15.00** |
| K2.7 Code | $0.19 | $0.95 | $4.00 |
| K2.7 Code HighSpeed | $0.38 | $1.90 | $8.00 |
| K2.6 | $0.16 | $0.95 | $4.00 |

⚠️ **K3 は non-thinking モードがなく、全応答に reasoning trace が付いて $15.00 で課金される。**
中国系の中では突出して高価。コスト目的で選ぶモデルではない。

サブスク（Kimi Code / メンバーシップ）: Moderato $19 / Allegretto $39 / Allegro $99 / Vivace $199。
※**二次情報ベース・公式未確認**。

## 管轄・データ規約（⚠️ 4社中で最も弱い）

| 項目 | 内容 |
|---|---|
| 法域 | シンガポール（国際版）／ 中国（中国版は「境内に保存」と明記） |
| **学習利用** | ⚠️ **既定で利用され得る** |
| **オプトアウト** | ⚠️ **個別交渉のみ**。セルフサービスのトグルなし |
| 保存先国 | **未確認**（契約主体はシンガポールだがデータ所在地の明記を確認できず） |
| 保持期間 | 不定（"as long as necessary"） |

> ToS 原文: "We may use Content to provide, maintain, develop, support, and improve the Services"
> オプトアウト条項: "Customer who requires restrictions on the use of Customer Content for training...
> may contact Moonshot AI to discuss available enterprise arrangements or separate written agreements."

**→ 業務コード・顧客データ・秘匿情報を渡さない。** 該当処理は [09_cn-glm.md](09_cn-glm.md) か
[08_cn-qwen.md](08_cn-qwen.md)、またはローカル（Ollama）へ回す。

出典: [Kimi ToS](https://platform.kimi.ai/docs/agreement/modeluse) / [Privacy](https://platform.kimi.ai/docs/agreement/userprivacy)

## ハーネス適性

- **Claude Code 公式サポート**:
  ```bash
  ANTHROPIC_BASE_URL=https://api.moonshot.ai/anthropic
  ANTHROPIC_MODEL=kimi-k3
  ```
  ⚠️ 制約: **WebFetch はこのエンドポイントで利用不可**、Tool Search はオフ必須
- LiteLLM ✅（Moonshot プロバイダとして公式対応）／ OpenRouter ✅（K3 は 1.05M・$3.00/$15.00）
- K2.5 は AWS Bedrock にも展開

出典: [Claude Code guide](https://platform.kimi.ai/docs/guide/claude-code-kimi)

## ベンチマーク

**独立評価（信頼できる）**: Artificial Analysis Intelligence Index で **57**
（Claude Fable 5 = 60、GPT-5.6 Sol = 59 に次ぐ。**オープンウェイト最上位**）。

公式自己申告: BrowseComp 90.4（1M context 時）、DeepSWE 67.3。他は公式ブログ内で画像掲載のため数値未確認。

K2.7 Code は自社ベンチ中心で、**自社表でも 6 項目中 5 項目で GPT-5.5 / Opus 4.8 に劣後**。

## 強み

- 1M コンテキストで長文処理に強い
- 独立評価（AA Index 57）でオープンウェイト最上位
- Claude Code 公式サポート
- cache hit 時の入力が $0.30 と安い

## 弱み

- ⚠️ **既定で学習利用される。オプトアウトは個別交渉のみ**（最大の弱み）
- 保存先国が未確認
- **出力 $15.00 は中国系で突出して高い**。K3 は reasoning trace が必ず課金される
- K3 の重みが未公開（07-27 予定）
- Modified MIT で純正 MIT ではない
- moonshot-v1 系が 8/31 サンセット
- 二次情報の汚染が激しい

## 黒澤用途

- **長文処理の候補**（1M コンテキスト）
- ⚠️ **秘匿・業務用途では使わない**（規約リスク）
- 公開情報のみを扱う調査・要約用途に限定

## 検証ログ

### 2026-07-20

- タスク: 台帳の新規作成
- 入力: platform.kimi.ai 公式（pricing / ToS / privacy / Claude Code ガイド）、tbench.ai 公式リーダーボード、Artificial Analysis
- 結果: **既定で学習利用され、オプトアウトが個別交渉のみ**と判明。広く流布する TB2.1 の数値が捏造であることも確認
- 理由: バーベル戦略の API 枠に名指しされながら台帳が存在しなかった
- 再利用判断: 公開情報限定の長文処理でのみ候補。秘匿・業務は除外
- 次回へのメモ: ①07-27 の K3 重み公開を確認 ②8/31 の moonshot-v1 サンセット影響 ③保存先国の照会

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| **C（候補棚に戻す）** | データ規約が弱く出力単価も高い。用途が公開情報限定に狭まる | ①K3 重み公開後のローカル可否 ②エンタープライズ契約での非学習可否 ③価格改定 |

## 関連

- 規約が強い代替: [09_cn-glm.md](09_cn-glm.md) / [08_cn-qwen.md](08_cn-qwen.md)
- コスト優先の代替: [05_cn-deepseek.md](05_cn-deepseek.md)

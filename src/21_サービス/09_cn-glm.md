# z.ai / GLM（Zhipu AI）

> **中国系4社の中でデータ規約が最も強い。** API コンテンツを一切保存せず、学習にも使わないと契約で明記。
> 秘匿寄り処理で中国系を使うなら第一候補。**ただし親会社が米国 Entity List 掲載**（下記）。
> **確認日: 2026-07-20**（価格・規約・ライセンス・Claude Code 互換は一次情報）

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社（国際版） | **JINGSHENG HENGXING TECHNOLOGY PTE. LTD.**（シンガポール） |
| 提供会社（中国版） | 北京智谱华章科技（Beijing Zhipu Huazhang Technology）。2026-01-08 香港上場 (2513.HK) |
| 準拠法 | **シンガポール法 / SIAC 仲裁**（国際版 z.ai） |
| 能力カテゴリ | 01_基盤モデル / 04_コーディングエージェント / 06_APIルーター・推論基盤 |
| 主力モデル | **GLM-5.2**（Coding Plan 先行 2026-06-13、重み公開 2026-06-17） |
| パラメータ / 文脈長 | MoE 約 744B〜753B 総 / 約 40B active、**1M トークン** |
| ライセンス | ✅ **MIT（裏取り済み）**。BF16/FP8 重み公開、vLLM でローカル実行可 |
| API | ✅ OpenAI 互換 ＋ **Anthropic 互換** |
| CLI | Claude Code / Cline / OpenCode を公式サポート |
| MCP | 未確認 |
| ローカル可否 | ✅ 可（MIT・重み公開） |

### API 料金（2026-07-20・公式 docs.z.ai）

USD / 1M トークン。

| モデル | 入力 | 出力 |
|---|---|---|
| **GLM-5.2** | $1.40 | $4.40 |
| GLM-5 | $1.00 | $3.20 |
| GLM-4.7 | $0.60 | $2.20 |
| GLM-4.7-Flash | **無料** | **無料** |

**OpenRouter 経由の方が安い**: GLM-5.2 を 1.05M context・**$0.93 / $3.00** で提供。公式 API より低価格。

### GLM Coding Plan（サブスク）

| プラン | 月額 | クォータ |
|---|---|---|
| Lite | **$18〜** | 約 80 prompts/5h・400/週 |
| Pro | **未確認** | 約 400/5h・2,000/週 |
| Max | **未確認** | 約 1,600/5h・8,000/週 |

⚠️ Pro / Max の正価は公式ページから取得できず**未確認**。二次情報が矛盾している（$72/$160 説と $30/$80 説）。
契約前に公式で要確認。全プランで GLM-5.2 / GLM-5-Turbo / GLM-4.7 が使える。

## 管轄・データ規約（3社中最強・一次情報）

| 項目 | 内容 |
|---|---|
| 法域 | **シンガポール**（国際版 z.ai） |
| **コンテンツ保存** | ✅ **一切保存しない**（DPA §4(b) に明記） |
| **学習利用** | ✅ **明示的同意がない限り使わない** |
| 個人データ処理地 | シンガポール |
| ZDR | **実質 ZDR が全 API 顧客に既定適用**。エンタープライズ契約不要 |

> DPA §4(b) 原文の要旨:
> 「顧客および利用者が提供・生成したコンテンツ（入力テキスト等）を一切保存しない。
> リアルタイム処理で API を提供し、**サーバに保存されない**」

ZCode の Optimization Program は**既定オフ**のオプトイン式、設定から15営業日以内に撤回可。

⚠️ **国際版と中国版は完全に別契約**。bigmodel.cn は北京智谱华章が主体で PRC 法・海淀区人民法院管轄、
匿名化データの学習利用を同意不要で留保している。**同じ「GLM」でも規約が真逆なので経路を混同しない。**

出典: [docs.z.ai privacy](https://docs.z.ai/legal-agreement/privacy-policy) / [terms](https://docs.z.ai/legal-agreement/terms-of-use)

## ⚠️ 規制リスク：米国 Entity List 掲載

**2025-01-16 発効で、北京智谱华章科技および複数子会社が米国商務省 Entity List に追加**（EAR §744.11）。
中国製大規模モデル企業として初。

出典: [Federal Register](https://www.federalregister.gov/documents/2025/01/16/2025-00704/addition-of-entities-to-and-revision-of-entry-on-the-entity-list)

日本からの利用に直接の影響はないが、**米国製 HW/SW 調達に制約がかかる企業**である点は
サプライチェーンの継続性リスクとして評価に含める。
[20_モデル/モデル階層.md](../20_モデル/モデル階層.md) の「単一フロンティアへ固定しない」原則の対象。

## ハーネス適性

- ワークフロー組み込み: **高**
- **Claude Code 公式サポート**:
  ```bash
  ANTHROPIC_BASE_URL=https://api.z.ai/api/anthropic
  ANTHROPIC_AUTH_TOKEN=<token>
  ```
  既定マッピング: Opus/Sonnet → GLM-4.7、Haiku → GLM-4.5-Air
- Cline / OpenCode も公式対応
- LiteLLM: `zai/` prefix ／ OpenRouter ✅ ／ AWS Bedrock に GLM-4.7 あり

出典: [docs.z.ai Claude Code](https://docs.z.ai/scenario-example/develop-tools/claude)

## ベンチマーク（⚠️ 全て vendor self-reported）

公式自己申告: SWE-bench Pro 62.1、Terminal-Bench 2.1 で 81.0（Terminus-2）/ 82.7（best）、FrontierSWE 74.4。

**独立検証済みの公式 Terminal-Bench 2.1 リーダーボードに GLM-5.2 は未掲載。**
掲載があるのは前世代 **GLM-5.1 の 58.7%**（Claude Code 経由、2026-05-01）のみ。

ただし Z.ai の比較表中の Opus 4.8 = 78.9 は公式ボードと完全一致しており、**引用元としては誠実**。

## 強み

- **API コンテンツ非保存・非学習を契約で明記**（中国系で最強、西側大手に匹敵）
- **MIT ライセンスで重み公開**（3社中もっともクリーン）
- Claude Code / Cline / OpenCode を公式サポート
- 1M コンテキスト
- GLM-4.7-Flash が無料
- OpenRouter 経由なら公式より安い

## 弱み

- **親会社が米国 Entity List 掲載**（継続性リスク）
- Coding Plan の Pro / Max 価格が公式で確認できない
- DeepSeek より高い（入力 $1.40 vs $0.435）
- 独立検証ベンチに最新モデルが載っていない
- MCP 対応が未確認

## 黒澤用途

- **秘匿寄り・業務寄り処理の第一候補**（中国系の中で）
- Claude Code のバックエンド差し替え候補 → **8/7 の契約判断に直結**
- エージェント基盤の候補（候補棚で「1M・MIT・エージェント基盤候補」と評価済み）
- コスト最優先の大量処理は DeepSeek 継続

## 検証ログ

### 2026-07-20

- タスク: 台帳の新規作成（候補棚止まりだったため昇格）
- 入力: docs.z.ai 公式（pricing / privacy / terms / Claude Code ガイド / devpack）、HF モデルカード、Federal Register
- 結果: **データ規約が中国系4社で最強**と判明。MIT ライセンスも裏取り完了。一方で Entity List 掲載を確認
- 理由: 候補棚に「1M・MIT・エージェント基盤候補」と書きながら台帳化されていなかった
- 再利用判断: 秘匿寄り処理の第一候補として採用検討。Claude Code バックエンド化を要検証
- 次回へのメモ: ①Coding Plan の Pro/Max 正価を公式で確認 ②Claude Code 差し替えの実地検証 ③MCP 対応の確認

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| **A候補** | データ規約・ライセンスが中国系最良で、Claude Code 公式サポートあり | ①Entity List の影響拡大 ②Coding Plan 価格 ③Claude Code バックエンドの実用性 ④独立ベンチへの掲載 |

## 関連

- コスト優先の比較対象: [05_cn-deepseek.md](05_cn-deepseek.md)
- 業務適格性の比較対象: [08_cn-qwen.md](08_cn-qwen.md)
- 秘匿判断: [22_用途/ローカル秘匿.md](../22_用途/ローカル秘匿.md)

# Qwen（Alibaba）

> ローカル秘匿の第一候補として [12_使い分けルール.md](../12_使い分けルール.md) に記載済みだが台帳は未整備だった。
> **確認日: 2026-07-20**（価格・規約・MCP は一次情報。ベンチと一部は二次情報）

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社 | **Alibaba Cloud (Singapore) Private Limited**（国際版）／ 中国本土版の運営法人は未確認 |
| 能力カテゴリ | 01_基盤モデル / 06_APIルーター・推論基盤 / 07_ローカルLLM |
| 種別 | フロンティア級 LLM（API ＋ 一部オープンウェイト） |
| 主用途 | 一般 LLM 処理、コーディング、**ローカル秘匿処理**（3.6系のローカル実行） |
| 主力モデル | qwen3.7-max（フラッグシップ）／ qwen3.7-plus ／ qwen3.6-flash |
| コンテキスト | 主要商用モデルで最大 **1M トークン** |
| 月額 | サブスクなし。API 従量のみ |
| 無料枠 | **2026-04-15 に廃止**（二次情報） |
| API | ✅ OpenAI 互換 |
| CLI | ✅ **Qwen Code**（公式・[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)） |
| MCP | ✅ **標準搭載**（`qwen mcp add`、SSE/HTTP transport、リモート MCP の OAuth 2.0 対応） |
| ローカル可否 | **3.6 系のみ可**（Apache 2.0）。3.7 系は非公開ウェイトで API 専用 |

### API 料金（2026-07-20・国際/シンガポールリージョン・一次情報）

USD / 1M トークン。

| モデル | 入力 | 出力 |
|---|---|---|
| qwen3.7-max | $2.50（**50%オフ適用中**） | $7.50（同） |
| qwen3.7-plus | $0.40〜$1.20（段階制） | $1.60〜$4.80 |
| qwen3.6-flash | $0.25〜$1.00（段階制） | $1.50〜$4.00 |

**価格の読み方に3つ注意**:

1. **入力長に応じた段階制**で単一単価にならない
2. max は**割引適用中**の価格。恒久前提にできない
3. **中国本土リージョンは大幅に安く別体系**

キャッシュヒットは入力の 10%、バッチ推論は 50%。

出典: [Model Studio pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing)

## 管轄・データ規約（DeepSeek との決定的な差分）

| 項目 | 内容 |
|---|---|
| 法域 | **シンガポール**（国際版）／ 中国（本土版）の二本立て |
| データ保存先 | **選択可能** — Singapore / US(Virginia) / **Japan(Tokyo)** / Germany(Frankfurt) / China(Beijing) / China(HK) |
| 学習利用 | ✅ **「明示的な同意なく顧客業務データをモデルの開発・改善に使用しない」と公式明記** |
| 通信暗号化 | AES-256 |

> **これが DeepSeek との最大の差分。**
> Model Studio API は明示的な非学習条項を持ち、**日本リージョンを選択できる**。
> 業務コード・受託案件で中国系モデルを使うなら、DeepSeek ではなくこちらが候補になる。

⚠️ **ただし適用範囲に注意**: 上記は **Model Studio API の規約**。
**Qwen Code CLI と qwen.ai コンシューマ版は別規約**で、学習利用可否は**未確認**。
CLI を業務で使う場合は別途確認が必要。

出典: [訓練データ開示](https://www.alibabacloud.com/help/en/model-studio/qwen-and-wan-training-data-disclosure) / [Model Studio FAQ](https://www.alibabacloud.com/help/en/model-studio/faq-about-alibaba-cloud-model-studio) / [qwen.ai privacy policy](https://qwen.ai/privacypolicy)

### 規制履歴

DeepSeek に相当する広範な政府利用禁止は**確認できなかった**（「なし」ではなく未確認）。
Alibaba Cloud 全体の各国規制動向も未確認。

## ハーネス適性

- ワークフロー組み込み: **高**
- 接続方式: OpenAI 互換 API / OpenRouter / LiteLLM（`dashscope/`）/ **Vertex AI 経由**（`vertex_ai/qwen/`）
- **MCP を公式 CLI が標準搭載**している点は DeepSeek より明確に強い
- **Vertex AI 経由で使える**点は Vertex フル活用の現行方針と噛み合う

## 強み

- **明示的な非学習条項**と**リージョン選択（日本可）** — 業務利用の適格性が高い
- 公式 CLI ＋ MCP 標準搭載
- 3.6 系が Apache 2.0 でローカル実行可能
- Vertex AI 経由の接続経路がある
- エージェント型ベンチで DeepSeek を上回る（下記）

## 弱み

- **フラッグシップ 3.7 系は非公開ウェイト**でローカル不可
- 段階制課金＋割引適用中で**実効単価が読みにくい**
- DeepSeek より明確に高価（max 入力 $2.50 vs V4-Pro $0.435）
- CLI / コンシューマ版が API と別規約（学習利用可否 未確認）
- 無料枠が廃止済み

## 得意用途

- **業務・受託案件でのコード生成**（非学習条項があるため）
- エージェント型の複雑タスク（SWE-bench Pro で優位）
- ローカル秘匿処理（3.6 系 ＋ Ollama）

## 苦手用途

- コスト最優先の大量生成（DeepSeek の方が安い）
- フラッグシップのローカル実行

## 黒澤用途

- **ローカル秘匿の第一候補**（Ollama + Qwen系）— 使い分けルールに記載済み
- DeepSeek が規約上使えない処理の受け皿
- Vertex 活用方針との接続候補

## ベンチマーク（二次情報・ベンダー申告ベース）

| ベンチ | Qwen3.7 Max | DeepSeek V4-Pro |
|---|---|---|
| SWE-bench Verified | 80.4% | 80.6%（Pro-Max） |
| **SWE-bench Pro（エージェント型）** | **60.6%** | 55.4% |

独立実測ではない。**エージェント型タスクでは Qwen が優位**という点は要実地検証。

## 検証ログ

### 2026-07-20

- タスク: 台帳の新規作成（使い分けルールに記載済みなのに台帳が存在しなかったため）
- 入力: Model Studio pricing / 訓練データ開示 / FAQ / qwen.ai ポリシー / Qwen Code MCP docs
- 結果: 価格・規約・MCP を一次情報で確定。**非学習条項と日本リージョンが DeepSeek との決定的差分**と判明
- 理由: ローカル秘匿の第一候補でありながら未台帳だった
- 再利用判断: 業務・秘匿寄り処理の第一候補として採用検討。コスト優先処理は DeepSeek 継続
- 次回へのメモ: ①Qwen Code CLI の規約を確認 ②エージェント型での優位を実測 ③Vertex 経由の接続検証

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| **A候補** | 非学習条項＋リージョン選択で業務適格性が高く、MCP 標準搭載 | ①CLI の規約 ②実効単価（段階制・割引の恒久性）③エージェント型の実測 ④Vertex 経由の実用性 |

## 関連

- 比較対象: [05_cn-deepseek.md](05_cn-deepseek.md)
- 秘匿判断: [22_用途/ローカル秘匿.md](../22_用途/ローカル秘匿.md)
- 使い分け正本: [12_使い分けルール.md](../12_使い分けルール.md)

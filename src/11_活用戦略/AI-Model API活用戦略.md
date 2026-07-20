# AI-Model API活用戦略

> **契約ではなく「契約済みキーをどう使うか」の戦略。**
> 契約側の正本は [10_契約/](../10_契約/README.md)。本ドキュメントは
> [02_AIフロンティア・バーベル戦略.md](../10_契約/02_AIフロンティア・バーベル戦略.md) の
> 第3レグ「その他は API 従量課金で摘み食いする」を、**実際にどう運用しているか**を定義する。
>
> 確認日: 2026-07-20

## 位置づけ

バーベル戦略は「高額1・標準1・その他API」と定めるが、その **API レグが機能するかは実行基盤に依存する**。
基盤がなければ「API で摘み食い」は絵に描いた餅になり、結局サブスクを増やす方向へ逆戻りする。

本戦略の主張は次の一点。

> **API レグは自作基盤で既に稼働しており、摩擦は低い。**
> ゆえに、サブスク契約を増やす前に「API で足りないか」を先に問える。

## 2つの軸

用途が異なる2系統を持つ。どちらも API キー従量課金で動く。

| 軸 | システム | 性格 | 主用途 |
|---|---|---|---|
| **① 対話型** | Open WebUI ＋ LiteLLM proxy | 即時・人が読む・単発 | 最高峰モデルへのピンポイント質問 |
| **② バッチ型** | reasoning-orchestrator | 非同期・監査可能・役割分離 | 品質重視の推論パイプライン |

計量・課金記録はどちらも **ai-gateway** に集約する。

---

## ① Open WebUI ＋ LiteLLM（対話型・常用）

`~/Dev/private-ops/labs/ai-frontends/open-webui`

契約済み全プロバイダを1つの UI から使う個人常用フロントエンド。
Mac mini で常時稼働し、自宅は localhost、外出先は tailnet 経由で同一環境へ入る。

到達可能モデル（2026-07-20 実測）:

```text
OpenAI     … 直接接続（API が返す全モデル）
Anthropic  … claude-opus-4.8 / claude-sonnet-5 / claude-haiku-4.5   ← LiteLLM
Google     … gemini-pro / gemini-flash                              ← LiteLLM
DeepSeek   … deepseek-pro / deepseek-flash                          ← LiteLLM
Perplexity … sonar / sonar-pro / sonar-reasoning-pro                ← LiteLLM
```

- モデル一覧の正本は `litellm-config.yaml`
- シークレットは Doppler `apps`/`dev` から実行時注入（repo にキーを持たない）
- 公開 inbound 面は作らない（Tailscale serve で tailnet 限定 HTTPS）

**戦略上の意味**: 未契約プロバイダの最上位モデルに、サブスクなしで到達できる。
Google / xAI に高額プラン（Ultra ¥14,500 / Heavy $300）を契約する理由がないのはこのため。

## ② reasoning-orchestrator（バッチ型・品質重視）

`~/Dev/private-ai-agent/reasoning-orchestrator`

Markdown の問いを役割分離パイプラインで処理する、個人所有のローカル推論バッチ。

```text
workhorse
  → deterministic verification
  → cross-vendor critic
  → synthesis
  → conditional premium
```

- 最新情報が必要な時だけ evidence を取得する
- 判断内容・失敗・route・検証・コストを**監査可能に残す**（SQLite ＋ run artifact）
- 価値の中心は特定 provider/model ではなく**オーケストレーション層**にある
- **品質が目的、コストは制約**
- 秘密送信・不可逆操作・売買執行の最終権限は所有者に残す

### バーベル戦略との構造的一致

このパイプラインの **`conditional premium`** は、バーベル戦略をソフトウェアとして実装したものに等しい。

| バーベル戦略 | reasoning-orchestrator |
|---|---|
| 日常は標準モデルで回す | workhorse |
| 最高峰モデルはピンポイントで使う | conditional premium |
| 高額固定費の二重化を避ける | premium は deterministic policy か明示的 owner intent の例外時のみ |

> 通常の成功経路は premium を呼ばない。
> premium は privacy / budget / verifier を bypass できない。

つまり「最高峰モデルへのアクセスは維持しつつ、常用はしない」という戦略が、
gate として強制される設計になっている。

### 現在の状態（重要）

**fake/paid execution は release-blocked**。
paid 再開は release runbook §1 の全 stop condition、drift ownership、fresh L1〜L3 をすべて満たす場合のみ。

→ **この軸は現時点で API 予算を消費していない**。コスト試算に含めないこと。
再開時は ai-gateway のログで実績を確認する。

---

## 契約判断への接続

### API 従量はサブスクを全面代替しない

| 用途 | API 従量で代替可能か | 理由 |
|---|---|---|
| チャットで最上位モデルにピンポイント質問 | ✅ 可能 | ① から直接到達。サブスク不要 |
| 品質重視の推論バッチ | ✅ 可能 | ② が担当（現在 release-blocked） |
| **ハーネスで回す**（Claude Code / Codex） | ❌ **不可** | サブスク枠を消費する。API キーでは代替できない |

**サブスクが要るのはハーネスを持つプロバイダだけ**（Anthropic / OpenAI）。
それ以外は本戦略の①②で足りる。

### コスト実測

判断ルール3（従量実績 vs プラン差額の損益分岐）は推測せず、**ai-gateway のログで確定させる**。

```text
例: Fable 5 の月間従量実績 < $80  → Pro $20 ＋ 従量が Max 5x $100 より安い
```

## 破綻条件

- 基盤が止まっているのに「API で足りる」と判断して契約を落とす（① の稼働確認が先）
- ai-gateway を通さない直接呼び出しが増え、**コスト実績が計測できなくなる**
- ② の premium gate を迂回して最高峰モデルを常用し、バーベル戦略が形骸化する
- API キーを repo・Markdown 台帳に書く（Doppler 経由を崩さない）
- 「複数プロバイダをつないだ」だけで品質が上がったと判断する（評価ログで確認する）

## 関連

- 契約側の正本: [10_契約/README.md](../10_契約/README.md)
- バーベル戦略（API レグの出典）: [02_AIフロンティア・バーベル戦略.md](../10_契約/02_AIフロンティア・バーベル戦略.md)
- 現契約: [01_現在の契約.md](../10_契約/01_現在の契約.md)
- ハーネス / ルーティングの用途逆引き: [22_用途/ハーネスルーティング.md](../22_用途/ハーネスルーティング.md)
- コスト実測ログ: [30_評価/](../30_評価/)

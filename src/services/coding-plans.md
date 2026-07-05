# AI コーディングサービス プラン比較

> 個人利用（黒澤）のコーディング系サービスの**料金プラン横比較**。どのプランを契約すべきかの判断材料。
> **確認日: 2026-07-05**（Web 公式・二次情報照合）。料金は頻繁に変わるため、契約・見直し時に再確認する。
> 現在の契約状況は [../現在の契約.md](../現在の契約.md) を参照（このファイルは「選択肢」、契約は「実際に払っているもの」）。

## 一覧（個人プラン・月額 USD）

| サービス | 種別 | 無料枠 | 有料プラン（月額 USD） | 課金モデル | 備考 |
|---|---|---|---|---|---|
| **Cursor** | AI IDE | Hobby $0 | Pro **$20** / Pro+ **$60** / Ultra **$200** | 使用量クレジット（Pro=$20 相当プール、Pro+=3x、Ultra=20x） | 年払い 20%off。学生は Pro 1年無料 |
| **GitHub Copilot** | IDE 補完/エージェント | Free $0（補完 2000/月） | Pro **$10** / Pro+ **$39** / Max **$100** | 2026-06-01 から従量（AI Credits、1cr=$0.01。Pro=$15/Pro+=$70/Max=$200 相当込み） | Business $19・Enterprise $39/席 |
| **Claude（Pro/Max）** | Claude Code の土台 | 無し（要 sub） | Pro **$20** / Max 5x **$100** / Max 20x **$200** | サブスク。Claude と Claude Code で**使用量を共有**（5時間ローリング窓＋週次上限） | Pro=~10–45 prompt/5h、Max20x=~900/5h |
| **ChatGPT（Plus/Pro）** | Codex CLI/IDE の土台 | Free / Go $8 | Plus **$20** / Pro **$100** / Pro **$200** | サブスク。Plus に Codex 含む。Pro100=5x、Pro200=20x quota | Codex Mobile は全プラン無料。**API は別課金** |
| **Cline** | VS Code OSS エージェント | 無料（拡張自体） | 無し（BYO API key / Cline クレジット） | モデル API 従量（自分のキー or OpenRouter 等） | ソフトは無料、コストはモデル利用分 |
| **Aider** | Git 差分前提 CLI | 無料（OSS） | 無し（BYO API key） | モデル API 従量 | ソフトは無料 |
| **OpenCode** | ターミナルエージェント | 無料（OSS） | 無し（BYO API key） | モデル API 従量 | ソフトは無料 |
| **Codex CLI** | OpenAI 製 CLI | 無料（CLI 本体） | ChatGPT Plus/Pro 経由 or API key | サブスク quota or API 従量 | ChatGPT サブスクの Codex quota を消費 |

> 円換算目安: ×155（¥/USD）。例 $20≈¥3,100、$100≈¥15,500、$200≈¥31,000。為替と課税で変動。

## プラン詳細（有料の主力4系統）

### Cursor（AI IDE）
- **Hobby**: $0。Tab 補完・Agent を制限付きで試せる。
- **Pro $20**: Tab 補完・Auto モード無制限＋プレミアムモデル用に $20 相当のクレジットプール。
- **Pro+ $60**: OpenAI / Claude / Gemini の使用量 3x。
- **Ultra $200**: 同 20x＋新機能優先アクセス。
- 課金は使用量クレジット制。年払いで 20%off。

### GitHub Copilot（補完＋エージェント）
- **2026-06-01 から従量課金へ移行**。各プランに月次 AI Credits 付与（1 credit=$0.01）、超過は従量。
- **Free $0**: 補完 2000/月、chat/agent 制限。
- **Pro $10**（$15 credits）/ **Pro+ $39**（$70 credits・プレミアムモデル）/ **Max $100**（$200 credits・最上位個人枠）。
- 法人: Business $19/席（$19 credits）、Enterprise $39/席。

### Claude Pro / Max（＝ Claude Code の土台）
- **Claude Code は Pro/Max サブスクで使える**（API 従量とは別）。Claude チャットと Claude Code で**同じ使用量枠を共有**。
- **Pro $20** / **Max 5x $100** / **Max 20x $200**。
- 使用量: 5時間ローリング窓（初回 prompt 起点）＋ Max は週次上限（全モデル＋Sonnet 別）。Pro ≈10–45 prompt/5h、Max20x ≈最大900/5h。
- 2026-05 に 5時間枠が恒久2倍化・ピーク時スロットル撤廃、週次上限も一時 +50%（〜2026-07-13）。

### ChatGPT Plus / Pro（＝ Codex CLI/IDE の土台）
- **Plus $20** に Codex 含む（GPT-5.5、Deep Research 10/月 等）。
- **Pro $100**（5x Plus quota）/ **Pro $200**（20x quota、Sora、GPT-5.4 1M context）。**Go $8** は軽量枠。
- Codex Mobile は全プラン無料。**ChatGPT サブスクと API は別課金**（Plus では API は使えない）。

## BYO-key 系（ソフト無料・コストはモデル API）
- **Cline / Aider / OpenCode**: ソフトウェアは無料。実コストは呼ぶモデルの API 従量（直接 or OpenRouter 経由）。プラン契約は不要で、モデル選択とトークン量でコストが決まる。
- **Codex CLI**: CLI 本体は無料だが、ChatGPT サブスクの Codex quota か OpenAI API key を消費。

## 使い分けの要点（コスト観点）
- **サブスク定額で回すなら**: Claude Code=Claude Max、Codex=ChatGPT Plus/Pro、IDE 補完=Copilot、IDE エージェント=Cursor。
- **モデルを自由に選びトークン単価で払うなら**: Cline / Aider / OpenCode ＋ BYO key（OpenRouter でルーティング）。
- 定額サブスク（Claude Max / ChatGPT Pro）は**使用量共有・上限あり**、BYO-key は**青天井だが従量**。用途量で損益分岐が変わる。

## 出典（2026-07-05 時点）
- Cursor: `aiproductivity.ai/blog/cursor-pricing`、`nocode.mba/articles/cursor-pricing`
- GitHub Copilot: `github.com/features/copilot/plans`、`github.blog`（従量移行）
- Claude: `support.claude.com`（Claude Code with Pro/Max）、`claude.com/pricing`
- ChatGPT/Codex: `chatgpt.com/pricing`、`intuitionlabs.ai/articles/chatgpt-plans-comparison`

> 更新規約: 台帳（`services/README.md`）に従い、料金変更を見たら確認日を差し替える。個別サービスの詳細は各 `services/<name>.md` の「基本」表へ反映してよい（現状 `未確認` のものが多い）。

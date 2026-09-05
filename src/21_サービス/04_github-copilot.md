# GitHub Copilot

> **公式情報確認日: 2026-09-06**。料金は USD・月払いの表示額。IDE 補完に加え、CLI / SDK / クラウドエージェントを含めて評価する。実タスク比較は未実施のため B候補を維持。

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社 | GitHub / Microsoft |
| 能力カテゴリ | 04_コーディングエージェント / 05_CLI・IDE・ハーネス |
| 種別 | IDE 補完 / CLI・デスクトップ / クラウドエージェント / SDK |
| 主用途 | 補完、複数ファイル実装、Issue→PR、コードレビュー、自動化 |
| 月額 | Pro $10 / Pro+ $39 / Max $100。Business $19/席、Enterprise $39/席。[プラン](https://docs.github.com/en/copilot/get-started/plans) |
| 無料枠 | Free: 補完 2,000/月、制限付き AI credits、モデルは Auto 選択。CLI / Copilot app も対象。無料 AI credits の固定数量は未確認 |
| API | **Copilot SDK は GA**。TypeScript / Python / Go / .NET / Rust / Java。GitHub 認証または BYOK でエージェントを組み込み可。GitHub Models の推論 API とは別。[SDK 発表](https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available/) |
| CLI | 独立した `copilot`。対話・Plan・非対話 `copilot -p`。macOS / Linux / Windows 対応。[CLI](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli) |
| IDE | VS Code、Visual Studio、JetBrains、Xcode、Eclipse 等。機能・モデルの対応範囲はエディタごとに異なる |
| MCP | 対応。CLI で外部 MCP サーバー接続、SDK で MCP と独自ツールを組み込み可 |
| AGENTS.md / rules / hooks 対応 | CLI は `AGENTS.md`、`CLAUDE.md`、`.github/copilot-instructions.md`、パス別 instructions を読める。skills / custom agents / hooks あり。[指示ファイル](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-custom-instructions) / [Hooks](https://docs.github.com/en/copilot/reference/hooks-reference) |
| ローカル可否 | CLI / IDE でローカルファイル編集・コマンド実行可。標準モデルの推論はクラウド。cloud agent は遠隔環境で作業。完全オフライン構成は未検証 |
| モバイル / Android | GitHub Mobile（iOS / Android）から Chat 等を利用可。端末内で CLI が動く意味ではない。[対応面](https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot/) |
| 学習利用 | 個人 Free / Pro / Pro+ / Max は設定に従い学習利用され得る（opt-out 可）。Business / Enterprise は顧客データを学習に使わない。モデルごとの保存条件は別。[モデルのホスティング・データ条件](https://docs.github.com/en/copilot/reference/ai-models/model-hosting) |

基本表の料金 / API / CLI / IDE / MCP / 指示ファイル / ローカル可否 / データ利用はすべて 2026-09-06 確認。

### 使用量と追加費用

| 個人プラン | 基本 AI credits / 月 | 変動する追加枠（Flex） | 確認時点の合計 |
|---|---:|---:|---:|
| Pro | 1,000 | 500 | 1,500（$15 相当） |
| Pro+ | 3,900 | 3,100 | 7,000（$70 相当） |
| Max | 10,000 | 10,000 | 20,000（$200 相当） |

**1 AI credit = $0.01**。モデルとトークン量で消費し、Flex は将来変動する。毎月1日 UTC にリセット、繰越なし。有料プランの補完・Next edit suggestions は AI credits を消費しない。Chat / CLI / cloud agent 等は同じ包含枠を使い、超過継続には追加予算の設定が必要。[個人向け課金](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals)

### 最近の重要更新

- **2026-09-04: GPT-6 Astra の GA・段階展開**。対象は **Pro+ / Max / Business / Enterprise**。Pro $10 に全最上位モデルが含まれるわけではない。[発表](https://github.blog/changelog/2026-09-04-gpt-6-astra-is-generally-available-in-github-copilot/)
- **2026-09-02: Copilot app / CLI の content exclusion が GA**。Business / Enterprise の管理者が除外したファイルをコンテキストに使わない。[発表](https://github.blog/changelog/2026-09-02-content-exclusions-generally-available-in-copilot-app-and-cli/)
- CLI はローカル sandbox と `--cloud` によるクラウド sandbox も提供するが、**public preview**。SDK は 6/2 に GA 済み。安定版機能と試験提供機能を分けて運用する。[CLI の実行環境](https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-copilot-cli)

## ハーネス適性

- ワークフロー組み込み: 高候補（CLI / SDK の仕様確認済み、実運用は未評価）。
- 接続方式: IDE / GitHub / CLI / SDK / MCP。cloud agent で Issue 起点の実装・PR 作成を委譲できる。[cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent)
- 指示の共有: CLI は複数の指示ファイルを統合して読む。一般的な優先順位は定義されていないため、AGENTS.md と Claude / Copilot 固有指示の矛盾を避ける。
- 制約: hooks のイベント・実行環境、モデル提供、管理者ポリシーは実行面で異なる。IDE で動く設定をそのまま CLI / cloud agent 共通とみなさない。

## 強み

- エディタ内の小さな補完。
- 反復的なコード記述。
- GitHub 連携。
- CLI / SDK / cloud agent を同じサービスで扱え、既存の GitHub Issue・PR 運用に接続できる。
- 有料プランは補完の使用量とエージェントの AI credits を分けて管理できる。

## 弱み

- 長いエージェント実行ではトークン課金が増え、安い月額だけでは総費用を判断できない。
- モデルを切り替えると保存条件も変わる。**Fable 5 / 5.1 は標準では安全性監視のため入力・出力を保存**し、通常の Claude モデルと同じ ZDR 条件ではない。[モデル別条件](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)
- 補完の便利さが評価ログに残りにくい。

## 得意用途

- IDE内補完。
- テストの雛形。
- 小さな関数や型定義の補助。
- Issue の実装→テスト→PR、CLI による repo 修正（対応機能に基づく評価候補）。

## 苦手用途

- GitHub / 組織のポリシー設定を揃えず、全エディタ・全モデルで同じ動作を期待する運用。
- 追加予算を見ずに最上位モデルで大量・長時間処理を回す用途。

複数ファイル編集や docs / テストまでの一連作業を「非対応・苦手」とする旧記述は撤回。対応は確認済みで、品質は同一タスク比較で測る。

## 黒澤用途

- [現在の契約](../10_契約/01_現在の契約.md) では **2026-08 解約済み**。今回の更新は再契約判断の材料。
- Free の補完と CLI で、Codex / Claude Code の代替度を測る。
- 再契約の比較軸は Pro の補完価値、Pro+ のモデル到達性、Issue→PR の完了率と AI credits 消費。追加費用を含めて判断する。

## 検証ログ

### 2026-06-27

- タスク: 初期分類
- 入力: コーディング用途の棚卸し
- 結果: coding の IDE内補完枠へ配置
- 理由: CLIエージェントとは役割が異なる
- 再利用判断: IDE補完用途で検証する

### 2026-09-06

- タスク: 公式プラン・課金・CLI / SDK・9月リリースの調査更新。
- 結果: 「IDE 補完中心」の旧分類を、CLI / SDK / クラウドを含むエージェントへ更新。Flex 枠、Astra の対象プラン、データ条件を確認。
- 未実施: repo 実装・コードレビューの実測、本人の無料枠・設定確認。
- 再利用判断: B候補を維持し、エージェントとして再評価する。解約済みという本人の契約記録は変更しない。

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| B候補 | 補完に加え CLI / SDK / GitHub 上の実装委譲が比較対象 | Free / Pro / Pro+ の差、Issue→PR の完了率、MCP・レビュー品質、追加費用 |

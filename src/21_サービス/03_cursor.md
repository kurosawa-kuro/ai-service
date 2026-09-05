# Cursor

> **公式情報確認日: 2026-09-06**。料金は USD・月払いの表示額（税別）。IDE / CLI / SDK / Cloud Agents / Origin を含めて更新。A候補は継続し、性能・費用対効果は実タスクで確認する。

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社 | Anysphere（Cursor）。**2026-08-14 に SpaceX の買収完了を発表**。[公式発表](https://cursor.com/blog/joining-spacex) |
| 能力カテゴリ | 04_コーディングエージェント / 05_CLI・IDE・ハーネス |
| 種別 | AI IDE / CLI / SDK / クラウドエージェント / コードホスティング |
| 主用途 | IDE 内編集、複数ファイル実装、遠隔エージェント、レビュー、自動化 |
| 月額 | Hobby $0 / Pro $20 / Pro+ $60 / Ultra $200。Teams Standard $40/席、Premium $120/席。Enterprise 個別。[公式プラン](https://cursor.com/help/account-and-billing/pricing) |
| 無料枠 | Hobby で Agent / Chat / Tab を制限付き利用。無料枠の固定回数は未確認 |
| API | Cloud Agents REST API（beta）、TypeScript `@cursor/sdk` / Python `cursor-sdk` でローカル・クラウドのエージェントを制御。管理・分析 API は Enterprise 向け。[API 一覧](https://cursor.com/docs/api) / [TS SDK](https://cursor.com/docs/sdk/typescript) / [Python SDK](https://cursor.com/docs/sdk/python) |
| CLI | 可。`agent`、非対話 `agent -p`。macOS / Linux / Windows 対応。[CLI](https://cursor.com/docs/cli/overview) |
| IDE | Cursor エディタと Agents の操作画面を提供。CLI とクラウドも選択可 |
| MCP | ローカル stdio / リモート MCP に対応。[MCP](https://cursor.com/docs/mcp) |
| AGENTS.md / rules / hooks 対応 | 階層的な `AGENTS.md`、`.cursor/rules/*.mdc`、skills / plugins / hooks。[Rules](https://cursor.com/docs/rules) / [Hooks](https://cursor.com/docs/hooks) |
| ローカル可否 | IDE / CLI でローカル編集・実行可。Cloud Agents は管理クラウドまたは self-hosted machines を選べる。**self-hosted でもモデル入力・ツール出力等は Cursor へ送信**され、完全オフラインではない。[実行境界](https://cursor.com/docs/cloud-agent/self-hosted) |
| モバイル / Android | iOS / iPadOS アプリあり（iOS / iPadOS 26.0 以降、有料対象プラン）。**Android アプリは計画中**。Web からの操作は別経路。[Mobile](https://cursor.com/docs/cloud-agent/mobile) |
| 学習利用 | Privacy Mode 有効時は学習に使わない。無効時はコード等を保存・学習利用し得る。濫用検知時の保存例外、非 ZDR モデルの条件あり。BYOK も Cursor バックエンドを経由。[データ利用（8/28 更新）](https://cursor.com/data-use) |

基本表の料金 / API / CLI / IDE / MCP / 指示ファイル / ローカル可否 / データ利用はすべて 2026-09-06 確認。

### 使用量と追加費用

- **Cursor Models と Other Models の2プール**。前者は Grok 4.6 / Grok 4.5 / Composer 2.5、後者は他社モデルの使用量。Pro / Pro+ / Ultra は両方を含む。月次リセットで、追加の on-demand usage も選べる。[Models & Pricing](https://cursor.com/docs/models-and-pricing)
- 有料個人プランは Tab 無制限。料金ページの Agent 利用枠は Pro+ が Pro の 3倍、Ultra が20倍。**「Auto 無制限」「プレミアムモデルは一律 $20 分」という旧理解で見積もらない**。実際の包含量は使用量画面で確認する。[料金](https://cursor.com/pricing)
- Teams / Enterprise の他社モデルには **Cursor Token Rate $0.25 / 1M tokens** が追加され、包含枠・超過・BYOK にも適用。個人プランと混同しない。[追加レート](https://cursor.com/help/models-and-usage/token-rate)

### 最近の重要更新

- **2026-09-02: Self-hosted machines**。自分の PC / VM やチームの worker pool でツールを実行できる。Mac / Linux で computer use も対応。[changelog](https://cursor.com/changelog) / [実行環境](https://cursor.com/docs/cloud-agent/self-hosted)
- **2026-08-27: Web のプレビュー・公開フロー**。クラウド環境をブラウザで確認でき、Vercel アカウントを接続して公開可能。[changelog](https://cursor.com/changelog)
- **2026-08-17: Origin Code Hosting の初期 beta**。有料プランへ段階提供され、repo / PR / コード閲覧 / GitHub sync を備える。現時点の事実はコードホスティングの追加であり、「Git 全体を置換した」とは扱わない。[発表](https://cursor.com/changelog)

## ハーネス適性

- ワークフロー組み込み: 高候補（CLI / SDK / API の仕様確認済み、黒澤環境では未実測）。
- 接続方式: IDE / CLI / TypeScript・Python SDK / Cloud Agents API / MCP。
- 自動化: `agent -p` の JSON / stream-json 出力を使える。非対話で実際にファイル変更するには `--force` が必要で、省略時は変更提案になる。[Headless CLI](https://cursor.com/docs/cli/headless)
- 指示の共有: repo 共通の `AGENTS.md` を使い、パス条件等が必要な部分を `.cursor/rules/*.mdc` に置く。
- 制約: ローカル・管理クラウド・self-hosted で実行環境を記録する。Origin の移行性と GitHub sync、成果物・費用の追跡は実測が必要。

## 強み

- エディタ内で文脈を持った修正を試しやすい。
- UI上で差分を見ながら操作しやすい。
- エージェント型IDEの実験に向く。
- UI でのレビューから CLI / SDK / 遠隔エージェントまで、一つのサービスで比較できる。
- 自前の Mac / VM・開発環境を Cloud Agents の実行先にできる。

## 弱み

- IDE 以外の連携は増えたが、モデル・実行場所・料金プールが増えて使用量を追いにくい。
- 同じファイルを他エージェントと同時編集すると破綻しやすい。
- Origin は初期 beta。Android ネイティブアプリも未提供のため、モバイル運用を iOS と同等に想定できない。
- Privacy Mode や self-hosted は外部送信を止める設定ではない。

## 得意用途

- UIを見ながらの実装。
- 複数ファイルの軽〜中規模修正。
- IDE内での探索。
- 自前の実行環境を使う遠隔作業、SDK / CLI による実装自動化（仕様に基づく評価候補）。

## 苦手用途

- コード・ツール出力を一切外へ送れない完全オフライン運用。
- 初期 beta の Origin を、移行・同期検証なしで既存 GitHub 運用の代わりにすること。

「CLI 作業が苦手」という旧記述は撤回。Headless CLI / SDK の対応は確認できたため、再現性・ログ品質を実タスクで比較する。

## 黒澤用途

- エージェントIDEの比較。
- Codex / Claude Code と役割分担できるかの検証。
- [現在の契約](../10_契約/01_現在の契約.md) では Hobby。まず無料枠で編集体験を測り、有料の Cloud Agents / Origin は費用対効果の検証対象にする。
- 非 iOS 運用では Web からの指示・差分レビューを確認する。Android アプリはリリース待ち。

## 検証ログ

### 2026-06-27

- タスク: 初期分類
- 入力: コーディング用途の棚卸し
- 結果: coding のエージェント実験枠へ配置
- 理由: IDE体験として Codex / Claude Code と異なる
- 再利用判断: IDEベースの開発体験で検証する

### 2026-07-05

- タスク: 昇格レビュー（B候補 → A候補）
- 理由（当時の owner 見立て）: イーロンによる巨額買収で各種機能の高度化・Git 代替化・モバイルフレンドリー化が加速。IDE エージェント勢の中で優位が広がると判断。
- 2026-09-06 補足: 上記は当時の見立てとして保存。買収**完了**は8/14の公式発表、Origin の初期 beta は8/17、Android アプリは計画中と確認。能力優位や Git 全体の代替を示す実測ではない。
- 確認: 料金 = Hobby $0 / Pro $20 / Pro+ $60 / Ultra $200（[コーディングプラン比較](../20_モデル/プラン比較.md)）。黒澤の現契約は Hobby 無料枠（[現在の契約](../10_契約/01_現在の契約.md)）。
- 再利用判断: A候補として実タスクで Codex / Claude Code と役割分担を検証する。

### 2026-09-06

- タスク: 公式料金・docs・changelog・買収発表の調査更新。
- 結果: CLI / SDK / MCP / self-hosted、2つの料金プール、Origin 初期 beta、iOS と Android の提供差を確認。
- 未実施: 有料プランでの作業量・追加課金、Origin 同期・移行、Web / モバイル・self-hosted の動作検証。
- 再利用判断: A候補を維持。買収への期待から、実際に追加された機能とコストを比較する段階へ進める。

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| A候補 | IDE・CLI・SDK・遠隔実行が揃い、開発環境全体の比較候補 | Codex / Claude Code との手戻り差、2プールの実費、Origin の同期・移行、Android からの操作 |

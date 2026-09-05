# Codex / Codex CLI

> **公式情報確認日: 2026-09-06**。料金は USD・月払いの表示額。仕様確認と実タスク評価を分け、既存の A 評価を維持する。

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社 | OpenAI |
| 能力カテゴリ | 04_コーディングエージェント / 05_CLI・IDE・ハーネス |
| 種別 | CLI / IDE 拡張 / デスクトップ / クラウドエージェント |
| 主用途 | リポジトリ作業、実装、レビュー、テスト、ドキュメント更新 |
| 月額 | Go $8 / Plus $20 / Pro 5x $100 / Pro 20x $200。Business は月払い $25/人、年払い $20/人/月・2人以上。API キー利用は別途従量。[料金](https://learn.chatgpt.com/docs/pricing) |
| 無料枠 | ChatGPT Free に Codex の制限付き利用を含む。CLI 本体の料金とモデル使用料は別 |
| API | Codex SDK（TypeScript / Python）、App Server で組み込み可。OpenAI API キー利用時は ChatGPT の包含枠を使わない。[SDK](https://learn.chatgpt.com/docs/codex-sdk) |
| CLI | 可。`codex`、非対話 `codex exec`、`codex resume`。[CLI](https://learn.chatgpt.com/docs/codex/cli) |
| IDE | 可。Codex IDE 拡張。CLI・デスクトップ・クラウドは別の実行面 |
| MCP | クライアント対応（stdio / Streamable HTTP、OAuth）。`codex mcp-server` によるサーバー化は**非推奨**、新規連携は App Server。[MCP](https://learn.chatgpt.com/docs/extend/mcp) / [サーバー移行案内](https://learn.chatgpt.com/docs/mcp-server) |
| AGENTS.md / rules / hooks 対応 | `AGENTS.md`、実行ルール、skills / plugins、hooks。hooks は `.codex/hooks.json` または `config.toml`。[Hooks](https://learn.chatgpt.com/docs/hooks) |
| ローカル可否 | ファイル編集・コマンドはローカル実行可。OpenAI モデルの推論はクラウド。`--oss` で Ollama / LM Studio を選ぶローカル推論にも対応するが、同等の能力・完全オフライン運用は未検証。[設定](https://learn.chatgpt.com/docs/config-file/config-advanced) |
| モバイル / Android | ChatGPT モバイルの Remote から接続中の Mac / Windows PC の作業を開始・承認・確認できる。端末を起動・接続しておく必要あり。Android 個別の配布状態は未確認。[Remote](https://learn.chatgpt.com/docs/remote) |

基本表の料金 / API / CLI / IDE / MCP / 指示ファイル / ローカル可否はすべて 2026-09-06 確認。

### 最近の重要更新

- **2026-09-04: CLI 0.153.4**。Astra をモデル選択に表示し、モデル未設定時の同梱既定値を Astra に変更。9/3 の 0.153.0 では遠隔 marketplace の plugin 一覧・追加・削除にも対応。[公式 changelog](https://learn.chatgpt.com/docs/changelog)
- 現行のモデル選択肢は **GPT-6 Astra / GPT-5.6 Sol・Terra・Luna**。Astra は CLI / IDE / デスクトップ等に対応するが、公式モデル表の **Codex cloud は非対応**。実際の表示・利用可否はアカウントと管理設定で確認する。[モデル](https://learn.chatgpt.com/docs/models)
- **ChatGPT Work と Codex は使用量を共有**。Pro の 5x / 20x は Plus 比の利用枠で、無制限ではない。モデル・推論量・Fast 設定で消費が変わるため、固定タスク数を保証値として扱わない。API キーでは GitHub 自動レビュー等のクラウド機能を利用できない。[料金・上限](https://learn.chatgpt.com/docs/pricing)

## ハーネス適性

- ワークフロー組み込み: 高
- 接続方式: `codex exec`、SDK、App Server、MCP、ローカルファイル編集・コマンド実行。
- 自動化: `codex exec --json` でイベントを JSONL 出力し、`--output-schema` で最終結果の形式を指定できる。[非対話実行](https://learn.chatgpt.com/docs/non-interactive-mode)
- 共通指示: repo の `AGENTS.md` を正本にする。モデルやサブエージェントの設定は実行時に記録して比較する。
- 制約: sandbox と承認・ネットワーク設定は別に管理する。ローカルで実行することと、コードが外部に送られないことは同義ではない。[権限と安全性](https://learn.chatgpt.com/docs/agent-approvals-security)

## 強み

- コードベースを読んで差分を作れる。
- テスト実行、Makefile、docs 更新まで一連で扱いやすい。
- AGENTS.md による repo 固有ルールとの相性が高い。

## 弱み

- 広い権限を渡すほど事故リスクが上がる。
- 最新仕様や外部サービス情報は確認が必要。
- 長い作業や並列実行では使用量が増える。作業範囲・完了条件・モデルを揃えて費用と手戻りを測る。
- CLI・IDE・クラウドでモデルと機能の提供範囲が異なる。API キーと ChatGPT ログインも同じ条件ではない。

## 得意用途

- 小〜中規模の実装。
- 既存コードの修正。
- テスト追加。
- docs と実装の同期。
- CLI / Markdown 台帳の整備。

## 苦手用途

- 判断基準のない大規模設計を、途中の方向修正なしで完了させる運用。
- 検索・出典確認を省いた外部サービスの最新料金・規約判断。
- CLI 単体での GUI 確認。ブラウザ / computer use 等を使う実行面・ツール構成が別途必要。

## 黒澤用途

- ai-service の台帳生成・整備。
- ハーネス設計。
- コードレビュー観点の壁打ち。
- ドキュメントと実装の差分整理。
- 次の比較は同一 repo の「修正→検証→docs 更新」で、Astra と Terra / Luna の完了率・消費枠・手戻りを記録する。
- 本人の支払い状態は [現在の契約](../10_契約/01_現在の契約.md) が正本。同台帳の「Basic ¥3,000」は本人記録の表記であり、公式 Plus と同一かは未確認。

## 検証ログ

### 2026-06-27

- タスク: Phase 1 catalog CLI 実装
- 入力: `docs/01_requirements.md`、`docs/02_architecture.md`
- 結果: `src/ai_catalog`、`tests`、`Makefile`、`src/` 初期構成を生成
- 理由: Markdown台帳を実際に書き足せる状態にできた
- 再利用判断: repo 内の小〜中規模実装では第一候補

### 2026-09-06

- タスク: 公式ドキュメント・料金・changelog の調査更新。
- 結果: Astra 対応、Work との使用量共有、SDK / MCP / hooks / ローカル実行の境界を確認。旧ドキュメント URL は現在の ChatGPT Learn に更新。
- 未実施: 新モデルの実タスク比較、本人の残枠・請求・Remote の動作確認。
- 再利用判断: repo 実装・台帳整備の A 評価は既存ログに基づき継続。今回の調査だけで性能評価を上書きしない。

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| A | repo 作業と Markdown 台帳整備の既存実績あり | Astra / Terra / Luna の費用差、Work と共有する使用量、長い作業の手戻り |

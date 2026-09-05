# Claude Code

> **公式情報確認日: 2026-09-06**。料金は USD・Web 月払いの表示額（税別）。仕様確認と実タスク評価を分け、A候補を維持する。

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社 | Anthropic |
| 能力カテゴリ | 04_コーディングエージェント / 05_CLI・IDE・ハーネス |
| 種別 | CLI / IDE 連携 / デスクトップ / Web コーディングエージェント |
| 主用途 | 長文設計、実装、コードレビュー、仕様整理 |
| 月額 | Pro $20（年払い $200/年）/ Max 5x $100 / Max 20x $200。Team は Standard $25/席、Premium $125/席（月払い）。[料金](https://claude.com/pricing) / [Max](https://support.claude.com/en/articles/11049741-what-is-the-max-plan) |
| 無料枠 | Claude Free に Claude Code は含まれない。有料プラン、または Console の API 従量で利用 |
| API | Claude API と、Claude Code のツール・実行ループを組み込む Agent SDK あり。サブスクの包含枠と API 請求は別。[概要・SDK 案内](https://code.claude.com/docs/en/overview) |
| CLI | 可。`claude`、非対話 `claude -p`。JSON / streaming JSON 出力、会話再開に対応。[非対話実行](https://code.claude.com/docs/en/headless) |
| IDE | VS Code 拡張、JetBrains 連携。デスクトップ / Web でも利用可。[提供面](https://code.claude.com/docs/en/overview) |
| MCP | ローカル stdio / リモート HTTP サーバーに接続可。`claude mcp serve` でツールを MCP サーバーとして公開可。[MCP](https://code.claude.com/docs/en/mcp) |
| AGENTS.md / rules / hooks 対応 | `CLAUDE.md`、`.claude/rules/`、skills / plugins / hooks。**AGENTS.md は直接自動読込しない**ため、`CLAUDE.md` から `@AGENTS.md` で取り込む。[メモリ・指示](https://code.claude.com/docs/en/memory) / [Hooks](https://code.claude.com/docs/en/hooks) |
| ローカル可否 | CLI はローカルファイルを編集しコマンドを実行。Claude 推論は Anthropic または対応クラウド基盤。Web のクラウド実行と区別する。完全ローカル推論は未対応として扱う |
| モバイル / Android | Remote Control でローカルセッションを Web / Claude モバイルから操作。Pro / Max / Team / Enterprise 対象、API キー不可。Team / Enterprise は管理者の有効化が必要。[Remote Control](https://code.claude.com/docs/en/remote-control) |
| 学習利用 | Pro / Max はモデル改善設定が有効なら利用される。Team / Enterprise / API 等は、明示的な提供への同意がない限り学習に使わない。本人設定は未確認。[データ利用](https://code.claude.com/docs/en/data-usage) |

基本表の料金 / API / CLI / IDE / MCP / 指示ファイル / ローカル可否 / データ利用はすべて 2026-09-06 確認。

### 最近の重要更新

- **2026-09-01: Claude Fable 5.1**。Claude Code **2.1.255 以降**で利用可能。API は入力 $10 / 出力 $50 / キャッシュ読込 $0.25（各 1M tokens）、1M コンテキスト。[リリースノート](https://platform.claude.com/docs/en/release-notes/overview) / [利用条件](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- **Fable 5 / 5.1 は Pro では最初から従量クレジット**。Max / Team Premium では週次上限の最大 50% まで包含されるが、別枠の追加 50% ではない。既存の週次使用量と共有する。[プラン別条件](https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan)
- 標準設定では **Pro / Team Standard は Sonnet 5、Max / Team Premium / Anthropic API 等は Opus 5**。組織設定や明示的なモデル指定で変わる。**Sonnet 5 の9月値上げは撤回され、API $2 / $10 が標準価格**になった（8/10 発表）。[モデル設定](https://code.claude.com/docs/en/model-config) / [価格変更](https://platform.claude.com/docs/en/release-notes/overview#august-10-2026)
- 調査時点の公式 changelog 先頭は **2.1.261**。`/skill-doctor` 追加、Remote Control・再開時のコンテキスト等の修正を確認。ローカル導入版は未確認。[公式 changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

## ハーネス適性

- ワークフロー組み込み: 高
- 接続方式: CLI、Agent SDK、MCP、IDE、Remote Control。
- 共通指示: `AGENTS.md` を `CLAUDE.md` から import し、Claude 固有の設定を薄く足す。
- 自動化: `claude -p` と構造化出力を使い、hooks で検証・ログ処理を接続する。プロンプト指示と強制的な権限制御は分ける。
- 課金上の制約: **非対話 `-p` / Agent SDK では、Fable の従量利用確認ダイアログが出ず課金される**。対話での確認を自動処理の予算制御として使わない。[Fable の確認動作](https://code.claude.com/docs/en/model-config)

## 強み

- 長文の構造化。
- 仕様矛盾やレビュー観点の抽出。
- PM / リーダー業務の言語化。
- コードと docs の関係を読み解く作業。

## 弱み

- Claude のチャット等と Claude Code は使用量を共有する。5時間枠に加え有料プランには週次上限があり、長文・並列実行・モデル選択で消費が変わる。[利用上限](https://claude.com/pricing)
- 最新情報は検索や公式確認が必要。
- Claude 固有ファイルへ寄せすぎると他エージェントと共有しにくい。

## 得意用途

- 要件整理。
- 設計レビュー。
- 大きめのコードレビュー。
- ドキュメントの構造整理。

## 苦手用途

- 低コスト大量処理。
- 最新サービス仕様の未確認断定。
- 短い単純作業だけを大量に回す用途。

## 黒澤用途

- ハーネス設計。
- PM判断。
- 技術文書レビュー。
- 実装方針の壁打ち。
- 講座や営業資料の構造化。
- Pro 相当の通常実装・設計レビューと、Fable 5.1 の従量実行を分けて測る。重いタスクで節約できた修正時間と追加費用を比較する。
- [現在の契約](../10_契約/01_現在の契約.md) にある「Claude Code 枠 ¥10,000→¥3,200」は本人記録で、構成・切替完了は未確認。一般向け料金表から実契約を推定しない。

## 検証ログ

### 2026-06-27

- タスク: 初期台帳の評価仮説作成
- 入力: AIカタログ構想、Phase 1 docs
- 結果: 代表的な第一候補として登録
- 理由: 長文設計・レビュー用途で代替しにくい可能性が高い
- 再利用判断: 設計・レビュー・PM判断では第一候補として検証する

### 2026-09-06

- タスク: 公式ドキュメント・料金・リリースノートの調査更新。
- 結果: Fable 5.1 と席種別課金、Sonnet 5 の価格据置、AGENTS.md の取り込み方、CLI / SDK / MCP / Remote Control を確認。
- 未実施: Sonnet 5 / Opus 5 / Fable 5.1 の同一タスク比較、本人の請求・使用量・モデル改善設定の確認。
- 再利用判断: 設計・レビュー・PM判断の第一候補として実測する。機能追加だけでは A へ昇格しない。

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| A候補 | 設計・レビュー用途の中心候補。CLI / SDK による実装自動化も比較対象 | Pro の枠内完了率、Fable 5.1 の追加費用、Codex との手戻り・速度差 |

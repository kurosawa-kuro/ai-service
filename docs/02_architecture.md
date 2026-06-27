# 02 アーキテクチャ（基礎設計）

## 概要

Markdown 台帳を起点に、段階的に検索・自動ルーティングへ育てる成長型カタログ。
最初から DB / Web アプリを作らず、「書き足せること」を最優先にする。

```text
サービス記録 (services/*.md)
  -> 用途別逆引き (usecases/*.md) + 使い分けルール (routing-rules.md)
  -> 評価ログ (evaluations/*.md)
  -> (将来) Supabase 化 -> 検索 (Streamlit/CLI) -> 自動ルーティング
```

## 成長フェーズ

| Phase | 内容 | 状態 |
|---|---|---|
| 1 | Markdown 台帳（services / usecases / evaluations / routing-rules） | 着手対象 |
| 2 | 用途別インデックスで逆引き可能にする | 予定 |
| 3 | 評価ログを蓄積し再利用判断に使う | 予定 |
| 4 | Supabase 化（構造が固まってから） | 将来 |
| 5 | Streamlit / CLI で検索 | 将来 |
| 6 | 自動ルーティング（自作 AI ルーター） | 将来 |

各フェーズは完了を待たず重ねてよい。早すぎる DB 化・Web アプリ化はしない。

## ディレクトリ構成（Phase 1）

```text
catalog/
  ├── services/        # サービス単位の記録 (claude.md, chatgpt.md, ...)
  ├── usecases/        # 用途単位の逆引き (coding.md, research.md, ...)
  ├── evaluations/     # 実タスクの評価ログ (YYYY-MM-<topic>.md)
  └── routing-rules.md # 使い分け判断の正本
```

## 分類軸（能力カテゴリ）

サービス名でなく能力カテゴリで分類する。50〜100 個に増えても破綻しない軸。

```text
01_基盤モデル        09_画像生成
02_チャットAI        10_動画生成
03_検索・リサーチ     11_音声・音楽
04_コーディングエージェント  12_プレゼン・資料
05_CLI・IDE・ハーネス  13_PM・業務自動化
06_APIルーター・推論基盤  14_ブラウザ操作・自律実行
07_ローカルLLM        15_評価・監視・セキュリティ
08_RAG・ナレッジDB     16_トレード調査・市場分析
```

## 記録フォーマット（評価軸の固定）

各 `services/*.md` は同一フォーマットで記録し、横比較可能にする。

- 基本: 種別（無料/有料/ローカル）・主用途・月額・無料枠・API/CLI/IDE/MCP/AGENTS.md 対応・ローカル可否
- ハーネス適性: ワークフローに組み込めるか（最重要軸）
- 強み / 弱み / 黒澤用途
- 検証ログ（日付つき）・継続評価（A/B/C と理由）

用途ページ `usecases/*.md` は「第一候補 / 低コスト補助 / ローカル検証 / 判断ルール / 破綻条件」を持つ。

## 構成要素

| 構成要素 | 役割 | 担当パス |
|---|---|---|
| サービス台帳 | サービス単位の記録 | `catalog/services/` |
| 用途逆引き | 用途から候補を引く | `catalog/usecases/` |
| 評価ログ | 実タスクの結果・再利用判断 | `catalog/evaluations/` |
| ルーティングルール | 使い分け判断の正本 | `catalog/routing-rules.md` |
| エージェントガイド | Codex / 他エージェント向けの repo ガイド | `AGENTS.md` |
| Claude ガイド | Claude Code の司令ルール | `CLAUDE.md` |
| タスク文書 | 一回性の作業計画・実装タスク | `docs/tasks/` |
| Claude skills | Claude Code で繰り返し使う作業手順 | `.claude/skills/` |

## 境界

- カタログ本体は `catalog/` 配下に置く（コードが伴う場合のソースは `src/`）。
- 非機密の設定は `env/config.yaml` に置く。
- ローカル秘密情報は ignore したまま。共有・本番の秘密情報は Doppler などの secret manager に置く。
- カタログには実在のアカウント情報・API キー・個人データを書かない（評価とスペックのみ）。
- Codex が `.claude/rules/` や `.claude/skills/` を読む前提にしない。永続させたい指針は `AGENTS.md` に置く。

## 関連タスク

- 構造変更、責務移動、adapter 追加、共通化は、実装前に `docs/tasks/active/` へ task を作る。
- 中規模以上の変更では、task に Skeleton / Plan / Acceptance Criteria を書いてから実装する。
- Phase 4 以降（Supabase 化・検索・自動ルーティング）は確定時に `docs/adr/` へ判断を昇格する。

# coding

## 第一候補

- Claude Code
- Codex / Codex CLI
- Aider
- Cline
- GitHub Copilot
- Cursor

## 低コスト補助

- DeepSeek
- Qwen
- OpenCode

## ローカル検証

- Ollama + Qwen系
- Ollama + DeepSeek系
- LM Studio

## 判断ルール

- 大規模リファクタリング: Claude Code / Codex
- 局所修正 / Git差分前提: Aider
- VS Code内エージェント実験: Cline
- IDE内補完: GitHub Copilot
- エージェント実験: Cursor / Cline / Aider / OpenCode
- 安価な雑レビュー: DeepSeek / Qwen
- 機密に近い内容: ローカル or 契約上許可された環境
- 仕様や docs と実装を同時に動かす作業: Codex / Claude Code
- コードベース理解が必要なレビュー: Claude Code / Codex
- 単発の関数補完: GitHub Copilot / Cursor
- 既存プロジェクトで複数AIを使う場合: 役割を分け、同じファイルを同時に触らせない

## 破綻条件

- 同じファイルを複数AIに同時修正させる。
- `AGENTS.md` や rules なしで広い変更を任せる。
- 差分レビューなしでマージする。
- コーディングAIを「コード生成」として一括りにし、補完 / チャット / 差分修正 / CLI実行 / レビュー / テスト生成 / MCP接続を区別しない。

## 関連評価ログ

- `src/evaluations/README.md`
- `src/evaluations/2026-06-coding-agent-comparison-plan.md`

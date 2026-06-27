"""Markdown templates for Phase 1 catalog records."""

from __future__ import annotations

from datetime import date

from .categories import category_labels


def service_template(name: str, category: str | None = None) -> str:
    selected_category = category or "TODO"
    categories = "\n".join(f"- {label}" for label in category_labels())
    today = date.today().isoformat()

    return f"""# {name}

## 基本

| 項目 | 内容 |
|---|---|
| 提供会社 | TODO |
| 能力カテゴリ | {selected_category} |
| 種別 | TODO（無料 / 有料 / ローカル） |
| 主用途 | TODO |
| 月額 | TODO |
| 無料枠 | TODO |
| API | TODO（可 / 不可 / 未確認） |
| CLI | TODO（可 / 不可 / 未確認） |
| IDE | TODO（可 / 不可 / 未確認） |
| MCP | TODO（可 / 不可 / 未確認） |
| AGENTS.md / rules / hooks 対応 | TODO（可 / 不可 / 未確認） |
| ローカル可否 | TODO（可 / 不可 / 未確認） |

## ハーネス適性

- ワークフロー組み込み: TODO
- 接続方式: TODO
- 制約: TODO

## 強み

- TODO

## 弱み

- TODO

## 得意用途

- TODO

## 苦手用途

- TODO

## 黒澤用途

- TODO

## 検証ログ

### {today}

- タスク: TODO
- 入力: TODO
- 結果: TODO
- 理由: TODO
- 再利用判断: TODO

## 継続評価

| 評価 | 理由 | 観察ポイント |
|---|---|---|
| TODO（A / B / C） | TODO | TODO |

## 能力カテゴリ候補

{categories}
"""


def usecase_template(name: str) -> str:
    return f"""# {name}

## 第一候補

- TODO

## 低コスト補助

- TODO

## ローカル検証

- TODO

## 判断ルール

- TODO

## 破綻条件

- TODO

## 関連評価ログ

- TODO
"""


def evaluation_template(topic: str, evaluated_on: date | None = None) -> str:
    day = evaluated_on or date.today()

    return f"""# {day.isoformat()} {topic}

## タスク

TODO

## 入力

TODO

## 使用サービス / 技術

- TODO

## 結果

TODO

## 理由

TODO

## 再利用判断

TODO

## 次回へのメモ

- TODO
"""


def routing_rules_template() -> str:
    return """# routing-rules

用途から AI サービス / 技術を選ぶための使い分け判断の正本。

## 基本方針

- 能力カテゴリ、用途、ハーネス適性、評価ログを根拠に選ぶ。
- 印象評価だけでルーティングしない。
- 機密に近い内容はローカル実行または契約上許可された環境に限定する。

## ルール

| 用途 | 第一候補 | 低コスト補助 | ローカル検証 | 判断ルール | 破綻条件 |
|---|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO | TODO |
"""

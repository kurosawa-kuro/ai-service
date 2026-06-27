"""Canonical capability categories for the catalog."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Category:
    code: str
    name: str

    @property
    def label(self) -> str:
        return f"{self.code}_{self.name}"


CATEGORIES: tuple[Category, ...] = (
    Category("01", "基盤モデル"),
    Category("02", "チャットAI"),
    Category("03", "検索・リサーチ"),
    Category("04", "コーディングエージェント"),
    Category("05", "CLI・IDE・ハーネス"),
    Category("06", "APIルーター・推論基盤"),
    Category("07", "ローカルLLM"),
    Category("08", "RAG・ナレッジDB"),
    Category("09", "画像生成"),
    Category("10", "動画生成"),
    Category("11", "音声・音楽"),
    Category("12", "プレゼン・資料"),
    Category("13", "PM・業務自動化"),
    Category("14", "ブラウザ操作・自律実行"),
    Category("15", "評価・監視・セキュリティ"),
    Category("16", "トレード調査・市場分析"),
)


def category_labels() -> list[str]:
    return [category.label for category in CATEGORIES]


def is_valid_category(label: str) -> bool:
    return label in category_labels()

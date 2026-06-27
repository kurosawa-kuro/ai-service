from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from ai_catalog.catalog import (
    CatalogError,
    create_evaluation,
    create_service,
    create_usecase,
    init_catalog,
)


class CatalogTest(unittest.TestCase):
    def test_init_catalog_creates_phase1_structure(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            init_catalog(root)

            self.assertTrue((root / "catalog" / "services").is_dir())
            self.assertTrue((root / "catalog" / "usecases").is_dir())
            self.assertTrue((root / "catalog" / "evaluations").is_dir())
            self.assertTrue((root / "catalog" / "routing-rules.md").is_file())

    def test_create_service_uses_required_sections(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            result = create_service(root, "Claude Code", category="04_コーディングエージェント")

            self.assertEqual(result.path, root / "catalog" / "services" / "claude-code.md")
            content = result.path.read_text(encoding="utf-8")
            self.assertIn("| 提供会社 | TODO |", content)
            self.assertIn("| 能力カテゴリ | 04_コーディングエージェント |", content)
            self.assertIn("| AGENTS.md / rules / hooks 対応 | TODO", content)
            self.assertIn("## ハーネス適性", content)
            self.assertIn("## 得意用途", content)
            self.assertIn("## 苦手用途", content)
            self.assertIn("## 検証ログ", content)
            self.assertIn("## 継続評価", content)

    def test_create_service_rejects_unknown_category(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            with self.assertRaises(CatalogError):
                create_service(Path(temporary_directory), "Unknown", category="99_その他")

    def test_create_usecase_uses_decision_sections(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            result = create_usecase(root, "coding")

            content = result.path.read_text(encoding="utf-8")
            self.assertIn("## 第一候補", content)
            self.assertIn("## 低コスト補助", content)
            self.assertIn("## ローカル検証", content)
            self.assertIn("## 判断ルール", content)
            self.assertIn("## 破綻条件", content)

    def test_create_usecase_allows_japanese_filename(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            result = create_usecase(root, "検索 リサーチ")

            self.assertEqual(result.path, root / "catalog" / "usecases" / "検索-リサーチ.md")

    def test_create_evaluation_uses_month_topic_filename(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)

            result = create_evaluation(root, "routing check", evaluated_on=date(2026, 6, 27))

            self.assertEqual(
                result.path,
                root / "catalog" / "evaluations" / "2026-06-routing-check.md",
            )
            content = result.path.read_text(encoding="utf-8")
            self.assertIn("## タスク", content)
            self.assertIn("## 入力", content)
            self.assertIn("## 結果", content)
            self.assertIn("## 理由", content)
            self.assertIn("## 再利用判断", content)

    def test_existing_files_are_not_overwritten_by_default(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            create_usecase(root, "research")

            with self.assertRaises(CatalogError):
                create_usecase(root, "research")


if __name__ == "__main__":
    unittest.main()

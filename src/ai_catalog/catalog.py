"""Filesystem operations for the Markdown catalog."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .categories import is_valid_category
from .templates import (
    evaluation_template,
    routing_rules_template,
    service_template,
    usecase_template,
)


CATALOG_DIRS = ("services", "usecases", "evaluations")


class CatalogError(ValueError):
    """Raised when a catalog operation cannot be completed."""


@dataclass(frozen=True)
class CreatedFile:
    path: Path
    created: bool


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"[^\w._-]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug).strip("-._")
    if not slug:
        raise CatalogError("name must contain at least one filename-safe character")
    return slug


def catalog_root(root: Path) -> Path:
    return root / "catalog"


def init_catalog(root: Path, force: bool = False) -> list[CreatedFile]:
    catalog = catalog_root(root)
    created: list[CreatedFile] = []

    for directory in CATALOG_DIRS:
        path = catalog / directory
        already_exists = path.exists()
        path.mkdir(parents=True, exist_ok=True)
        created.append(CreatedFile(path=path, created=not already_exists))

    routing_rules = catalog / "routing-rules.md"
    created.append(write_file(routing_rules, routing_rules_template(), force=force))
    return created


def create_service(
    root: Path,
    name: str,
    category: str | None = None,
    force: bool = False,
) -> CreatedFile:
    if category is not None and not is_valid_category(category):
        raise CatalogError(f"unknown category: {category}")

    path = catalog_root(root) / "services" / f"{slugify(name)}.md"
    return write_file(path, service_template(name=name, category=category), force=force)


def create_usecase(root: Path, name: str, force: bool = False) -> CreatedFile:
    path = catalog_root(root) / "usecases" / f"{slugify(name)}.md"
    return write_file(path, usecase_template(name=name), force=force)


def create_evaluation(
    root: Path,
    topic: str,
    evaluated_on: date | None = None,
    force: bool = False,
) -> CreatedFile:
    day = evaluated_on or date.today()
    filename = f"{day.strftime('%Y-%m')}-{slugify(topic)}.md"
    path = catalog_root(root) / "evaluations" / filename
    return write_file(path, evaluation_template(topic=topic, evaluated_on=day), force=force)


def write_file(path: Path, content: str, force: bool = False) -> CreatedFile:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not force:
        raise CatalogError(f"file already exists: {path}")
    created = not path.exists()
    path.write_text(content, encoding="utf-8")
    return CreatedFile(path=path, created=created)

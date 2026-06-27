"""Command line interface for the AI service catalog."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence

from .catalog import (
    CatalogError,
    create_evaluation,
    create_service,
    create_usecase,
    init_catalog,
)
from .categories import category_labels


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-catalog",
        description="Maintain the Phase 1 Markdown AI service catalog.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="project root that contains catalog/ (default: current directory)",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create Phase 1 catalog structure")
    init_parser.add_argument("--force", action="store_true", help="overwrite routing-rules.md")

    categories_parser = subparsers.add_parser("categories", help="print capability categories")
    categories_parser.set_defaults(handler=handle_categories)

    service_parser = subparsers.add_parser("new-service", help="create a service record")
    service_parser.add_argument("name", help="service name")
    service_parser.add_argument("--category", choices=category_labels(), help="capability category")
    service_parser.add_argument("--force", action="store_true", help="overwrite existing file")

    usecase_parser = subparsers.add_parser("new-usecase", help="create a usecase page")
    usecase_parser.add_argument("name", help="usecase name")
    usecase_parser.add_argument("--force", action="store_true", help="overwrite existing file")

    evaluation_parser = subparsers.add_parser("new-evaluation", help="create an evaluation log")
    evaluation_parser.add_argument("topic", help="evaluation topic")
    evaluation_parser.add_argument(
        "--date",
        dest="evaluated_on",
        type=date.fromisoformat,
        help="evaluation date in YYYY-MM-DD format",
    )
    evaluation_parser.add_argument("--force", action="store_true", help="overwrite existing file")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "init":
            results = init_catalog(root=args.root, force=args.force)
        elif args.command == "categories":
            return handle_categories()
        elif args.command == "new-service":
            results = [
                create_service(
                    root=args.root,
                    name=args.name,
                    category=args.category,
                    force=args.force,
                )
            ]
        elif args.command == "new-usecase":
            results = [create_usecase(root=args.root, name=args.name, force=args.force)]
        elif args.command == "new-evaluation":
            results = [
                create_evaluation(
                    root=args.root,
                    topic=args.topic,
                    evaluated_on=args.evaluated_on,
                    force=args.force,
                )
            ]
        else:
            parser.error(f"unknown command: {args.command}")
            return 2
    except CatalogError as error:
        parser.exit(status=1, message=f"error: {error}\n")

    for result in results:
        action = "created" if result.created else "updated"
        print(f"{action}: {result.path}")
    return 0


def handle_categories() -> int:
    for label in category_labels():
        print(label)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

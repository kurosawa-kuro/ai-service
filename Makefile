.PHONY: setup build run dev test fmt lint catalog-init categories clean

# Application
APP_NAME := ai-service
PYTHON ?= python3
PYTHONPATH := src

# 初期セットアップ
setup: build
	@echo "Setup complete."

# ビルド
build:
	@$(PYTHON) -m compileall -q src

# 実行
run:
	@PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m ai_catalog --help

# 開発
dev: run

# catalog/ 初期化
catalog-init:
	@PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m ai_catalog init

# テスト
test:
	@PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tests

# 能力カテゴリ一覧
categories:
	@PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m ai_catalog categories

# 整形
fmt:
	@$(PYTHON) -m compileall -q src tests

# 静的解析
lint:
	@PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tests

# クリーンアップ
clean:
	@find src tests -type d -name __pycache__ -prune -exec rm -rf {} +

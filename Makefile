.PHONY: install test build clean

install:
	pip install -e .

test:
	python -m pytest tests/

build-windows:
	python sniffer_tool/build.py windows

build-linux:
	python sniffer_tool/build.py linux

build-mac:
	python sniffer_tool/build.py mac

build-all:
	python sniffer_tool/build.py

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
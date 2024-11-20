SHELL := /bin/bash
TEST_DIR := $(shell pwd)/tests
RUST_DIR := $(shell pwd)/rust-shared
all:
	gcc -fprofile-arcs -ftest-coverage -o tests/add.so -shared add.c
	pushd rust-shared && cargo build && cp $(RUST_DIR)/target/release/librust_shared.so $(TEST_DIR) && popd	
pytest:
	pip install -r requirements.txt 
	pytest $(TEST_DIR) --cov=wrapper --cov-report=html
	lcov --capture --directory . --output-file coverage.info
	genhtml coverage.info --output-directory out

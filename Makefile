SHELL := /bin/bash

CYAN_COLOR := \033[34;1m
NO_COLOR := \033[0m
ANSIBLE_DIR := ansible
BASH_DIR := scripts
 
.PHONY: help apply format
.DEFAULT_GOAL := help
 
help: ## show this help
    @grep -E "^[a-zA-Z_-]+.*: ## .*$$" $(MAKEFILE_LIST) | sort | awk 'BEGIN { FS=": ##"}{ printf "$(CYAN_COLOR)%-20s$(NO_COLOR)%s\n", $$1, $$2 }'
 
format: ## format and validate terraform configuration
	@bash $(BASH_DIR)/fmt_valid.sh
 
apply: ## apply terraform configuration
	@bash $(BASH_DIR)/apply.sh
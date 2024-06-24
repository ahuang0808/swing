POETRY_RUN := poetry run
DOT_ENV := DJANGO_READ_DOT_ENV_FILE=True
DJANGO_MANAGE := $(DOT_ENV) $(POETRY_RUN) python manage.py
DJANGO_ADMIN := $(DOT_ENV) $(POETRY_RUN) django-admin

.DEFAULT_GOAL := help

help:  ## print this help
	@# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo ""
.PHONY: help

up:    ## run site
	$(DJANGO_MANAGE) runserver 0.0.0.0:8000
.PHONY: up

release    ## release
.PHONY: release

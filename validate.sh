#!/usr/bin/env bash
set -ex
pipenv run pytest tests
pipenv run mypy --config-file mypy.ini isseven tests
pipenv run black --check isseven tests
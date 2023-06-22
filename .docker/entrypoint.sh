#!/bin/bash

pdm install
pdm run python src/core/invoice/infra/migrations/migrate.py
tail -f /dev/null
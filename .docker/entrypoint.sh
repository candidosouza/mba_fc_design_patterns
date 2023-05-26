#!/bin/bash

pdm install
pdm run python migrate.py
tail -f /dev/null
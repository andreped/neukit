#!/bin/bash
isort --sl neukit app.py
black --line-length 80 neukit app.py
flake8 neukit app.py

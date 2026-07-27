#!/usr/bin/env python3
from build_docs import build_docs
from utils.container import run_in_playwright_container

if __name__ == "__main__":
    build_docs()
    run_in_playwright_container(
        "npm install && npm exec --no -- playwright test --update-snapshots"
    )

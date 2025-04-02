#!/usr/bin/env python3
from subprocess import run

from build import build

if __name__ == "__main__":
    build()
    run("uv publish", check=True, shell=True)

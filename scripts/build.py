#!/usr/bin/env python3
from subprocess import run


def build():
    run(["npm", "run", "build"], check=True, shell=True)
    run(["uv", "build"], check=True, shell=True)


if __name__ == "__main__":
    build()

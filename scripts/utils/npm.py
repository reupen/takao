#!/usr/bin/env python3
from json import load


def get_dependency_version(package):
    with open("package-lock.json") as file:
        lockfile_data = load(file)

    return lockfile_data["dependencies"][package]["version"]

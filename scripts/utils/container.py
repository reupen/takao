import os
from pathlib import PurePath
from platform import system
from subprocess import run

from .npm import get_dependency_version

IS_WINDOWS = system() == "Windows"
ROOT_DIR = PurePath(__file__).parents[2]
CONTAINER_RUNNER = os.environ.get(
    "CONTAINER_RUNNER", "wslc" if IS_WINDOWS else "podman"
)


def run_in_playwright_container(arg):
    playwright_version = get_dependency_version("node_modules/@playwright/test")
    command = [
        CONTAINER_RUNNER,
        "run",
        "--rm",
        "-v",
        f"{ROOT_DIR.as_posix()}:/home/pwuser/",
        "-v",
        f"{ROOT_DIR.name}:/home/pwuser/node_modules/",
        "-v",
        f"{ROOT_DIR.name}-npm-cache:/home/pwuser/.npm/",
        "-w",
        "/home/pwuser/",
        "-it",
        "-e",
        "CI",
        f"mcr.microsoft.com/playwright:v{playwright_version}",
        "bash",
        "-c",
        arg,
    ]
    run(command, check=True, shell=IS_WINDOWS)

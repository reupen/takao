#!/usr/bin/env python3
import json
import os
import sys
from pathlib import PurePath
from subprocess import run

import xmltodict
from sphinx.cmd.build import main


def convert_sitemap_to_json():
    with open("docs/build/html/pages.xml", "rb") as sitemap_xml:
        pages = xmltodict.parse(sitemap_xml)

    with open("docs/build/html/pages.json", "w", encoding="utf-8") as sitemap_json:
        json.dump(pages, sitemap_json, indent=2)


def build_docs(*args):
    os.chdir(PurePath(__file__).parents[1])
    run("npm run build", check=True, shell=True)
    main(["-a", "-D", "html_baseurl=/", *args, "docs/source", "docs/build/html"])
    convert_sitemap_to_json()


if __name__ == "__main__":
    build_docs(*sys.argv[1:])

#!/usr/bin/python3

import argparse
from lib.build import run_build
from lib.clean import run_clean
from lib.add import run_add
from lib.launch import run_launch

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

build = subparsers.add_parser("build", help="Build to dist")
build.add_argument("--version")
build.add_argument("--export")
build.set_defaults(func=run_build)

clean = subparsers.add_parser("clean", help="Delete dist folder")
clean.set_defaults(func=run_clean)

add = subparsers.add_parser("add", help="Add entry to manifest")
add.add_argument("item_name")
add.add_argument("new_name")
add.set_defaults(func=run_add)

launch = subparsers.add_parser("launch", help="Build and export dist to minecraft dir")
launch.add_argument("-p", "--prod", action="store_true")
launch.set_defaults(func=run_launch)

args = parser.parse_args()

print(args)

if __name__ == "__main__":
    if "func" in args:
        args.func(args)

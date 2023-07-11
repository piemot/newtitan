from pathlib import Path
import tomlkit as toml
import schema
import os
import shutil as sh

from lib.build import run_build
from lib.shared import get_pack_name

DIST = Path("dist")


def run_launch(args):
    with open("config.toml", "rb") as f:
        config = toml.parse(f.read())

    x = schema.Schema({"minecraft_dir": str, schema.Optional(str): object})
    x.validate(dict(config.unwrap()))

    run_build(object())

    targetdir = Path(
        config["minecraft_dir"], "resourcepacks", get_pack_name(not args.prod)
    )

    if os.path.exists(targetdir):
        sh.rmtree(targetdir)

    sh.copytree(DIST, targetdir)

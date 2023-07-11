from pathlib import Path
import shutil as sh
import os
import json

from lib.shared import AppError, open_manifest
from lib.maps import model_map, custom_model_map

DIST = Path("dist")
ASSETS = Path("assets")
META = Path("meta")

manifest = open_manifest()


def gen_models():
    for item in manifest:
        print(item, manifest[item])

        MODEL = DIST / Path("assets", "minecraft", "models")

        model_type = get_model(item)

        model = model_map[model_type](item)

        model_path = Path(MODEL, model["path"])

        if not os.path.exists(model_path):
            os.makedirs(model_path)

        content = model["meta"].copy()
        content["overrides"] = [
            {
                "predicate": {"custom_model_data": custom_item["data"]},
                "model": f"titan:{model['path']}/{custom_item['id']}",
            }
            for custom_item in manifest[item]
        ]

        with open(model_path / f"{item}.json", "w+") as f:
            json.dump(content, f)


def gen_custom_models():
    for item in manifest:
        print(item, manifest[item])

        MODEL = DIST / Path("assets", "titan", "models")

        model_type = get_model(item, True)

        for custom_item in manifest[item]:
            model = custom_model_map[model_type](custom_item["id"])

            model_path = Path(MODEL, model["path"])
            if not os.path.exists(model_path):
                os.makedirs(model_path)

            content = model["meta"].copy()

            with open(model_path / f"{custom_item['id']}.json", "w+") as f:
                json.dump(content, f)


def gen_textures():
    for item in manifest:
        MODEL = DIST / Path("assets", "titan", "textures")

        model_type = get_model(item, True)

        for custom_item in manifest[item]:
            model = custom_model_map[model_type](custom_item["id"])

            model_path = Path(MODEL, model["path"])
            if not os.path.exists(model_path):
                os.makedirs(model_path)

            item_path = f"{custom_item['id']}.png"

            try:
                sh.copy(ASSETS / item_path, model_path / item_path)
            except FileNotFoundError:
                raise AppError(f"Asset file at {ASSETS / item_path} does not exist")


def get_model(item: str, custom: bool = False):
    try:
        model_type = [
            type
            for type in list((custom_model_map if custom else model_map).keys())
            if item.endswith(type)
        ][0]
    except IndexError:
        raise AppError(f"Cannot find {'custom ' if custom else ''}model for {item}")

    return model_type


def run_build(args):
    VERSION_STR = f"§9v{args.version}" if args.version else "§4§l§nDEV"
    
    if args.export: 
        global DIST
        DIST = Path(args.export)

    if os.path.exists(DIST):
        sh.rmtree(DIST)

    os.mkdir(DIST)

    sh.copy(META / "pack.png", DIST / "pack.png")
    sh.copy("LICENSE", DIST / "LICENSE")

    with open(DIST / "pack.mcmeta", "w+") as f:
        with open(META / "pack.mcmeta", "r") as old_file:
            text = old_file.readlines()
        f.writelines(
            map(
                lambda l: l.replace("{version}", VERSION_STR)
                if "{version}" in l
                else l,
                text,
            )
        )

    gen_models()
    gen_custom_models()
    gen_textures()

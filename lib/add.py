import tomlkit as toml

from lib.shared import open_manifest

manifest = open_manifest()


def run_add(args):
    item_name = args.item_name
    new_name = args.new_name

    if item_name in manifest:
        item = manifest[item_name]
        new_id = max(map(lambda x: x["data"], item)) + 1
        item.append({"data": new_id, "id": new_name})
    else:
        manifest[item_name] = [{"data": 1, "id": new_name}]

    with open("manifest.toml", "w") as f:
        toml.dump(manifest, f)

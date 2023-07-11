import tomlkit as toml
import schema


class AppError(Exception):
    pass


def open_manifest():
    with open("manifest.toml", "rb") as f:
        manifest = toml.parse(f.read())

    x = schema.Schema(schema.Or({str: [{"id": str, "data": int}]}, {}))
    x.validate(dict(manifest.unwrap()))

    return manifest


def get_pack_name(dev: bool = True):
    return "TitanBox Dev" if dev else "TitanBox"

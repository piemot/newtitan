model_map = {
    "_axe": lambda itemname: {
        "path": "item",
        "meta": {
            "parent": "item/handheld",
            "textures": {"layer0": f"item/{itemname}"},
        },
    },
    "_sword": lambda itemname: {
        "path": "item",
        "meta": {
            "parent": "item/handheld",
            "textures": {"layer0": f"item/{itemname}"},
        },
    },
}

custom_model_map = {
    "_axe": lambda itemname: {
        "path": "item",
        "meta": {
            "parent": "item/handheld",
            "textures": {"layer0": f"titan:item/{itemname}"},
        },
    },
    "_sword": lambda itemname: {
        "path": "item",
        "meta": {
            "parent": "item/handheld",
            "textures": {"layer0": f"titan:item/{itemname}"},
        },
    },
}

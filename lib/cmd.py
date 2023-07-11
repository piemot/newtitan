from lib.shared import open_manifest

manifest = open_manifest()

def run_cmd(props):
    selector = "@p" if props.player else "@s"
    for i in manifest:
        for item in manifest[i]:
            if item["id"] == props.item_name:
                print(f"/give {selector} {i}{{CustomModelData:{item['data']}}}")
                return

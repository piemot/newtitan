<div align="center">
  <a href="https://github.com/piemot/newtitan">
    <img src="meta/pack.png" alt="Pack icon" width="80" height="80">
  </a>

[![Issues](https://img.shields.io/github/license/piemot/newtitan?logo=logo&style=for-the-badge)](./LICENSE)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/piemot/newtitan?sort=semver&include_prereleases&style=for-the-badge)](https://github.com/piemot/newtitan/releases)

  <h1>TitanBox Textures</h1>
  <h3>The custom texture pack for the TitanBox server</h3>
  <br />
  <p>
    <a href="https://github.com/piemot/newtitan"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/piemot/newtitan/issues">Report Bug</a>
    ·
    <a href="https://github.com/piemot/newtitan/issues">Request Feature</a>
  </p>
</div>

## Installation

Client-side installation is good for development,
but in production the texture pack should be added to the server.

### Client-side

1. Select your preferred version of the pack from the Releases.

1. Unzip `Titan.zip` and place it in your Resource Packs directory.

1. Select it in the Resource Packs menu.

_Generally, the latest release will be the only one supported._

[![All Releases](https://img.shields.io/badge/All%20Releases-blue?style=for-the-badge)](https://github.com/piemot/newtitan/releases)
[![Latest Release](https://img.shields.io/github/v/release/piemot/newtitan?sort=semver&include_prereleases&style=for-the-badge&label)](https://github.com/piemot/newtitan/releases/latest)

### Server-side

1. Open your `server.properties` file.
1. Set `resource-pack` to `https://github.com/piemot/newtitan/releases/download/latest/Titan.zip`.
1. You may require users to download the texture pack by setting the `require-resource-pack` property to `true`.
1. Restart your server to apply the changes.

_If needed, you can lock your server's resource pack version by substituting `latest` for a SemVer version,
f.e. `https://github.com/piemot/newtitan/releases/download/v0.0.1/Titan.zip`._

## Usage

A map of items and Custom Model Data numbers can be found in the [manifest](./manifest.toml).
`data` is the value of `CustomModelData`, an NBT tag that must be applied to an item for it to have a custom texture.
For instance, the item listing `"birch_leaf_axe"` is recorded as such:

````toml
[[wooden_axe]]
data = 2
id = "birch_leaf_axe"```
To get it, you need to get a `wooden_axe` with a `CustomModelData` of `2`. A command for this would be:
````

/give @s minecraft:wooden_axe{CustomModelData:2}

```

## Local Development

`x.py` is a utility script for generating and managing the texture pack.
I recommend generating a venv to manage dependencies.

Some scripts require a `config.toml` file to be populated in the root directory;
an example can be found at [config.toml](./config.toml).

### minecraft_directory

The directory your Minecraft instance is in:

- Windows: `%appdata%/.minecraft`,
- Mac: `~/Library/Application Support/minecraft`,
- Linux: `~/.minecraft`

## Versioning

Releases must be SemVer format compatible, but we do not strictly adhere to the SemVer standard.

## Authors

- 01110000

## License

This project is licensed under the GPLv3 License - see the [LICENSE file](./LICENSE) for details.
```

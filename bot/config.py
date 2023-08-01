import tomllib
from dataclasses import dataclass
import pathlib


@dataclass(frozen=True)
class discord_config:
    key: str
    owner_ids: list[int]
    commands_module: str


dir_path = pathlib.Path(__file__).parent
# this is the polyelo/bot directory

with open(dir_path.joinpath("config.toml"), "rb") as f:
    data = tomllib.load(f)
    config = discord_config(**data['discord'])

    if config.key == "YOUR API KEY HERE":
        raise ValueError("You forgot to put your bot's api key in config.toml.")

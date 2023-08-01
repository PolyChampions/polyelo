# Copyright (c) 2023 PolyELO Bot development team. This file is licensed under the terms of the GPL License,
# version 3.0. More details can be found with the LICENSE file at the root of the repository.
#
# Main entry point to the bot, which is launched via the command `python -m bot`

import nextcord
from nextcord.ext import commands
from bot.config import config


class PolyELOBot(commands.Bot):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    async def on_ready(self):
        print(f"logged in: {self.user.name} ({self.user.id})")


def main():
    bot = PolyELOBot(owner_ids=config.owner_ids)
    bot.load_extensions_from_module(config.commands_module)
    # TODO
    bot.run(config.key)


if __name__ == '__main__':
    main()

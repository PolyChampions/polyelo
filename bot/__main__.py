# Copyright (c) 2023 PolyELO Bot development team. This file is licensed under the terms of the GPL License,
# version 3.0. More details can be found with the LICENSE file at the root of the repository.
#
# Main entry point to the bot, which is launched via the command `python -m bot`

import nextcord
from nextcord.ext import commands


class PolyELOBot(commands.Bot):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)

    def on_ready(self):
        print(f"logged in: {self.user.name} ({self.user.id})")


def main():
    bot = PolyELOBot()
    # TODO
    bot.run()


if __name__ == '__main__':
    main()

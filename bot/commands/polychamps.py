from nextcord.ext import commands


class pc_cog(commands.Cog):
    ...


def setup(bot: commands.Bot, **kwargs):
    bot.add_cog(pc_cog(**kwargs))

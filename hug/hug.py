import discord
from redbot.core import commands, Config
import random

class hug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=1234567890)
        default_guild = {"hug_counter": 0}
        self.config.register_guild(**default_guild)
        self.gifs = [
            "https://media.giphy.com/media/od5H3PmEG5EVq/giphy.gif",
            "https://media.giphy.com/media/u9BxQbM5bxvwY/giphy.gif",
            "https://media1.giphy.com/media/lrr9rHuoJOE0w/giphy.gif?cid=ecf05e47pwt7i8zqysdj0q3qzv41n2b6pc4uphk4du21mf4i&rid=giphy.gif",
            "https://media1.giphy.com/media/du8yT5dStTeMg/giphy.gif?cid=ecf05e47l52y8u7meoxxkd0iunvkn87zbf6mudc7h0k6zwu4&rid=giphy.gif"
        ]

    @commands.command()
    async def hug(self, ctx, user: discord.Member):
        """Hugs a user."""
        gif_url = random.choice(self.gifs)
        await self.config.guild(ctx.guild).hug_counter.set(await self.config.guild(ctx.guild).hug_counter() + 1)
        hug_count = await self.config.guild(ctx.guild).hug_counter()
        embed = discord.Embed(title=f"{ctx.author.name} hugs {user.name}!", description=f"Total hugs: {hug_count}", color=0xff69b4)
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(hug(bot))

import discord
from discord.ext import commands
import random
from redbot.core import Config

class Kiss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.gifs = [
            "https://media.giphy.com/media/bm2O3nXTcKJeU/giphy.gif",
            "https://media.giphy.com/media/G3va31oEEnIkM/giphy.gif",
            "https://media.giphy.com/media/MQVpBqASxSlFu/giphy.gif",
            "https://media.giphy.com/media/11rWoZNpAKw8w/giphy.gif",
            "https://media.giphy.com/media/gTLfgIRwAiWOc/giphy.gif",
            "https://media.giphy.com/media/12VXIxKaIEarL2/giphy.gif",
            "https://media.giphy.com/media/QGc8RgRvMonFm/giphy.gif"
        ]
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_guild(kiss_counter=0)

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        """Kiss someone C:"""
        gif_url = random.choice(self.gifs)
        
        kiss_count = await self.config.guild(ctx.guild).kiss_counter()
        await self.config.guild(ctx.guild).kiss_counter.set(kiss_count + 1)

        kisser = ctx.author.display_name
        kissed_member = member.display_name

        embed = discord.Embed(
            title=f"{kisser} kissed {kissed_member}!",
            color=discord.Color.blue()
        )
        embed.set_image(url=gif_url)
        embed.set_footer(text=f"{ctx.author.name} has given {kiss_count + 1} kisses so far.")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Hug(bot))

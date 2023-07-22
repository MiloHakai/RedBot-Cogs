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
        self.config = Config.get_conf(self, identifier=1234567890, force_registration=True)
        self.config.register_guild(hug_counter=0)

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        """Hug someone!"""
        gif_url = random.choice(self.gifs)
        
        hug_count = await self.config.guild(ctx.guild).hug_counter()
        await self.config.guild(ctx.guild).hug_counter.set(hug_count + 1)
        
        hugger = escape_mentions(ctx.author.mention)
        hugged_member = escape_mentions(member.mention)
        
        embed = discord.Embed(
            title=f"{hugger} hugged {hugged_member}!",
            color=discord.Color.purple()
        )
        embed.set_image(url=gif_url)
        embed.set_footer(text=f"{ctx.author.name} has given {hug_count + 1} hugs so far.")
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Hug(bot))

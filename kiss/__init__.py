from .kiss import kiss

__red_end_user_data_statement__ = "This cog does not persistentily store data or metadata about users."


async def setup(bot):
    await bot.add_cog(kiss(bot))

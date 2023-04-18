import discord
import enter_token_here

bot = discord.Bot()

@bot.slash_command()
async def activer(ctx):
    """
    simple slash command for activate badge.
    """
    await ctx.respond("""Voilà
Vérifie si t'es éligible ici : <https://discord.com/developers/active-developer>.
Cela prend généralement 24h.
Le serveur du bot doit être en mode communauté et les messages developpeurs activés dans un channel spécifique.
Toute informations complémentaires sont disponibles ici : <https://support-dev.discord.com/hc/en-us/articles/10113997751447-Active-Developer-Badge>
""")


    
bot.run(enter_token_here.TOKEN)
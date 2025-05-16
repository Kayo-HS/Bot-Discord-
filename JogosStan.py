import discord
from discord.ext import commands

@commands.command()
async def jogos(ctx:commands.Context):
    embed = discord.Embed(title="Vamos no divertir", description= "Escolha uma opção:", color=discord.Color.blue())
    embed.add_field(name= "Opção 1:", value= "Pedra, papel e tesoura", inline=False)
    embed.add_field(name= "Opção 2:", value= "Pedra, papel e tesoura", inline=False)
    embed.add_field(name= "Opção 3:", value= "Pedra, papel e tesoura", inline=False)
    msg = await ctx.send(embed=embed)

    await msg.add_reaction("1️⃣")
    await msg.add_reaction("2️⃣")
    await msg.add_reaction("3️⃣")

    def check (reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣"]
    
    try:
        reaction, user = await commands.wait_for("reaction_add", timeout=60.0, check=check)

        if str(reaction.emoji) == "1️⃣":
            await ctx.send('Você escolheu a Opção 1!')
        elif str(reaction.emoji) == "2️⃣":
              await ctx.send('Você escolheu a Opção 2!')
        elif str(reaction.emoji) == "3️⃣":
           await ctx.send('Você escolheu a Opção 3!')
    except StopAsyncIteration.TimeoutError:
        await ctx.send('Tempo esgotado!')

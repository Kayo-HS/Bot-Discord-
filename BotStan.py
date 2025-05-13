import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import StanCaculadora

load_dotenv()

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

botStan = commands.Bot(command_prefix = "-", intents = permissoes)


@botStan.event
async def on_ready():
    print("Estou Pronto!")


@botStan.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author
    await ctx.reply(f"Olá, {usuario.display_name}")

@botStan.command()
async def falar(ctx:commands.Context, *,frase):
    usuario = ctx.author
    await ctx.reply(frase)    

botStan.add_command(StanCaculadora.calcular)

@botStan.command()
async def jogos(ctx:commands.Context):
    embed = discord.Embed(title="Vamos no divertir", description= "Escolha uma opção:", color=discord.Color.blue())
    embed.add_field(name= "Opção 1:", value= "Pedra, papel e tesoura", inline=False)
    embed.add_field(name= "Opção 2:", value= "Pedra, papel e tesoura", inline=False)
    embed.add_field(name= "Opção 3:", value= "Pedra, papel e tesoura", inline=False)
    msg = await ctx.send(embed=embed)

    await msg.add_reaction("1")
    await msg.add_reaction("2")
    await msg.add_reaction("3")

    def check (reaction, user):
        return user == ctx.author and str(reaction.str) in ["1", "2", "3"]
    
    try:
        reaction, user = await botStan.wait_for("reaction_add", timeout=60.0, check=check)

        if str(reaction.str) == "1":
            await ctx.send('Você escolheu a Opção 1!')
        elif str(reaction.str) == "2":
            await ctx.send('Você escolheu a Opção 2!')
        elif str(reaction.str) == "3":
            await ctx.send('Você escolheu a Opção 3!')
    except StopAsyncIteration.TimeoutError:
        await ctx.send('Tempo esgotado!')


























botStan.run(os.getenv("DISCORD_TOKEN"))


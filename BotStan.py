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




























botStan.run(os.getenv("DISCORD_TOKEN"))


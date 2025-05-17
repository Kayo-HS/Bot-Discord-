import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import StanCaculadora
import JogosStan

load_dotenv()

permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

botStan = commands.Bot(command_prefix = "-", intents = permissoes)


@botStan.command()
async def ola(ctx:commands.Context):
    usuario = ctx.author
    await ctx.reply(f"Olá, {usuario.display_name}")

@botStan.command()
async def falar(ctx:commands.Context, *,frase):
    usuario = ctx.author
    await ctx.reply(frase)

@botStan.event
async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    await canal.send(f"Novo canal criado: {canal.name}")

@botStan.event
async def on_member_join(membro:discord.Member):
    canal = botStan.get_channel(1371965370054738022)
    await canal.send(f"{membro.display_name} Entrou no servidor!!\nSeja bem vindo!!")  
    meu_embed = discord.Embed(title=f"Bem vindo, {membro.name}!!!")
    meu_embed.description = "Aproveite a estadia!"
    meu_embed.set_thumbnail(url=membro.avatar)

    await canal.send(embed=meu_embed) 
    








botStan.add_command(StanCaculadora.calcular)

botStan.add_command(JogosStan.jogos)


@botStan.event
async def on_ready():
    print("Estou Pronto!")


botStan.run(os.getenv("DISCORD_TOKEN"))


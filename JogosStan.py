import discord
from discord.ext import commands

@commands.command()
async def jogos(ctx:commands.Context):
    async def resposta_botao(interact:discord.Integration):
        await interact.response.send_message("Escolha uma opção:", view = resposta_botao)

    view_jogos = discord.ui.View()

    botao_jogos = discord.ui.Button(label="Pedra, Papel e Tesoura", style=discord.ButtonStyle.green)
    botao_jogos.callback = resposta_botao
    view_jogos.add_item(botao_jogos)

    botaoJogoAdvinhaçao = discord.ui.Button(label= "Advinhe o Nº que estou pensando")
    botaoJogoAdvinhaçao.callback = resposta_botao
    view_jogos.add_item(botaoJogoAdvinhaçao)
    
    await ctx.reply("Escolha um jogo:", view=view_jogos)

@commands.command()
async def escolha_jogo(ctx: commands.context):
    async def resposta_escolha(interact : discord.Integration):
        await interact.response.send_message(f"Você escolheu: {interact.data["custom_id"]}")

    view_escolha = discord.ui.View()

    botao_pedra = discord.ui.Button(label="Pedra", style=discord.ButtonStyle.gray)
    botao_papel = discord.ui.Button(label="Papel", style=discord.ButtonStyle.green)
    botao_tesoura = discord.ui.Button(label="Tesoura", style=discord.ButtonStyle.red)

    botao_pedra.callback = resposta_escolha
    botao_papel.callback = resposta_escolha
    botao_tesoura.callback = resposta_escolha

    view_escolha.add_item(botao_pedra)
    view_escolha.add_item(botao_papel)
    view_escolha.add_item(botao_tesoura)

    await ctx.send("Escolha seu objeto:", view = view_escolha) 

    
    

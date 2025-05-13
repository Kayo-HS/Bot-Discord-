import discord
from discord.ext import commands
import math

@commands.command()
async def calcular(ctx: commands.context, num1:float ,operador:str ,num2:float):
    try:
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0 or num1 == 0:
                await ctx.reply("Erro: Divisão por zero!")
                return
            resultado = num1/num2
        elif operador == "**" or operador == "^":
            resultado = num1 ** num2
        else:   
            await ctx.reply("Erro use um dos operadores abaixo: +, -, *, /, **, ^")
            return
        await ctx.reply(f"O resultado da sua conta deu {resultado}")
    except Exception as erro:
        await ctx.reply(f"Ocorreu um erro: {erro}")
        
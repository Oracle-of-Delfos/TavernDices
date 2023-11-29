import discord
from discord.ext import commands
import json
from json import dump
from os.path import dirname,realpath
class Economia(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  #Registra uma conta no Json financeiro
  @commands.command(aliases=['registrarcarteira'])
  async def Registrarcarteira(self,ctx,nome):
    with open("Banco.json","r") as f:
      data=json.load(f)
    data[nome]=0
    with open("Banco.json","w") as f:
      dump(data,f,indent=4,separators=(',',':'))
    await ctx.reply('Personagem Criado')
  #Mostra o saldo atual de uma conta no Json financeiro
  @commands.command(aliases=['Carteira'])
  async def carteira(self,ctx,nome):
    try:
      with open("Banco.json","r") as f:
        valores= json.load(f)
      valor_carteira=valores[nome]
      quantidade=f'{nome} tem {valor_carteira} po'
      await ctx.send(quantidade)
    except Exception:
      await ctx.reply('Personagem não registrado,tente cria-lo através do comando "criarpersonagem"')
  #Altera o saldo de uma conta já registrada no json financeiro
  @commands.command(aliases=['Transacao','Transaçao','Transaçâo','transação','transaçao','Transação'])
  async def transacao(self,ctx,nome,valor:int):
    with open("Banco.json","r") as f:
        valores= json.load(f)
    valores[nome]+= valor
    with open("Banco.json","w") as f:
      json.dump(valores,f,indent=4,separators=(',',':'))
    await ctx.reply('Transação Concluída')
  #Realiza uma transferência entre players no Json financeiro
  @commands.command(aliases=['Pagar','dar','propina','doação','doar','negociação','negociar','Negociação','Negociar','Propina','Dar','Doar'])
  async def pagar(self,ctx,nome1,nome2,valor:int):
    with open("Banco.json","r") as f:
        valores= json.load(f)
    valores[nome1]+=-valor
    with open("Banco.json","w") as f:
        valores= json.dump(valores,f,indent=4,separators=(',',':'))
    with open("Banco.json","r") as f:
        valores= json.load(f)
    valores[nome2]+= valor
    with open("Banco.json","w") as f:
        valores= json.dump(valores,f,indent=4,separators=(',',':'))
    await ctx.reply('Transação concluida')
#Adiciona esse arquivo como Cog do bot, possibilitando que ele seja carregado no arquivo principal
def setup(bot):
  bot.add_cog(Economia(bot))

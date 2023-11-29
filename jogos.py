import discord
from discord.ext import commands
import random
from os.path import dirname,realpath,join
import json
from JsonLib import JsonManager

class Jogos(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  #Mecânica de truco criada pelo DM durante uma sessão, automatizada para maior comodidade, o dinheiro atualiza automaticamente na conta do player no Json
  @commands.command(aliases=['Truco'],pass_context=True)
  async def truco(self,ctx,nome,moedas:int):
    with open("Banco.json","r") as f:
      valores= json.load(f)
    if valores[nome]>=moedas:
      soma_das_quedas=0
      for r in range(3):
        d100_2=int(random.randint(1,100))
        d100=int(random.randint(1,100))
        if d100_2>d100:
          vitoria_queda='**Boa!,você ganhou essa queda**'
          await ctx.reply(vitoria_queda)
          a=1
        elif d100>d100_2:
          await ctx.reply('**Que pena!Você perdeu essa queda**')
          a=0
        else:
          d2=random.randint(1,2)
          if d2 == 1:
            a=0
            await ctx.reply('**Que pena!Você perdeu essa queda**')
          else:
            a=1
            await ctx.reply('**Parabéns,você venceu essa queda**')
        soma_das_quedas += a
      if soma_das_quedas > 1.5:
        valores[nome] += moedas
        with open("Banco.json","w") as f:
          valores= json.dump(valores,f,indent=2,separators=(',',':'))
        vencedor=(f'**Parabéns!Você ganhou {moedas} moedas!**')
        await ctx.reply(vencedor)
      elif soma_das_quedas < 1.5:
        valores[nome] += -moedas
        with open("Banco.json","w") as f:
          valores= json.dump(valores,f,indent=2,separators=(',',':'))
        perdedor=(f'**Mais sorte da próxima,você perdeu {moedas} moedas!**')
        await ctx.reply(perdedor)
    else:
      await ctx.reply(f'Você não tem po suficiente para apostar {moedas} moedas!')

  #Mecânica de truco criada pelo DM durante uma sessão, automatizada para maior comodidade, o dinheiro atualiza automaticamente na conta do player no Json
  @commands.command(aliases=['copos'])
  async def Copos(self,ctx,nome,moedas:int):
    """Aposta com copos."""
    with open("Banco.json","r") as f:
      valores= json.load(f)
    if valores[nome] >= moedas:
      d20=int(random.randint(1,20))
      dado=('Você rolou {} no d20'.format(d20))
      await ctx.reply(dado)
      if d20 > 14:
        vitoria=int(moedas)
        valores[nome] += moedas
        with open("Banco.json","w") as f:
          valores= json.dump(valores,f,indent=2,separators=(',',':'))
        victory=('Parabéns,você ganhou {} moedas!'.format(vitoria))
        await ctx.reply(victory)
      elif d20 < 9:
        valores[nome] += -moedas
        with open("Banco.json","w") as f:
          valores= json.dump(valores,f,indent=2,separators=(',',':'))
        derrota=('Que pena,você perdeu {} moedas'.format(moedas))
        await ctx.reply(derrota)
      else:
        copos=int(random.randint(1,3))
        if copos == 1:
          valores[nome] += moedas
          with open("Banco.json","w") as f:
            valores= json.dump(valores,f,indent=2,separators=(',',':'))
          copo_certo=int(moedas)
          parabens=('Parabéns,você ganhou {} moedas!'.format(copo_certo))
          await ctx.reply(parabens)
        else:
          valores[nome] += -moedas
          with open("Banco.json","w") as f:
            valores= json.dump(valores,f,indent=2,separators=(',',':'))
          copo_errado=('Que pena,você perdeu {} moedas'.format(moedas))
          await ctx.reply(copo_errado)
    else:
      await ctx.reply(f'Você não tem po suficiente para apostar {moedas} moedas!')
#adiciona esse arquivo como Cog do bot, possibilitando que ele seja carregado no arquivo principal
def setup(bot):
  bot.add_cog(Jogos(bot))

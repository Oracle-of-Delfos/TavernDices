import discord
from discord.ext import commands
import json
from json import dump,load

class Items(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  #Cria uma conta no Json de inventário
  @commands.command(aliases=['registro'])
  async def Registro(self,ctx,nome):
    with open("Items.json","r") as f:
      arquivo=json.load(f)
    arquivo[nome]=""
    with open("Items.json",'w') as f:
      json.dump(arquivo,f,indent=2,separators=(',',':'))
    await ctx.reply('Seu inventário pessoal foi criado!')
  #Adciona um novo item à uma conta já criada
  @commands.command(aliases=['Adicionaritem'])
  async def adicionaritem(self,ctx,nome,*args):
    with open("Items.json","r") as f:
      items=json.load(f)
    for arg in args:
      if items[nome] == "":
        items[nome]=f'{items[nome]}{arg}'
      else:
        items[nome]=f'{items[nome]},{arg}'
      with open("Items.json","w") as f:
        dump(items,f,indent=2,separators=(',',':'))
      await ctx.reply('Item adicionado!')
  #Mostra todos os itens de uma conta já registrada no Json de inventário
  @commands.command(aliases=['Inventario','Inventário','inventário'])
  async def inventario(self,ctx,nome):
    with open("Items.json","r") as f:
      items=json.load(f)
    await ctx.reply(f'Inventário de {nome}:'
    '\n' f'{items[nome]}')
  #Deleta um ou mais itens do Json de inventário
  @commands.command(aliases=['deletaritem'])
  async def Deletaritem(self,ctx,nome,*args):
    for arg in args:
      try:
        with open('Items.json','r') as f:
          objetos=json.load(f)
        objetos_lista=objetos[nome].split(',')
        objeto=objetos_lista.index(arg)
        del objetos_lista[objeto]
        items_finais=','.join(objetos_lista)
        objetos[nome]=items_finais
        with open('Items.json','w') as f:
          json.dump(objetos,f,indent=2,separators=(',',':'))
        await ctx.reply('Item deletado com sucesso!')
      except Exception:
        await ctx.reply(f'O item {arg} não foi encontrado no inventário de {nome}!')
  #Automatiza a troca de itens entre players no Json de inventário
  @commands.command(aliases=['Daritem'])
  async def daritem(self,ctx,nome1,nome2,*args):
    for arg in args:
      try:
        with open('Items.json','r') as f:
          objetos=json.load(f)
        objetos_lista=objetos[nome1].split(',')
        objeto=objetos_lista.index(arg)
        del objetos_lista[objeto]
        items_finais=','.join(objetos_lista)
        objetos[nome1]=items_finais
        with open('Items.json','w') as f:
          json.dump(objetos,f,indent=2,separators=(',',':'))
        with open("Items.json","r") as f:
          items=json.load(f)
        if items[nome2] == "":
          items[nome2]=f'{items[nome2]}{arg}'
        else:
          items[nome2]=f'{items[nome2]},{arg}'
        with open("Items.json","w") as f:
          dump(items,f,indent=2,separators=(',',':'))
        await ctx.reply('Objeto transferido com sucesso!')
      except Exception:
        await ctx.reply('Ops,objeto não encontrado!')
#Adiciona esse arquivo como Cog do bot, possibilitando que ele seja carregado no arquivo principal
def setup(bot):
  bot.add_cog(Items(bot))

import discord
import discord.ext
import random
import os
import typing
from discord.ext import commands
import host
#Configura a aparência do Bot no servidor,estabelece o prefixo e carrega as extensões e outros arquivos
activity = discord.Game(name="D&D 5e")
client=discord.Client()
bot = commands.Bot(command_prefix='',activity=activity,status=discord.Status.idle)
bot.remove_command('help')
extensions=['jogos','help','economia','inventario']
if __name__=='__main__':
  for extension in extensions:
    bot.load_extension(extension)
#Rola um dado pseudo-aleatório com a biblioteca random, uso explicado no comando help
@bot.command(aliases=['r'])
async def R(ctx, dice: str,soma: typing.Optional[int],dice2: typing.Optional[str],dice3: typing.Optional[str],dice4: typing.Optional[str]):
    try:
       rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.reply('Por favor,escreva os dados no formato NdN!')
        return
    result =','.join(str(random.randint(1, limit)) for r in range(rolls))
    resultados=result.split(sep=',')
    final=sorted(resultados, key= int, reverse=True)
    finalizacao=sorted(resultados,key=int,reverse=True)
    soma_dos_dados=0
    for caractere in resultados:
      if caractere.isdigit():
        soma_dos_dados += int(caractere) 
    for numero in final:
      #Zuação para o player quando ele tira 1
      if numero == '1' and limit == 20:
        zuera=(':fist: :pensive: **Perdemo**','**Mamou**:smiling_imp:','**F pra prestar homenagem** :sob:','**lamentavel de vdd 9vinha** :rolling_eyes:','**saudou a mandioca** :fist:','**vai dar n** :sob:','**já encomendou o caixão?** :cross:','**pode rolar dnv? :sweat_smile:**','**onde é que eu tô?**','_pain_','**chama o shamu** :ambulance:','**ih lá vem merda**','**Boa nerdola,to gostando de ver** :clap:','**CORRE GALERA**','**DEIXA EU VIVO PFV** :pray:')
        zueira=random.choice(zuera)
        await ctx.reply(zueira)
      if numero == '20' and limit == 20:
      #Elogio para o player quando ele tira 20
        elogio=('** :medal: aceitas ?? **','**:sunglasses: ganhamo**','**Slk Tio pra q isso tudo :flushed:**','**padabains** :clap:','**O pai ta ON** :sunglasses:','**Essa vai ser minha maior vigarice** :smirk:','**brabissimo**','**só o filé** :ok_hand:','**rei delas** :smirk:',' :leaves: **voa mlk**',' :fire: **brabo demais**','**lançou a braba** :sunglasses:','**UMA MÁQUINA????**','**olha isso mano**:eyes:')
        agradecimento=random.choice(elogio)
        await ctx.reply(agradecimento) 
    try:    
      rolls2, limit2 = map(int, dice2.split('d'))
      result2 =','.join(str(random.randint(1, limit2)) for s in range(rolls2))
      resultados2=result2.split(sep=',')
      final2=sorted(resultados2, key= int, reverse=True)
      finalizacao2=sorted(resultados2,key=int,reverse=True)
      soma_dos_dados2=0
      for caractere2 in final2:
        if caractere2.isdigit():
            soma_dos_dados2 += int(caractere2)
    except Exception:
      soma_dos_dados2=0
      finalizacao2="['0']"
    try:
      rolls3, limit3 = map(int, dice3.split('d')) 
      result3 =','.join(str(random.randint(1, limit3)) for t in range(rolls3))
      resultados3=result3.split(sep=',')
      final3=sorted(resultados3, key= int, reverse=True)
      finalizacao3=sorted(resultados3,key=int,reverse=True)
      soma_dos_dados3=0
      for caractere3 in final3:
        if caractere3.isdigit():
         soma_dos_dados3 += int(caractere3)
    except Exception:
      soma_dos_dados3=0
      finalizacao3="['0']"
    try:
      rolls4, limit4 = map(int, dice4.split('d'))
      result4 =','.join(str(random.randint(1, limit4)) for u in range(rolls4))
      resultados4=result4.split(sep=',')
      final4=sorted(resultados4, key= int, reverse=True)
      finalizacao4=sorted(resultados4,key=int,reverse=True)
      soma_dos_dados4=0
      for caractere4 in final4:
        if caractere4.isdigit():
          soma_dos_dados4 += int(caractere4)   
    except Exception:
      soma_dos_dados4=int('0')
      finalizacao4="['0']"
    if soma == None: 
      soma=int('0') 
    else:
      soma=soma
    resultados_finais='{}'.format(int(soma_dos_dados)+int(soma_dos_dados2)+int(soma_dos_dados3)+int(soma_dos_dados4)+int(soma))
    texto_final='{}{}{}{}'.format(finalizacao,finalizacao2,finalizacao3,finalizacao4)
    fim_do_codigo='Total=[{}], Soma dos Resultados:{}+{}'.format(resultados_finais,texto_final,soma) 
    await ctx.reply(fim_do_codigo)
#Quando o bot liga com sucesso escreve uma mensagem só para a visualização de que ele está funcionando.
@bot.event
async def on_ready():
    print('Bem vindo à', bot.user.name ,'!')
    print('ID=',bot.user.id)
    print('------')
token=os.environ.get("token")
bot.run(token)

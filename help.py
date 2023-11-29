import discord
from discord.ext import commands
#Escreve um texto explicativo para todos os comandos funcionais do bot
class Ajuda(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  @commands.command(aliases=['Help'])
  async def help(self,ctx):
    await ctx.reply('**r (dado1) (número a ser somado ou subtraido) (dado2) (dado3) (dado4)**:rola um ou mais dados no formato NdN e soma eles à um número dado'
    '\n''**registrarcarteira (nome)**:abre uma conta na carteira virtual do TavernDices para seu personagem!'
    '\n''**Transação (nome) (valor)**:soma a quantidade fornecida à conta do personagem dado,caso queira retirar dinheiro coloque um número negativo,por exemplo,-5 para diminuir 5 de sua conta'
    '\n''**pagar (nome1) (nome2) (valor)**: transfere o valor fornecido da conta do primeiro personagem para a conta do segundo'
    '\n''**truco (nome) (aposta)**: executa um jogo de truco automatizado com D20 com a aposta fornecida
    '\n' '**copos (nome) (aposta)**: executa um jogo dos copos automatizado com D20 com a aposta fornecida'
    '\n' '**carteira (nome)**: mostra o saldo atual do player especificado'
    '\n' '**registro (nome)**: cria uma conta para registro de inventário'
    '\n' '**adicionaritem (item1) (item2)...**: adiciona items à uma conta já registrada'
    '\n' '**inventario (nome)**: mostra todos os itens guardados em uma conta registrada'
    '\n' '**deletaritem (nome) (item1) (item2)...**: deleta items à uma conta registrada'
    '\n' '**daritem (nome1) (nome2) (item1) (item2)...**: Transfere items entre contas registradas')
#adiciona esse arquivo como Cog do bot, possibilitando que ele seja carregado no arquivo principal
def setup(bot):
  bot.add_cog(Ajuda(bot))

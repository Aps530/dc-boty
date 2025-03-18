import discord
from discord.ext import commands
import requests

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def zacznij(ctx):
    await ctx.send(f'Napisz, czy twoja karta graficzna, zasilacz i procesor zużywają więcej niż 600W! Napisz ,,$Więcej" lub ,,$Mniej"')

@bot.command()
async def Mniej(ctx):
    await ctx.send(f'Świetnie! Nie kupuj nowych podzespołów do komputera, które łącznie zużywają więcej niż 600W, ponieważ przyczynisz się do globalnego ocieplenia, przez które spłoniesz! Z resztą, niedługo i tak niedługo zostanie to zabronione.')

bot.command()
async def Wiecej(ctx):
    await ctx.send(f'Świetnie! W nagrodę mam dla ciebie poradnik! Otwórz wiersz polecenia i wpisz ,,shutdown /s /t 0" Ta komend zmnejszy ilośc watów, tak po prostu! Jeśli nie chcesz tego robić napisz ,,$Nie_chce"')

bot.command()
async def Nie_chce(ctx):
    await ctx.send(f'Samolot zużywa 50 kWh na 100 pkm, a ty zużywasz 600W, to 12 razy więcej niż samolot! Zanieczyszczasz środowisko 12 razy bardziej niż ogromny samolot, więc wyłącz komputer i uratuj środowisko.')

bot.run("Tokena nie ma tylko w wersji na github")
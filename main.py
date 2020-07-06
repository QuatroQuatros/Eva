import discord
from discord import FFmpegPCMAudio
from discord.utils import get
from translate import Tradutor
from fala import Fala
from bot import Bot
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    bot= Bot('eva')
    if message.author == client.user:
        return

    elif message.content.startswith('!'):
        #await message.channel.send('Funcionou!')
        #bot.treina('treino')
        z = message.content
        frase = z.replace('!', '')
        resposta = bot.responde(frase)
        await message.channel.send(resposta)

    elif message.content.startswith('&'):
        try:
            canal = message.author.voice.channel
            voice = get(client.voice_clients)
            if voice and voice.is_connected():
                await voice.move_to(canal)
                x = message.content
                frase = x.replace('&', '')
                resposta = bot.responde(frase)
                await message.channel.send(resposta)
                ttsx = Fala.falar(resposta)
                voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="eva.mp3"))
            else:
                voice = await canal.connect()
                z = message.content
                frase = z.replace('&', '')
                resposta = bot.responde(frase)
                await message.channel.send(resposta)
                ttsx = Fala.fale(resposta)
                voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="eva.wav"))
        except:
            await message.channel.send('entre em um canal de voz')

    elif message.content.startswith('::ensinar'):
        #await message.channel.send('escreva algo e apos a ? escreva a resposta')
        bot = Bot('Eva')
        b = message.content
        frase = b.replace('::ensinar', '')
        nova = bot.aprender(b, frase)
        await message.channel.send('obrigada por me ensinar')
        await message.channel.send(nova)

    elif message.content.startswith('$traduzaEN'):    
        print(message.content)
        x = message.content
        frase = x.replace('$traduzaEN', '')
        print(frase)
        lang = 'en'
        palavra_traduzida = Tradutor.traduza(frase, lang)
        await message.channel.send(palavra_traduzida)

    elif message.content.startswith('$traduzaPT'):    
        print(message.content)
        x = message.content
        frase = x.replace('$traduzaPT', '')
        print(frase)
        lang = 'pt'
        palavra_traduzida = Tradutor.traduza(frase, lang)
        await message.channel.send(palavra_traduzida)

    elif message.content.startswith('$fale'):
        try:
            canal = message.author.voice.channel
            voice = get(client.voice_clients)
            if voice and voice.is_connected():
                await voice.move_to(canal)
                x = message.content
                frase = x.replace('$fale', '')
                print(frase)
                lang = 'en'
                palavra_traduzida = Tradutor.traduza(frase, lang)
                ttsx = Fala.__init__(palavra_traduzida)
                voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="fala.mp3"))
            else:
                voice = await canal.connect()
                x = message.content
                frase = x.replace('$fale', '')
                print(frase)
                lang = 'en'
                palavra_traduzida = Tradutor.traduza(frase, lang)
                ttsx = Fala.__init__(palavra_traduzida)
                voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="fala.mp3"))
        except:
            await message.channel.send('entre em um canal de voz')
        

client.run('NzI3NjgzMjYyOTczMDgzNjQ4.XvvaYg.fPQtmyUX9Wsllh0RhymTwdg-p4A')
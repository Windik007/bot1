import discord
from discord.ext import commands 
import json
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import asyncio
from asyncio import sleep
import requests
from PIL import Image, ImageFont, ImageDraw
from discord import File
import io
import random
import os, csv, random, discord, asyncio, requests, json, traceback
from dotenv import load_dotenv
import youtube_dl
from discord.utils import get
from discord.ext.commands import Bot
import time
from discord import Game
import math, time
import sqlite3
import os
import random
import time
import math


member = discord.Member




bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())
bot.remove_command( 'help' )
play_next_song = asyncio.Event()


@bot.event
async def on_ready():
   DiscordComponents(bot)
print("Подключение!")

print("Загрузка...")

print("Бот успешно подключен!")

@bot.command()
async def mute(ctx, user: discord.Member, time: int, reason):
    role = user.get_role(894170737617817640)
    await ctx.send(
      embed=discord.Embed(title=" Safety | Mute  ", timestamp = ctx.message.created_at, colour = discord.Color.purple(),   description = f'''
      **{user} получил мут:**
```Случай: -
Время наказания: {time} секунд(a)
Модератор: {ctx.author.name}#{ctx.author.discriminator}
Причина: {reason}```
     ''' )
    )
    await user.add_roles(role)
    await user.move_to(None)
    await asyncio.sleep(time * 60)
    await user.remove_roles(role)
   



@bot.command()
async def unmute(ctx, user: discord.Member):
    role = user.guild.get_role(894170737617817640) 
    await ctx.send(
      embed=discord.Embed(title=" WA Safety | Mute  ", timestamp = ctx.message.created_at, colour = discord.Color.purple(),   description = f'''
      C пользователя {user} снят мут
     ''' )
    )
    await user.remove_roles(role)



@bot.command()
async def user(ctx,member:discord.Member = None, guild: discord.Guild = None):
    if member == None:
        emb = discord.Embed(title="Информация о пользователе:", colour = discord.Color.purple())
        emb.add_field(name="Имя: ", value=ctx.message.author.name,inline=False)
        t = ctx.message.author.status
        if t == discord.Status.online:
            d = " В сети"

        t = ctx.message.author.status
        if t == discord.Status.offline:
            d = " Не в сети"

        t = ctx.message.author.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = ctx.message.author.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"

        emb.add_field(name="Статус:", value=d,inline=False)
        emb.add_field(name="Пользовательский статус:", value=ctx.message.author.activity,inline=False)
        emb.add_field(name="Роли:", value=f"{ctx.message.author.top_role.mention}",inline=False)
        emb.add_field(name="Дата создания:", value=ctx.message.author.created_at.strftime("%#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await ctx.send(embed = emb)
        emb.set_footer(text="Windows Assistent © 2021 All rights are sniffed ")
    else:
        emb = discord.Embed(title="Информация о пользователе:", colour = discord.Color.purple())
        emb.add_field(name="Имя:", value=member.display_name,inline=False)
        t = member.status
        if t == discord.Status.online:
            d = " В сети"

        t = member.status
        if t == discord.Status.offline:
            d = " Не в сети"

        t = member.status
        if t == discord.Status.idle:
            d = " Не активен"

        t = member.status
        if t == discord.Status.dnd:
            d = " Не беспокоить"
        emb.add_field(name="Статус:", value=d,inline=False)
        emb.add_field(name="Пользовательский статус:", value=member.activity,inline=False)
        emb.add_field(name="Роли:", value=f"{member.top_role.mention}",inline=False)
        emb.add_field(name="Дата создания:", value=member.created_at.strftime("%#d %B %Y, %I:%M %p UTC"),inline=False)
        emb.set_footer(text="Windows Assistent © 2021 All rights are sniffed ")
        await ctx.send(embed = emb)
        




@bot.command(aliases = ['AVATAR','Avatar'])
async def avatar(ctx):
    await ctx.send(
      ctx.message.author_url
      )



@bot.command(name='say')
async def audit(ctx, *, msg=None):
    if msg is not None:
        await ctx.send(msg)


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Хочешь увидеть лисицу? Вот она!') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed


@bot.command()
async def server(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)
  guildname = str(ctx.guild.name)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title="Информация о сервере:",
      color=discord.Color.purple()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Название:", value=guildname, inline=True)
  embed.add_field(name="Cоздатель:", value=owner, inline=True)
  embed.add_field(name="Регион сервера:", value=region, inline=True)
  embed.add_field(name="Количество участников:", value=memberCount, inline=True)

  await ctx.send(embed=embed)


@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=1, limit_amount=1):
    await ctx.channel.purge(limit=amount+1)
    await ctx.channel.purge(limit=limit_amount)
    author = ctx.message.author
    await ctx.send(
      embed = discord.Embed(title = 'Очистка:', description = f'{author} удалил {amount} сообщений!', colour = discord.Color.purple())
    )




  




@bot.command()
async def test(ctx):
    await ctx.send(
        components=[
            Select(
                placeholder="Вперед!!",
                options=[
                    SelectOption(label="🗺️ Карты", value="Бан выдан пользователю"),
                    SelectOption(label="📃 Общая информация", value="Мут выдан"),
                    SelectOption(label="👻 Виды призраков", value="Варн выдан"),
                    SelectOption(label="⚔️ Уровни сложности", value="Пользователь кикнут"),
                ],
                custom_id="select1",
            )
        ],
    )

    interaction = await bot.wait_for(
        "select_option", check=lambda inter: inter.custom_id == "select1"
    )
    await interaction.send(content=f'''{interaction.values[0]}''')









@bot.command()
async def info(ctx):
  await ctx.send(
    embed = discord.Embed(title = '**Windows Bot**', description = '''
        Привет! Меня зовут Windows Bot! 
Сборка:
`1.9 BETA (от 16.10.2021)`
Разработчик:
`!~Windo [WS11] Nakatsu#6666`


Полезные ссылки:
`В разработке`

        ''', timestamp = ctx.message.created_at, colour = discord.Color.purple()),

        components = [
            Button(style = ButtonStyle.URL, url = 'https://youtube.com', label = 'Подробнее'),
        ]
        )
   





@bot.command()
async def testcom(ctx):
  await ctx.send( 
    embed = discord.Embed(
      title = "В этом гайде собрана полезная и просто любопытная информация по игре Phasmophobia. Информация, факты и предположения основаны, как на личном опыте, так и на собирательном опыте других игроков. Данное руководство будет дополнятся и улучшаться по возможности."
    ),
      components = [
Select(
        placeholder = 'Вперед!',
        options = [
            SelectOption(label="🗺️ Карты", value="1"),
            SelectOption(label="📃 Общая информация", value="2"),
            SelectOption(label="👻 Виды призраков", value="3"),
            SelectOption(label="⚔️ Уровни сложности", value="4"),
            SelectOption(label="⏰ Скоро", value="5")
          ])
    ]
  )

  interaction = await bot.wait_for(
        "select_option", check=lambda inter: inter.custom_id == "select1"
    )
  await interaction.send(content=f'''{interaction.values[0]}''')
  await interaction.send(content=f'''{interaction.values[1]} s''')


@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def ban( ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await member.ban(reason=reason)
    await ctx.send(
  embed = discord.Embed( title = f'Safety | {ctx.author.name} ', description = f'''Нарушитель {ctx.user.name}
Модератор: 
Причина:
{reason}
'''
  )
    )
   


@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def unban( ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    await member.unban()

@bot.command()
async def t(ctx):
    await ctx.send(
      embed=discord.Embed(title = 'Набор в Команду <:a1:898993211480113152>', description = '''Открыт набор в состав команды на должность <@&897535752085315645> 
`Примечания:`
• <@&897535752085315645>  — человек, отвечающий за партнёрства (заключение и обновление).
• Чтобы подать заявку, необходимо правильно заполнить и отослать следующую анкету:
Анкета:
1. Упоминание самого себя.
2. Ваше полное имя. 
3. Готовы ли вы, в случае чего, пройти проверку в голосовом формате? 
4. Опыт работы. 
5. Ваш часовой пояс. 
6. Ваш возраст.

Пример:
1. <@770318740083572797>
2. Вася.
3. Готов.
4. Опыта не имеется.
5. МСК
6. 15 лет
`Ответственный за набор:`
 <@770318740083572797>
      '''
      )
    )



@bot.command()
async def help(ctx):
    await ctx.send(
      embed = discord.Embed(
        title="Доступные команды:", description ='''
      Что бы подробно получить информацию о какой либо команде, введите ".help Название команды", или выберете в меню ниже 
 **Информация**
``.help`` ``.user`` ``.info`` ``.server`` ``.invite``
 **Модерация**
~~``.warn``~~ ~~``.unwarn``~~ ``.ban`` ~~``.unban``~~ ``.mute`` ``.unmute`` ~~``.kick``~~ ~~``.warns``~~ ``.clear``
 **Ranking**
~~``.rank``~~ ~~``.leaders``~~
 **Music**
~~``.play``~~ ~~``.stop``~~
 **Fun**
``.avatar`` ``.fox``
*Все команды которые зачеркнуты - в разработке*'''
      )
    )


@bot.command()
async def invite(ctx):
  await ctx.send(
    embed = discord.Embed(title = "Пригласите *Windows Assistent'a* к себе на сервер",
    description = "Приглашая бота на сервер вы соглашаетесь с нашими [Условиями пользования](https://youtube.com)",  timestamp = ctx.message.created_at, colour = discord.Color.purple()),
        components = [
            Button(style = ButtonStyle.URL, url = 'https://discord.com/api/oauth2/authorize?client_id=789800733327228939&permissions=8&scope=bot', label = 'Пригласить'),
        ]
        )










bot.run("Nzg5ODAwNzMzMzI3MjI4OTM5.X93VQA.rgQmvmFCcpE1mhXkju07YCaTpdo")

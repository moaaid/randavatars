import random
import discord
from discord.ext import commands
from time import sleep

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('the bot is ready')


@client.command()
async def gif(ctx):
    while True:
        sleep(5)
        gifsC = client.get_channel(716239404275990576)
        avatarsG = ["https://cdn.discordapp.com/attachments/715910958803058718/716409646612480082/4ez_92692577_544188123163043_8380038935868829351_n.jpg",
        "https://cdn.discordapp.com/attachments/715910958803058718/716409646050705468/fcbccce194bc19f4de0551d2dec4eff6.jpg",        
        "https://cdn.discordapp.com/attachments/715910958803058718/716409645614366730/D29D7iIiqC.png",        
        "https://cdn.discordapp.com/attachments/715910958803058718/716409645123764234/IMG__.png"]          
        randomavatar  = discord.Embed(color = discord.Color.dark_blue())
        randomavatar.set_image(url=random.choice(avatarsG))
        randomavatar.set_footer(text=":copyright: ทστ__мσαiα∂.#1230")
        await gifsC.send(embed=randomavatar)
        
@client.command()
async def avatar(ctx):
    while True:
        sleep(5)
        avatarC = client.get_channel(716239404275990576)
        avatarsA = ["https://cdn.discordapp.com/attachments/715910958803058718/716409646612480082/4ez_92692577_544188123163043_8380038935868829351_n.jpg",
        "https://cdn.discordapp.com/attachments/715910958803058718/716409646050705468/fcbccce194bc19f4de0551d2dec4eff6.jpg",        
        "https://cdn.discordapp.com/attachments/715910958803058718/716409645614366730/D29D7iIiqC.png",        
        "https://cdn.discordapp.com/attachments/715910958803058718/716409645123764234/IMG__.png"]        
        randomavatar  = discord.Embed(color = discord.Color.dark_blue())
        randomavatar.set_image(url=random.choice(avatarsA))
        randomavatar.set_footer(text=":copyright: ทστ__мσαiα∂.#1230")
        await avatarC.send(embed=randomavatar)

client.run("NzE0MTgxNjEyNTc2ODMzNTQ4.XtEPWg.S3CFMrajPfm9qliRM4It2f-Z5Jk")

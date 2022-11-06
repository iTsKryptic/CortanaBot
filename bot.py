import lightbulb
import hikari
import random
import requests
from hikari.colors import Color
import datetime as dt

bot = lightbulb.BotApp(token='mytoken',
                       default_enabled_guilds=(1038270669789610025))


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Cortana now online!')


@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def myGroup(ctx):
    pass


@myGroup.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand')


# command to add two numbers
@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


# command to @ the user and say hello
@bot.command()
@lightbulb.option("user", "User to greet", hikari.User)
@lightbulb.command("greet", "ping the user")
@lightbulb.implements(lightbulb.SlashCommand)
async def greet(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Hello Spartan {ctx.options.user.mention}!")


# command to say a quote
@bot.command
@lightbulb.command('quote', 'Cortana quote')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    quotes_list = ['Chief, when you get to Earth, good luck.', 'It has been an honor serving with you, Spartan.',
                   'So, whats the plan?', 'You did that on purpose, didnt you',
                   'You might consider sitting this one out']
    rand_quote = random.choice(quotes_list)
    await ctx.respond(rand_quote)


img_plugin = lightbulb.Plugin("images", "Images manipulation related command")


# command to say a send a picture .
@bot.command
@lightbulb.command("dice", "roll a 6 sided die")
@lightbulb.implements(lightbulb.SlashCommand)
async def command_dice(ctx):
    dice_roll = random.randint(1, 6)
    await ctx.respond(dice_roll)


# command to get a koala image
@bot.command
@lightbulb.command(name="koala", aliases=("koala",), description="get a picture of a koala")
@lightbulb.implements(lightbulb.SlashCommand)
async def command_cat(ctx: lightbulb.SlashContext) -> None:
    image_url = requests.get("https://some-random-api.ml/img/koala")
    image_link = image_url.json()
    image = image_link['link']

    embed = (hikari.Embed(
        colour=Color(0x36393f),
        timestamp=dt.datetime.now().astimezone()
    )
             .set_footer(text=f"Requestest by {ctx.member.display_name}", icon=ctx.author.avatar_url)
             .set_image(image)
             )

    await ctx.respond(embed=embed, reply=True)


# command to get a fact about koalas
@bot.command
@lightbulb.command(name="facts", aliases=("koala",), description="get a fact of a koala")
@lightbulb.implements(lightbulb.SlashCommand)
async def command_cat(ctx: lightbulb.SlashContext) -> None:
    fact_url = requests.get("https://some-random-api.ml/facts/koala")
    koala_fact = fact_url.json()
    await ctx.respond(koala_fact)


bot.run()

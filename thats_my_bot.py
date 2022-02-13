import discord
import json
import random
import street_kitchen
from discord.ext import commands


# guild = Guilds in Discord represent an isolated collection of users and channels, and are often referred to as "servers" in the UI.


CREDENTIALS_FILE_PATH = 'creds.json'
FOOD_FILE_PATH = 'food_categories.json'
JOKES_FILE_PATH = 'jokes.txt'


def load_json(file_path: str):
    with open(file_path, mode='r', encoding='utf-8') as file:
        json_file = json.load(file)
        return json_file


def load_jokes():
    with open(JOKES_FILE_PATH, mode='r', encoding='utf-8') as file:
        return file.readlines()


creds = load_json(CREDENTIALS_FILE_PATH)
food_cats = load_json(FOOD_FILE_PATH)
bot = commands.Bot(command_prefix='!')


@bot.command(name='create-channel', help='Create a channel with the given name. For example: !create-channel channel-name')
#@commands.has_role('Admin')
async def create_channel(ctx, channel_name='Piggys channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await ctx.send(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.command(name='cookie', help='Recommends a cookie recipe from streetkitchen.hu')
async def reommend_cookie(ctx):
    food_id = food_cats['dessert']
    food = street_kitchen.get_food(*food_id.values())
    print(food.name)
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='fishdish', help='Recommends a fish dish recipe from streetkitchen.hu')
async def reommend_fish_dish(ctx):
    food_id = food_cats['fish']
    food = street_kitchen.get_food(*food_id.values())
    print(food.name)
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='veggie', help='Recommends a veggie food from streetkitchen.hu')
async def reommend_veggie_food(ctx):
    food_id = food_cats['veggie']
    food = street_kitchen.get_food(*food_id.values())
    print(food.name)
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='meat', help='You get some protein boost from streetkitchen.hu')
async def reommend_veggie_food(ctx):
    food_id = food_cats['meat']
    food = street_kitchen.get_food(*food_id.values())
    print(food.name)
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='joke', help='Tells you a joke' )
async def tell_joke(ctx):
    joke_list = load_jokes()
    response = random.choice(joke_list)
    await ctx.send(response)


@bot.command(name="help-list", help="Returns all commands available. Then use !help [command]")
async def help(ctx):
    helptext = "```"
    for command in bot.commands:
        helptext += f"{command}\n"
    helptext += "```"
    await ctx.send(helptext)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command!')


bot.run(creds['token'])
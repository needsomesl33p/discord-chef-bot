from discord.ext import commands
from discord import Message
from typing import AsyncIterator
from hashlib import sha1
from utils import (
    get_message_context,
    load_jokes,
    load_json
)
import discord
import random
import street_kitchen

# guild = Guilds in Discord represent an isolated collection of users and channels, and are often referred to as "servers" in the UI.


CREDENTIALS_FILE_PATH = 'creds.json'
FOOD_FILE_PATH = 'food_categories.json'
JOKES_FILE_PATH = 'jokes.txt'
MSG_LIMIT = 300
hashes: list = []


creds: dict = load_json(CREDENTIALS_FILE_PATH)
food_cats: dict = load_json(FOOD_FILE_PATH)
joke_list: list = load_jokes(JOKES_FILE_PATH)
bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')


@bot.command(name='create-channel', help='Create a channel with the given name. For example: !create-channel channel-name')
async def create_channel(ctx, channel_name='Piggys channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await ctx.send(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


@bot.command(name='get-recipe', help='It returns a concrete recipe according to the given food name.')
async def get_recipe(ctx, food_name):
    food = street_kitchen.get_food(food_name, None)
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='cookie', help='Recommends a cookie recipe from streetkitchen.hu')
async def recommend_cookie(ctx):
    food_id = food_cats['dessert']
    food = street_kitchen.get_food(*food_id.values())
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='fishdish', help='Recommends a fish dish recipe from streetkitchen.hu')
async def recommend_fish_dish(ctx):
    food_id = food_cats['fish']
    food = street_kitchen.get_food(*food_id.values())
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='veggie', help='Recommends a veggie food from streetkitchen.hu')
async def recommend_veggie_food(ctx):
    food_id = food_cats['veggie']
    food = street_kitchen.get_food(*food_id.values())
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='meat', help='You get some protein boost from streetkitchen.hu')
async def recommend_meat_food(ctx):
    food_id = food_cats['meat']
    food = street_kitchen.get_food(*food_id.values())
    await ctx.send(f'Name: {food.name}\nLink:{food.URL}\nImage: {food.image_URL}')


@bot.command(name='joke', help='Tells you a joke')
async def tell_joke(ctx):
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
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message: Message = await channel.fetch_message(payload.message_id)
    if len(message.reactions) == 5:
        history: AsyncIterator = channel.history(
            limit=MSG_LIMIT)

        golden_quote_ctx = await get_message_context(history, message)

        sha1_print: str = sha1(golden_quote_ctx.encode()).hexdigest()
        if sha1_print not in hashes:
            hashes.append(sha1_print)

            destination_channel = bot.get_channel(
                creds['golden_quotes_chn_id'])
            await destination_channel.send(golden_quote_ctx)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command!')


bot.run(creds['token'])

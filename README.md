# Discord Chef Bot #

 - You have a friend, familiy or other group / channel where the topic is the food?
 - You cannot really decide what's for Saturday lunch?
 - Or just want to eat a cookie but no idea what?

 Let the Chef bot do the brainstorming and select a recipe for you! Then control the Bot with the `!` (exclamation mark) commands!

You can choose from the following categories:
 - veggie
 - meat
 - fish
 - dessert

 OR

 You just type the name of the food to get your recipe from `https://streetkitchen.hu`
 
 ### Install ###

```pip3 install -r requirements.txt```

### Run ###

```python .\thats_my_bot.py```

### Tested on ###

```Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32```

### Init ###

 - Create a Discord account and follow the below tutorial to add a new bot to your server: 
 
    https://discordpy.readthedocs.io/en/stable/discord.html

 - You also have to put the bot's Token into the `creds.json` file
 - Find it on: https://discord.com/developers/applications, then under the 'Bot' submenu.

### Usage ###

Get a food recipe according to the provided parameter (name of the food):

![Get recipe](https://raw.githubusercontent.com/needsomesl33p/discord-chef-bot/master/images/get-recipe.png)

Get a cookie recipe:

![Get a cookie recipe](https://raw.githubusercontent.com/needsomesl33p/discord-chef-bot/master/images/cookie.png)

Get a veggie recipe:

![Save the animals, Eat Veggie Food](https://raw.githubusercontent.com/needsomesl33p/discord-chef-bot/master/images/veggie.png)

Hey Chef-Boty, tell me a joke:

![Boty, tell me a joke!](https://raw.githubusercontent.com/needsomesl33p/discord-chef-bot/master/images/joke.png)

Help me out here:

![Command Help](https://raw.githubusercontent.com/needsomesl33p/discord-chef-bot/master/images/help.png)

### Golden Quotes Feature ###

Feature request: [Collect golden quotes to a different channel]('https://github.com/needsomesl33p/discord-chef-bot/issues/2')

Feature implemented:

![5 reactions message and its context](https://raw.githubusercontent.com/needsomesl33p/discord-chef-bot/master/images/golden-quotes.png)

### Commands ###

```
meat
fishdish
get-recipe
veggie
cookie
create-channel
help-list
help
```

### Help System ###

Type the `!help` command to get the message:

```
​No Category:
  cookie         Recommends a cookie recipe from streetkitchen.hu
  create-channel Create a channel with the given name. For example: !create-c...
  fishdish       Recommends a fish dish recipe from streetkitchen.hu
  get-recipe     It returns a concrete recipe according to the given food name.
  help           Shows this message
  help-list      Returns all commands available. Then use !help [command]
  joke           Tells you a joke
  meat           You get some protein boost from streetkitchen.hu
  veggie         Recommends a veggie food from streetkitchen.hu

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```

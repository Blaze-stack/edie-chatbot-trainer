# a script to automate the training of the model using the data from discord and write them to the pattern.json file
# Author: @Blaze_dev
# Date: 2023-02-22
# Version: 1.0.0

import json
from colorama import Fore, Style
import discord
from discord.ext import commands

# open the pattern.json file
with open('pattern.json', 'r') as f:
    pattern = json.load(f)

# run the main bot
bot = commands.Bot(command_prefix='!', self_bot=True)

logo = f"""{Fore.CYAN}   _______   ________  ___  _______      
  |\  ___ \ |\   ___ \|\  \|\  ___ \     
  \ \   __/|\ \  \_|\ \ \  \ \   __/|    
   \ \  \_|/_\ \  \ \\\ \ \  \ \  \_|/__  
    \ \  \_|\ \ \  \_\\\ \ \  \ \  \_|\ \ 
     \ \_______\ \_______\ \__\ \_______\
      \|_______|\|_______|\|__|\|_______| Trainer By Blaze_dev"""
print(logo)
print("")
print("")


token = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Enter your token : {Fore.WHITE}")

# get the data from discord
@bot.event
async def on_ready():
    print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Logged in as {Fore.WHITE}{bot.user.name}#{bot.user.discriminator} {Fore.LIGHTBLACK_EX}with the id {Fore.WHITE}{bot.user.id}")
    print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Ready to train the model !")
    print("")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "":
        return
    message = message.content
    pattern["speechPatterns"].append(message)
    print(f"{Fore.WHITE}[ {Fore.GREEN}+ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Added {Fore.WHITE}{message} {Fore.LIGHTBLACK_EX}to the pattern.json file", end="\r")
    with open('pattern.json', 'w') as f:
        json.dump(pattern, f, indent=4)

bot.run(token, bot=False)

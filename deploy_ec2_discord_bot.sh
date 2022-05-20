#!/bin/bash

#######
# Ad-hoc deployment script on a free-tier EC2 instance.
# Swap the script variables then run:
# chmod +x deploy_ec2_discord_bot.sh
# sh deploy_ec2_discord_bot.sh
#######

DST_FOLDER='projects'
TOKEN='YourToken'
CHANNEL_ID='YourChannelID'

# Installing python3.8 latest
sudo amazon-linux-extras install python3.8

# Creating folder
mkdir -p ${DST_FOLDER}
cd ${DST_FOLDER}

# Pulling bot
git clone https://github.com/needsomesl33p/discord-chef-bot.git
cd discord-chef-bot

# Installing requirements
pip3.8 install -r requirements.txt

# Swapping Token and etc.
sed -i -E 's/    "token":.*/    "token": "'${TOKEN}'",/g' creds.json
sed -i -E 's/    "golden_quotes_chn_id":.*/    "golden_quotes_chn_id": "'${CHANNEL_ID}'",/g' creds.json

# Startup
python3.8 thats_my_bot.py &

# # APPLICATION ID:1132657680268394516
# # PUBLIC KEY: Add api key here [or use a file and read it]

# # to use a file, use the following code:
# # with open("API_KEY.txt", 'r') as file:
# # api_key = file.read().strip()
# # openai.api_key = api_key

# # and to use the token, use the following code:
# # with open("Token.txt", 'r') as file:
# # token = file.read().strip()
# # and then use the token variable to run the bot

# import discord
# import os
# import openai

# # file = input("Enter 1, 2, or 3 for loading the chat:\n")
# file = "1"
# match (file):
#   case "1":
#     file = "chat1.txt"
#   case "2":
#     file = "chat2.txt"
#   case "3":
#     file = "chat3.txt"
#   case _:
#     print("Invalid input, defaulting to chat1.txt")
#     exit()

# with open(file, 'r') as file:
#   chat = file.read()

# # with open("API_KEY.txt", 'r') as file:
# # #   api_key = os.environ['SECRET_API_KEY']
# #   openai.api_key = api_key
# # #   openai.api_key = os.environ['SECRET_API_KEY']
# # with open("API_KEY.txt", 'r') as file:
# with open("API_KEY.txt", 'r') as file:
#     api_key = file.read().strip()
#     openai.api_key = api_key
#     api_key = file.read().strip()
# openai.api_key = api_key


# with open("Token.txt", 'r') as file:
#   token = file.read().strip()
# # token = os.environ['SECRET_TOKEN']


# class MyClient(discord.Client):

#   async def on_ready(self):
#     print(f'Logged on as: {self.user}!')

#   async def on_message(self, message):
#     global chat
#     chat += f"{message.author}: {message.content}\n"
#     print(f'Message from {message.author}: {message.content}')

#     if self.user != message.author:
#       if self.user in message.mentions:
#         print(chat)
#         response = openai.Completion.create(
#           model="text-davinci-003",
#           prompt=f"{chat}\n Pandora_v1: ",
#           temperature=1,
#           max_tokens=512,
#           top_p=1,
#           frequency_penalty=0,
#           presence_penalty=0.6,
#         )
#         channel = message.channel
#         messageToSend = response.choices[0].text
#         await channel.send(messageToSend)


# intents = discord.Intents.default()
# intents.members = True

# Client = MyClient(intents=intents)
# Client.run(token)



import discord
import os
import openai

file = "1"
match (file):
  case "1":
    file = "chat1.txt"
  case "2":
    file = "chat2.txt"
  case "3":
    file = "chat3.txt"
  case _:
    print("Invalid input, defaulting to chat1.txt")
    exit()

with open(file, 'r') as file:
  chat = file.read()

with open("API_KEY.txt", 'r') as file:
  api_key = file.read().strip()
  openai.api_key = api_key

with open("Token.txt", 'r') as file:
  Token = file.read().strip()

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as: {self.user}!')

  async def on_message(self, message):
    global chat
    chat += f"{message.author}: {message.content}\n"
    print(f'Message from {message.author}: {message.content}')
    if self.user != message.author:
      if self.user in message.mentions:
        print(chat)
        response = openai.Completion.create(
          model="text-davinci-003",
          prompt=f"{chat}\n Pandora_v1: ",
          temperature=1,
          max_tokens=512,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.6,
        )
        channel = message.channel
        messageToSend = response.choices[0].text
        await channel.send(messageToSend)

intents = discord.Intents.default()
intents.members = True
Client = MyClient(intents=intents)
Client.run(Token)
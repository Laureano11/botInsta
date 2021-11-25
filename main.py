from instabot import Bot
import shutil
import time
from tqdm import tqdm
import json


avax= Bot()



def logear(bot):
    key= input("Ingrese contrasenia: ")
    bot.login(username="avax.indumentaria", password=key)


def sendMessageAll2(botUse, mensaje):
    for follower in botUse.followers :
        botUse.send_message(mensaje, follower)
    print("Sent An Individual Messages To Your Followers..")
    time.sleep(1)
    exit()


def sendMessageAll(bot):
    message=  input("Que mensaje desea enviar?: ")
    bot.send_message_all_users(bot,message)

def getUserNameFollowers(bot):
    lista=[]
    range= len(bot.followers)
    for i in range:
        lista.append(bot.get_username_from_user_id(bot.followers[i]))
    return lista

def getUserInfo(bot, id):
    userInfo=bot.get_user_info(id)
    return userInfo

def getMessages(bot):
    set= bot.get_messages()
    return set



logear(avax)

set= avax.get_messages()
print(set)


fileJson= json.loads(set)

print(fileJson["inbox"])











def deleteDirConfig():
    time.sleep(2)
    shutil.rmtree("config")

deleteDirConfig()
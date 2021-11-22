from instabot import Bot
import shutil
import time
from tqdm import tqdm

botardo = Bot()

botardo.login(username="", password="")




def send_message_all_users(botUse, mensaje):
    for follower in botUse.followers :
        botUse.send_message(mensaje, follower)
    print("Sent An Individual Messages To Your Followers..")
    time.sleep(1)
    exit()


message = input("Que mensaje desea enviar?")

##send_message_all_users(botardo, message)

print(botardo.followers)

botardo.send_messages(message, botardo.followers)

def all_followers_msg(botToUse):
    for users in



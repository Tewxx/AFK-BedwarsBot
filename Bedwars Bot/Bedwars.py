from javascript import require, On, Once, AsyncTask, once, off
import time
from utils.vec3_conversion import vec3_to_str
from colorama import Fore, Back, Style

mineflayer = require("mineflayer")
mineflayer_pathfinder = require("mineflayer-pathfinder")
mineflayerViewer = require('prismarine-viewer').mineflayer
vec3 = require("vec3")

# options
username = "9cap"

bot = mineflayer.createBot(
    {"auth": 'microsoft', "host": "play.pika-network.net", "version": "1.8.9", "hideErrors": False}
)

bot.loadPlugin(mineflayer_pathfinder.pathfinder)

@On(bot, "messagestr")
def handle_chat(this, username, message, *args, **kwargs):
    print(f"[CHAT] {username}: {message}")
    if "9cap has joined! (" in username or username + "9cap has joined! (" in message:
        print(Fore.GREEN+"\nYou have joined a bedwars game\n"+Fore.WHITE)
        time.sleep(1.2)
        bot.chat("gl everyone <3")

    if "You are now in team" in username or "You are now in team" in message:
        print(Fore.GREEN+"\nYou have now joined your team sit back and relax\n"+Fore.WHITE)
        InGame = True
        time.sleep(15)
        bot.chat("Sorry guys I have to go afk my mom keeps telling me to take a shower ;(")

    if "AFK!" in username or "AFK!" in message:
        print(Fore.YELLOW+"\nBeing AFK kicked, jumping for 3 seconds\n"+Fore.WHITE)
        bot.setControlState('jump', True)
        time.sleep(3)
        bot.setControlState('jump', False)
    if "[Match Recap]" in username or "[Match Recap]" in message  or "Click on your desired vote" in username or "Click on your desired vote" in message:
        print(Fore.YELLOW+"\nGame end detected. Returning to hub.\n"+Fore.WHITE)
        time.sleep(2)
        bot.chat("/hub")
        time.sleep(5)
        join_and_play()

def join_and_play():
    @Once(bot, "login")
    def handle_login(this):
        print(Fore.GREEN+"Joined Server/Transfered server"+Fore.WHITE)
        mineflayerViewer(bot, {})
        time.sleep(3)
        bot.chat("/server")
        time.sleep(1.2)
        bot.clickWindow(30, 0, 0) 
        time.sleep(1)
        print(Fore.GREEN+"Joined the Bedwars lobby"+Fore.WHITE)
        print(Fore.GREEN+"Walking up to NPC"+Fore.WHITE)

        goal_location = {
            "x": 6.5,  
            "y": 59,   
            "z": -44   
        }

        bot.pathfinder.setGoal(
            mineflayer_pathfinder.pathfinder.goals.GoalNear(
            goal_location["x"], goal_location["y"], goal_location["z"], 0
        ))
        time.sleep(15)
        bot.setQuickBarSlot(2) # -1
        time.sleep(1.2)
        entity = bot.nearestEntity()
        bot.attack(entity)
        time.sleep(1)
        bot.clickWindow(40, 0, 0) 
        
        pass
join_and_play()

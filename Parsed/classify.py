import os
import subprocess


folder_dict = {'a':"Apple", 'ch':"Chip", 'mh':"MermaidHair", 'nf': "NormieFish", 'uh': "UnicornHorn", "b": "Banana", 'c': "Coin", 'ds': "DragonScale", 'ec': "EpicCoin", 'ef': "EpicFish", 'gf': "GoldenFish", 'lp': "LifePotion", 'ws': "WolfSkin", 'ze': "ZombieEye", 'r':"Ruby"}

for f in os.listdir():
    if f[-3:] == "png":
        print("open -gj {}".format(f))
        subprocess.run("open {}".format(f), shell=True)
        selection = input()
        if folder_dict[selection] in os.listdir():
            os.rename(f, os.path.join(folder_dict[selection], f))
        else:
            print("BAD")
            break
    else:
        print(f)

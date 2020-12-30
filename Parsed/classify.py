import os
import subprocess


folder_dict = {'a':"Apple", 'ch':"Chip", 'mh':"MermaidHair", 'nf': "NormieFish", 'uh': "UnicornHorn", "b": "Banana", 'c': "Coin", 'ds': "DragonScale", 'ec': "EpicCoin", 'ef': "EpicFish", 'gf': "GoldenFish", 'lp': "LifePotion", 'ws': "WolfSkin", 'ze': "ZombieEye", 'r':"Ruby"}
folder_iter = {'a':0, 'ch':0, 'mh':0, 'nf':0, 'uh':0, "b":0, 'c':0, 'ds':0, 'ec':0, 'ef':0, 'gf':0, 'lp':0, 'ws':0, 'ze':0, 'r':0}

for key, value in folder_dict.items():
    folder_iter[key] = len(os.listdir(value))

# Start main loop
for f in os.listdir():
    if f[-3:] == "png":
        print("open -gj {}".format(f))
        subprocess.run("open {}".format(f), shell=True)
        selection = input()
        if folder_dict[selection] in os.listdir():
            os.rename(f, os.path.join(folder_dict[selection], folder_dict[selection]+"_"+str(folder_iter[selection])+".png"))
            folder_iter[selection] += 1
        else:
            print("BAD")
            break
    else:
        print(f)

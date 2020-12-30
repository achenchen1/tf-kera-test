import os
import subprocess


folder_iter = {'Apple':0, 'Chip':0, 'MermaidHair':0, 'NormieFish':0, 'UnicornHorn':0, "Banana":0, "Coin":0, 'DragonScale':0, 'EpicCoin':0, 'EpicFish':0, 'GoldenFish':0, 'LifePotion':0, 'WolfSkin':0, 'ZombieEye':0, 'Ruby':0}

for key, value in folder_iter.items():
    files = set(os.listdir(os.path.join("images", key)))
    for f in files:
        if f[:3] == "img":
            files.remove(f)

    folder_iter[key] = len(files)
     


# Start main loop
for d in os.listdir("images"):
    for f in os.listdir(os.path.join("images", d)):
        if f[-3:] == "img":
            os.rename(os.path.join("images", d, f), os.path.join("images", d, d+"_"+str(folder_iter[d])+".png"))
            folder_iter[d] += 1

import os

for d in os.listdir():
    if not os.path.isdir(d):
        continue
    for f in os.listdir(d):
        if f[-3:] == 'txt':
            os.rename(os.path.join(d, f), f)

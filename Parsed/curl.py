import subprocess

with open('list3.txt', "r") as f:
	i = 0
	for line in f:
		subprocess.run("curl -o images/img_{}.png {}".format(i, line), shell=True)
		i+=1

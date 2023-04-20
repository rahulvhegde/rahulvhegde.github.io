import subprocess
import sys
import os
import random

a=random.randint(1,100000)


msg = 'commit'+str(a)
repo_directory = 'C:/Users/Rahul V Hegde/Desktop/rahulvhegde.github.io'

subprocess.run(["git", "add", "C:/Users/Rahul V Hegde/Desktop/rahulvhegde.github.io/Data/pokemon_data2.json"], cwd=repo_directory)
# commit file
subprocess.run(["git", "commit", "-m", msg], cwd=repo_directory)
# push
subprocess.run(["git", "push"], cwd=repo_directory) 
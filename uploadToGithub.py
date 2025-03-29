import os
from datetime import datetime


commitMessage = f"Update data {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

os.system(f"git --git-dir=/home/ranmadhu/Computing/Python/Odds/GitRepo/odds/.git --work-tree=/home/ranmadhu/Computing/Python/Odds/GitRepo/odds add .")
os.system(f'git --git-dir=/home/ranmadhu/Computing/Python/Odds/GitRepo/odds/.git --work-tree=/home/ranmadhu/Computing/Python/Odds/GitRepo/odds commit -m"{commitMessage}"')
os.system("git --git-dir=/home/ranmadhu/Computing/Python/Odds/GitRepo/odds/.git --work-tree=/home/ranmadhu/Computing/Python/Odds/GitRepo/odds push")
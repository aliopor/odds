import os
import pandas as pd
from datetime import datetime


if os.name == "posix":
    pathname = "/home/ranmadhu/Computing/Python/Odds"
    csvPathname = "/home/ranmadhu/Computing/Python/Odds/GitRepo/odds"
else:
    pathname = r"Z:\Computing\Python\Odds"

allData = pd.read_csv(os.path.join(pathname,"data.csv.gz"),index_col=0, parse_dates=[0])
csvPath = os.path.join(csvPathname, "data.csv")

priceData=allData[allData["market"]=="48th Parliament of Australia"]
priceData = pd.pivot_table(priceData, values='price', index=[priceData.index], columns=['name'])/100
probData = priceData.apply(lambda x: 1/x)
probData["sum"] = probData.sum(axis=1)
probData = probData.loc[:, probData.columns != 'sum'].div(probData['sum'], axis=0)
probData.to_csv(csvPath)
print(probData)


commitMessage = f"Update data {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

os.system(f"git add {csvPath}")
os.system(f'git commit -m "{commitMessage}"')
os.system("git push origin main")
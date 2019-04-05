from pathlib import Path
#absoulte path
#Relative path

path = Path("emails")
print(path.exists())
path.mkdir()
print(path.exists())

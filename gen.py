import shutil
import sys
from pathlib import Path

day = str(sys.argv[1])

shutil.copytree("template", day)

file = Path(f"{day}/a.py")
file.rename(f"{day}/{day}.py")

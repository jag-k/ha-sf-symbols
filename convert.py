import json
from pathlib import Path
from os import listdir
import re

BASE_DIR = Path(__file__).resolve().parent
SF_SYMBOLS_PATH = BASE_DIR / 'SF_Symbols'
ALL_SYMBOLS = {}
RE_PATH = re.compile(r'<path d="(.*?)"')
files = sorted(listdir(SF_SYMBOLS_PATH))
files_length = len(files)
i = 0

for symbol_file in files:
    i += 1
    symbol_name = symbol_file.rstrip('.svg')
    print(f'\r{i:4}/{files_length:4}: {symbol_name}', end='')
    with (SF_SYMBOLS_PATH / symbol_file).open('r') as symbol_data:
        symbol_path_d = RE_PATH.findall(symbol_data.read())
        ALL_SYMBOLS[symbol_name] = str(symbol_path_d[0])

print('\rDone!')

with open('sf-symbols.json', 'w') as file:
    json.dump(ALL_SYMBOLS, file, indent=2)

with open('sf-symbols.min.json', 'w') as file:
    json.dump(ALL_SYMBOLS, file)
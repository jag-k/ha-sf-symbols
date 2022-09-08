import json
from pathlib import Path
from os import listdir
import re

BASE_DIR = Path(__file__).resolve().parent
SF_SYMBOLS_PATH = BASE_DIR / 'SF_Symbols'
ALL_SYMBOLS = {}
RE_PATH = re.compile(r' d="(.*?)"')
files = sorted(listdir(SF_SYMBOLS_PATH))
files_length = len(files)

i = 0
for symbol_file in files:
    i += 1
    symbol_name = symbol_file.rstrip('.svg')
    print(f'\r{i:4}/{files_length:4}: {symbol_name}', end='')
    symbol_file_path = SF_SYMBOLS_PATH / symbol_file
    with symbol_file_path.open('r') as symbol_data:
        symbol_path_d = RE_PATH.findall(symbol_data.read())
        try:
            ALL_SYMBOLS[symbol_name] = str(symbol_path_d[0])
        except Exception as err:
            print(f'\n\n{symbol_file_path}')
            raise err

print('\rDone!')

with open(BASE_DIR / 'sf-symbols.json', 'w') as file:
    json.dump(ALL_SYMBOLS, file, indent=2)

with open(BASE_DIR / 'sf-symbols.min.json', 'w') as file:
    json.dump(ALL_SYMBOLS, file)

with open(BASE_DIR / 'sf-symbols.raw.js', 'r') as raw, \
    open(BASE_DIR / 'sf-symbols.js', 'w') as res:
    res.write(
        raw.read().replace(
            "require('./sf-symbols.min.json')",
            json.dumps(ALL_SYMBOLS)
        )
    )

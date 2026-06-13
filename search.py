import os
import re

directory = r'c:\Users\kodav\Downloads\Farming pdd\frontend\src'
matches = []

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.ts') or file.endswith('.tsx'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                for i, line in enumerate(lines):
                    # Find all $ not followed by {
                    if re.search(r'\$(?!\{)', line):
                        # also ignore ending $ in variable like amount$
                        if re.search(r'(?<![a-zA-Z0-9_])\$(?!\{)', line):
                            print(f'{filepath}:{i+1}:{line.strip()}')
            except Exception as e:
                pass

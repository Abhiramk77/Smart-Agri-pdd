import os
import re

directory = r'c:\Users\kodav\Downloads\Farming pdd\frontend\src'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace literal $ followed by numbers, e.g. $1,200 or $1.20 or $0.80
    content = re.sub(r'\$(\d)', r'₹\1', content)
    
    # Replace $ inside template strings for currency, e.g. `$${amount}` -> `₹${amount}`
    content = re.sub(r'\$\$\{', r'₹${', content)
    
    # Replace $ in JSX text, e.g. >${totalEarnings} or > ${totalEarnings}
    # Look for > followed by optional spaces, then $, then optional spaces, then {
    content = re.sub(r'>(\s*)\$(\s*)\{', r'>\1₹\2{', content)
    
    # Replace $ in placeholder strings, e.g. placeholder="$" or placeholder="e.g., $1.20"
    content = re.sub(r'placeholder="([^"]*)\$([^"]*)"', r'placeholder="\1₹\2"', content)
    
    # Replace $ in other known strings like "Payment of $800"
    content = re.sub(r'of \$(\d)', r'of ₹\1', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.ts') or file.endswith('.tsx'):
            filepath = os.path.join(root, file)
            try:
                process_file(filepath)
            except Exception as e:
                pass

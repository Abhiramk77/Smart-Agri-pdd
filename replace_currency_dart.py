import os
import re

filepath = r'c:\Users\kodav\Downloads\Farming pdd\smart_agri_app\lib\main.dart'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace '\$' with '₹' in strings where it represents money
content = content.replace(r"'\$2.50/kg'", r"'₹2.50/kg'")
content = content.replace(r"'\$1,250'", r"'₹1,250'")
content = content.replace(r"'\$1.20/L'", r"'₹1.20/L'")
content = content.replace(r"'\$4,800/mo'", r"'₹4,800/mo'")
content = content.replace(r"'\$8.50/lb'", r"'₹8.50/lb'")
content = content.replace(r"'\$17,000'", r"'₹17,000'")
content = content.replace(r"'\$${val.toStringAsFixed(2)}'", r"'₹${val.toStringAsFixed(2)}'")
content = content.replace(r"'Price (e.g. \$2.50/kg)'", r"'Price (e.g. ₹2.50/kg)'")
content = content.replace(r"Icons.attach_money", r"Icons.currency_rupee")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {filepath}")

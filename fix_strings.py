import re
import os

def fix_astro_strings(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define a helper to replace multi-line quoted strings with single-line ones
    def single_line_replacer(match):
        quote = match.group(1)
        inner = match.group(2)
        # Only replace if it actually contains a newline
        if '\n' in inner:
            # Flatten whitespace and newlines
            flattened = ' '.join(inner.split())
            return f"{quote}{flattened}{quote}"
        return match.group(0)

    # Regex to find '...' and "..." that might span multiple lines
    # This is a bit greedy but we target specific patterns like desc: '...' or || "..."
    content = re.sub(r"desc:\s*(')([\s\S]*?)(')", lambda m: "desc: " + single_line_replacer(m), content)
    content = re.sub(r"\|\|\s*(\")([\s\S]*?)(\")", lambda m: "|| " + single_line_replacer(m), content)
    
    # Also fix the DIR objects that are particularly messy
    content = re.sub(r"\{ id: ' DIR_01'", "{ id: 'DIR_01'", content) # Fix leading space
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_astro_strings(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro')

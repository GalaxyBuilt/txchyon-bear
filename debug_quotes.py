import sys

def find_unmatched_quotes(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        single_quotes = line.count("'")
        double_quotes = line.count('"')
        backticks = line.count('`')
        
        if single_quotes % 2 != 0:
            print(f"Line {i+1}: Unbalanced single quotes")
        if double_quotes % 2 != 0:
            # Check if it's a multi-line tag start
            if not (line.strip().startswith('<') and '>' not in line):
                 print(f"Line {i+1}: Unbalanced double quotes")
        if backticks % 2 != 0:
            print(f"Line {i+1}: Unbalanced backticks")
        
        for char in line:
            if ord(char) < 32 and char not in '\n\r\t':
                print(f"Line {i+1}: Non-printable character found: {hex(ord(char))}")

if __name__ == "__main__":
    find_unmatched_quotes(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro')

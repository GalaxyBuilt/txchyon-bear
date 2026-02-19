import sys

def dump_hex(filepath, start_line, end_line):
    with open(filepath, 'rb') as f:
        lines = f.readlines()
    
    for i in range(start_line - 1, min(end_line, len(lines))):
        line = lines[i]
        print(f"Line {i+1} HEX:")
        print(" ".join(f"{b:02X}" for b in line))
        print(f"Line {i+1} TEXT:")
        print(line.decode('utf-8', errors='replace').strip())
        print("-" * 20)

if __name__ == "__main__":
    dump_hex(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro', 185, 195)

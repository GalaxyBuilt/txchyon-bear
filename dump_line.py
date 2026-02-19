import sys

def dump_line(filepath, line_no):
    with open(filepath, 'rb') as f:
        lines = f.readlines()
    if line_no <= len(lines):
        line = lines[line_no-1]
        print(f"Line {line_no} HEX: {line.hex(' ')}")
        print(f"Line {line_no} LEN: {len(line)}")

if __name__ == "__main__":
    dump_line(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro', 189)
    dump_line(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro', 190)

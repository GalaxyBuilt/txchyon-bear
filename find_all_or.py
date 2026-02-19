import re

def find_all_or(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    
    for m in re.finditer(b'\\|\\|', data):
        start = max(0, m.start() - 20)
        end = min(len(data), m.end() + 20)
        context = data[start:end].decode('utf-8', errors='replace')
        print(f"Found at {m.start()}: context: [ {context} ]")

if __name__ == "__main__":
    find_all_or(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro')

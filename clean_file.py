import sys

def clean_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Remove any SOH (0x01) or other weird low characters
    cleaned_data = bytearray()
    for b in data:
        if b == 1: # SOH
            continue
        if b < 32 and b not in [9, 10, 13]: # Not tab, LF, CR
            continue
        cleaned_data.append(b)
    
    with open(filepath, 'wb') as f:
        f.write(cleaned_data)

if __name__ == "__main__":
    clean_file(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro')

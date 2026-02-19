import re
import os

def final_clean_and_fix(filepath):
    with open(filepath, 'rb') as f:
        raw_data = f.read()
    
    # 1. Purge null bytes and weird control characters (but keep tab, CR, LF)
    cleaned_bytes = bytearray()
    for b in raw_data:
        if b == 0: continue # Null byte
        if b < 32 and b not in [9, 10, 13]: continue # Control chars
        cleaned_bytes.append(b)
    
    try:
        content = cleaned_bytes.decode('utf-8')
    except UnicodeDecodeError:
        content = cleaned_bytes.decode('utf-8', errors='replace')

    # 2. Fix duplicated desc: desc:
    content = content.replace('desc: desc:', 'desc:')
    
    # 3. Consolidate specific problematic multi-line strings
    
    # Fix the description in featured post
    content = re.sub(
        r'(\{featuredPost\.data\.description\s*\|\|\s*")([\s\S]*?)("\})',
        lambda m: m.group(1) + ' '.join(m.group(2).split()) + m.group(3),
        content
    )
    
    # Fix DIR objects
    def fix_dir_block(match):
        block = match.group(0)
        # Flatten the whole block into a single line for the array definition
        flattened = ' '.join(block.split())
        # Clean up common issues introduced by flattening
        flattened = flattened.replace('id: \' DIR_01\'', 'id: \'DIR_01\'')
        return flattened

    # Find the array of objects for DIR and SYS
    # This is a bit brute force but should work given the structure
    content = re.sub(r'\{\[\s*\{ id: \'DIR_01\'[\s\S]*?\}\s*\]\.map', fix_dir_block, content)
    content = re.sub(r'\{\[\s*\{ id: \'SYS_01\'[\s\S]*?\}\s*\]\.map', fix_dir_block, content)

    # 4. Final pass: fix doubled ||, correct import, and ensure apostrophes are escaped
    content = content.replace('|| ||', '||')
    content = content.replace('@/layouts/BaseBear.astro', '@/layouts/Base.astro')
    content = content.replace("isn' t", "isn&apos;t")
    content = content.replace("It's", "It&apos;s")
    content = content.replace("isn't", "isn&apos;t")
    
    # Optional: reduce excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    final_clean_and_fix(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro')

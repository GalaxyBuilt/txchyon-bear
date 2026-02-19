
import re
import os

def clean_duplicates(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean up double dark:bg-red-500/10 dark:bg-red-950/20
    content = re.sub(r'dark:bg-red-500/10\s+dark:bg-red-950/20', 'dark:bg-red-950/20', content)
    content = re.sub(r'dark:bg-orange-500/10\s+dark:bg-orange-950/20', 'dark:bg-orange-950/20', content)
    content = re.sub(r'bg-red-600/5\s+dark:bg-red-950/20', 'bg-red-500/5 dark:bg-red-950/20', content)
    content = re.sub(r'bg-orange-600/5\s+dark:bg-orange-950/20', 'bg-orange-500/5 dark:bg-orange-950/20', content)

    # Specific fix for BearGenesisPreview double backgrounds
    content = re.sub(r'bg-red-600/5\s+dark:bg-red-500/10\s+dark:bg-red-950/20', 'bg-red-500/5 dark:bg-red-950/20', content)
    content = re.sub(r'bg-orange-600/5\s+dark:bg-orange-500/10\s+dark:bg-orange-950/20', 'bg-orange-500/5 dark:bg-orange-950/20', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned Duplicates: {file_path}")

clean_duplicates(r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro')
clean_duplicates(r'c:\Users\NefuTrades\txchyon-bear\src\partials\BearGenesisPreview.astro')

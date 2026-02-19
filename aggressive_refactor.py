
import re
import os

def refactor_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace hardcoded red/dark backgrounds in classes
    # Matches bg-red-900/20, bg-red-950/30, etc.
    content = re.sub(r'bg-red-[0-9]{3}/[0-9]{2}', 'bg-red-500/10 dark:bg-red-950/20', content)
    content = re.sub(r'bg-orange-[0-9]{3}/[0-9]{2}', 'bg-orange-500/10 dark:bg-orange-950/20', content)
    content = re.sub(r'bg-amber-[0-9]{3}/[0-9]{2}', 'bg-amber-500/10 dark:bg-amber-950/20', content)
    content = re.sub(r'bg-emerald-[0-9]{3}/[0-9]{2}', 'bg-emerald-500/10 dark:bg-emerald-950/20', content)
    
    # 2. Replace hardcoded red/amber borders
    content = re.sub(r'border-red-[0-9]{3}/[0-9]{2}', 'bear-border-accent', content)
    content = re.sub(r'border-orange-[0-9]{3}/[0-9]{2}', 'bear-border-accent', content)
    content = re.sub(r'border-amber-[0-9]{3}/[0-9]{2}', 'bear-border-accent', content)
    content = re.sub(r'border-emerald-[0-9]{3}/[0-9]{2}', 'bear-border-accent', content)
    
    # 3. Replace inline radial gradients for dots/grids
    # Matches radial-gradient(circle, #b91c1c 1px, transparent 1px)
    content = re.sub(r'radial-gradient\(circle,\s*#b91c1c\s*1px,\s*transparent\s*1px\)', 
                     'radial-gradient(circle, var(--color-bear-accent) 1px, transparent 1px)', content)
    # Matches linear-gradient(#b91c1c 1px, transparent 1px)
    content = re.sub(r'linear-gradient\(#b91c1c\s*1px,\s*transparent\s*1px\)', 
                     'linear-gradient(var(--color-bear-accent) 1px, transparent 1px)', content)
    # Matches linear-gradient(90deg, #b91c1c 1px, transparent 1px)
    content = re.sub(r'linear-gradient\(90deg,\s*#b91c1c\s*1px,\s*transparent\s*1px\)', 
                     'linear-gradient(90deg, var(--color-bear-accent) 1px, transparent 1px)', content)

    # 4. Handle complex gradients in classes
    content = re.sub(r'bg-gradient-to-br from-red-900/20 to-orange-900/20', 
                     'bg-gradient-to-br from-red-500/10 to-orange-500/10 dark:from-red-900/20 dark:to-orange-900/20', content)
    content = re.sub(r'bg-gradient-to-br from-amber-900/20 to-red-900/20', 
                     'bg-gradient-to-br from-amber-500/10 to-red-500/10 dark:from-amber-900/20 dark:to-red-900/20', content)
    
    # 5. Handle dialog/floating elements
    content = re.sub(r'bg-black/80', 'bear-bg-card/80', content)
    content = re.sub(r'background:\s*linear-gradient\(135deg,\s*#0a0c0e\s*0%,\s*#030405\s*100%\)', 
                     'background: var(--color-bear-bg)', content)

    # 6. Specific fix for h1-h6 in the style block
    content = re.sub(r'h1,\s*h2,\s*h3,\s*h4,\s*h5,\s*h6\s*{\s*color:\s*white;\s*}', 
                     'h1, h2, h3, h4, h5, h6 { color: var(--color-bear-text); }', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Aggressively Refactored: {file_path}")

files_to_refactor = [
    r'c:\Users\NefuTrades\txchyon-bear\src\pages\index.astro',
    r'c:\Users\NefuTrades\txchyon-bear\src\partials\BearGenesisPreview.astro'
]

for f in files_to_refactor:
    refactor_file(f)

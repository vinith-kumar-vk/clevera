import os

replacements = {
    "il² il": "Clevera",
    "il² RMUTTO": "Clevera",
    "il² rmutto": "Clevera",
    "il²": "Clevera",
    "RMUTTO": "Clevera",
    "rmutto": "Clevera"
}

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content = content
        for k, v in replacements.items():
            new_content = new_content.replace(k, v)

        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
    except Exception as e:
        pass

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('node_modules', 'vendor', '.git', 'storage', 'bootstrap')]
    for file in files:
        if file.endswith('.php') or file.endswith('.blade.php') or file.endswith('.js') or file.endswith('.css'):
            filepath = os.path.join(root, file)
            replace_in_file(filepath)

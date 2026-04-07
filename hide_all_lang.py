import os

replacements = {
    '<form method="POST" class="language-selector" style="display: inline;">': '<form method="POST" class="language-selector" style="display: none !important;">',
    '<div class="home-lang-switch" aria-label="Language">': '<div class="home-lang-switch" aria-label="Language" style="display: none !important;">',
    '<div class="home-lang-switch" style="padding: 0 20px 16px; justify-content: center;">': '<div class="home-lang-switch" style="display:none !important; padding: 0 20px 16px; justify-content: center;">',
    'class="footer-lang-form"\n                    style="display:inline;"': 'class="footer-lang-form"\n                    style="display:none !important;"',
    'class="footer-lang-form" style="display:inline;"': 'class="footer-lang-form" style="display:none !important;"',
    '<select class="footer-lang">': '<select class="footer-lang" style="display: none !important;">',
    '<select class="footer-lang-old">': '<select class="footer-lang-old" style="display: none !important;">',
    '<select class="f-lang-select">': '<select class="f-lang-select" style="display: none !important;">',
    'class="footer-lang-form"\r\n                    style="display:inline;"': 'class="footer-lang-form"\r\n                    style="display:none !important;"'
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

for root, dirs, files in os.walk('resources'):
    for file in files:
        if file.endswith('.blade.php'):
            filepath = os.path.join(root, file)
            replace_in_file(filepath)

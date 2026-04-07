import os

replacements = {
    "<option>Thai</option>": "<option style=\"display:none;\">Thai</option>",
    "<option value=\"th\" @selected(app()->getLocale() === 'th')>{{ __('home.lang_thai') }}</option>": "<option style=\"display:none;\" value=\"th\" @selected(app()->getLocale() === 'th')>{{ __('home.lang_thai') }}</option>",
    "class=\"home-lang-btn {{ app()->getLocale() === 'th' ? 'active' : '' }}\">{{ __('home.lang_thai') }}": "style=\"display:none;\" class=\"home-lang-btn {{ app()->getLocale() === 'th' ? 'active' : '' }}\">{{ __('home.lang_thai') }}"
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

import os

replacements = {
    "<td>Maths</td>": "<td>Machine Learning 101</td>",
    "<td>Creative</td>": "<td>Creative UI/UX Design</td>",
    "<td>Arts</td>": "<td>Digital Arts & Media</td>",
    "Guide 2 Maths": "Mastering Algorithms",
    "Mastering Maths": "Mastering Algorithms",
    "Bigger Class": "Clevera Pro Plan",
    "TutorX Pro": "Clevera Pro Max",
    "Exam Module": "Certification Module",
    "Breakout Room": "Mentor Sessions",
    "<td>Johny</td>": "<td>Subscription Fee</td>",
    "<span>Jhonny</span>": "<span>Alex (Student)</span>",
    "Jhon34@gmail.com": "alex_backup@gmail.com",
    "jhon@gmail.com": "alex@gmail.com"
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
        if file.endswith('.php') or file.endswith('.blade.php'):
            filepath = os.path.join(root, file)
            replace_in_file(filepath)

import os

replacements = {
    "Veterinary Nursing Assistant Course - Chapter 4": "Advanced AI & Machine Learning - Chapter 4",
    "Veterinary Nursing Assistant Course": "Advanced AI & Machine Learning",
    "Learn the essential skills to become a certified Veterinary Nursing Assistant. This comprehensive course covers animal care, clinical procedures, and emergency response in a professional setting.": "Learn the essential skills to master Artificial Intelligence and Machine Learning. This comprehensive course covers neural networks, deep learning, and practical applications in a professional setting.",
    "Building a Sustainable Startup: Strategies for Success": "Web Development Bootcamp: Frontend to Full Stack",
    "Building a Sustainable Startup": "Web Development Bootcamp",
    "Rajamangala Identity Course": "Cloud Computing & DevOps Masterclass",
    "Explore the cultural identity and values of Rajamangala University.": "Explore modern cloud architectures and DevOps methodologies."
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

import os
import shutil
from collections import defaultdict

FILE_CATEGORIES = {
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.odt', '.rtf'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.mkv', '.flv', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Scripts': ['.py', '.js', '.sh', '.bat'],
    'Spreadsheets': ['.xls', '.xlsx', '.ods'],
    'Presentations': ['.ppt', '.pptx', '.odp'],
    'HTML': ['.html', '.htm'],
    'CSS': ['.css', '.scss', '.sass'],
    'JavaScript': ['.js', '.jsx'],
    'Others': []
}

def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return
    
    categorized_files = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()
            
            categorized = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    categorized_files[category].append(file_path)
                    categorized = True
                    break
            
            if not categorized:
                categorized_files['Others'].append(file_path)
    
    for category, files in categorized_files.items():
        if category == 'Others':
            continue
        
        category_dir = os.path.join(directory, category)
        os.makedirs(category_dir, exist_ok=True)

        for file_path in files:
            shutil.move(file_path, category_dir)
            print(f"Moved '{file_path}' to '{category_dir}'")

    print("File organization complete.")

if __name__ == "__main__":
    directory = input("Enter the directory to organize: ").strip()
    organize_files(directory)
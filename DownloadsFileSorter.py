import os
import shutil


def sort_files():
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    extensions = {
        'Winrar': ['rar', 'zip', '7z'],
        'Torrents': ['torrent'],
        'PDFs': ['pdf'],
        'Word Documents': ['doc', 'docx'],
        'MP3s': ['mp3'],
        'Video Files': ['mp4', 'mov', 'avi', 'mkv'],
        'Python Files': ['py'],
        'Installer Files': ['exe', 'msi'],
        'Java Files': ['java', 'jar'],
        'Image Files': ['png', 'jpg', 'jpeg', 'bmp'],
        'GIFs': ['gif'],
        'Text Files': ['txt']
    }

    for file in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file)
        if not os.path.isfile(file_path):
            continue
        if os.path.dirname(file_path) != downloads_path:
            continue
        file_extension = file.split('.')[-1]
        for folder, ext_list in extensions.items():
            if file_extension.lower() in ext_list:
                folder_path = os.path.join(downloads_path, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(file_path, os.path.join(folder_path, file))
                break

    print("Sorted all items in the 'Downloads' folder. What would you do without me?")


if __name__ == "__main__":
    sort_files()

import os

def count_files_and_folders(directory):
    num_files = 0
    num_folders = 0
    file_details = []

    for root, dirs, files in os.walk(directory):
        num_folders += len(dirs)
        num_files += len(files)
        file_details.append({
            'folder': root,
            'files': files
        })

    return num_files, num_folders, file_details

directory = r'F:\JPOG ISO FILE\Jurassic Park Operation Genesis'
num_files, num_folders, file_details = count_files_and_folders(directory)

print(f'>>Total number of files: {num_files}')
print(f'>>Total number of folders: {num_folders}')
print(f'>>Details of files in each folder:')

for detail in file_details:
    print(f">>Folder: {detail['folder']}")
    print(f">>Files: {', '.join(detail['files'])}")
    print()
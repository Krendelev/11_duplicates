import os
import sys


def get_duplicates(path):
    file_dict, duplicates = {}, {}
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            dup_location = file_dict.setdefault((name, file_size), [])
            if dup_location:
                duplicates.update({name: dup_location})
            dup_location.append(root)
    return duplicates


def print_duplicates(duplicates):
    if duplicates:
        print('Duplicates found:')
        for name, paths in duplicates.items():
            output = ['/'.join([path, name]) for path in paths]
            print(*output, sep='\n', end='\n\n')
    else:
        print('Duplicates not found')


if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        print('Please specify directory name')
    if os.path.isdir(path):
        print_duplicates(get_duplicates(path))
    else:
        print('Not a directory')

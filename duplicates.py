import os
import sys


def get_duplicates(path):
    file_dict = {}
    for root, dirs, files in os.walk(path):
        for name in files:
            file_path = os.path.join(root, name)
            file_size = os.path.getsize(file_path)
            dup_location = file_dict.setdefault((name, file_size), []).append(file_path)
    return file_dict


def print_duplicates(duplicates):
    output = []
    for name, paths in duplicates.items():
        if len(paths) > 1:
            output.extend([path for path in paths])
    if output:
        print('Duplicates found:')
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

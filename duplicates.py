import os
import sys


def get_files_locations(path):
    locations = {}
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            file_dict_insertion = locations.setdefault(
                (filename, file_size),
                []
                ).append(file_path)
    return locations


def print_duplicates(files_locations):
    duplicates = [
        path for paths in files_locations.values()
        for path in paths if len(paths) > 1
    ]
    if duplicates:
        print('Duplicates found:', *duplicates, sep='\n')
    else:
        print('Duplicates not found')


if __name__ == '__main__':
    try:
        path = sys.argv[1]
    except IndexError:
        print('Please specify directory name')
    if os.path.isdir(path):
        print_duplicates(get_files_locations(path))
    else:
        print('{} is not a directory'.format(path))

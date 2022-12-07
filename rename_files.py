#!/usr/bin/env python3

import os
import sys


if len(sys.argv) < 2:
    print("You forget to provide path of directory as a system arument")
    sys.exit()

directory_path = sys.argv[1]


def rename_file(files_directory):
    files_list = os.listdir(files_directory)
    for filename in files_list:
        if not filename.startswith(" ") and not filename.endswith(" "):
            print(filename)
        # In replace method first argument is old_string and second argument is new_string
            os.rename(os.path.join(files_directory, filename), os.path.join(
                files_directory, filename.replace(" ", "_")))


rename_file(directory_path)

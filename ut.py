

def read_file(path):
    file = open(path, "r")
    contents = file.read()
    return contents


def read_file_lines(path):
    file = open(path, "r")
    contents = file.readlines()
    return contents


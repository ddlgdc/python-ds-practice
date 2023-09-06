def read_file_list(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            print(f'- {line}')
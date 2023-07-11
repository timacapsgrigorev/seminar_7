from random import randint, choice
from os import mkdir


VOVELS = 'euioay'
CONSONANTS = 'wrtpsdfghklzcvnmb'


def fill_file_nums(rows: int, filename: str):
    with open(filename, 'w') as file:
        for _ in range(rows):
            first_num = randint(-1000, 1000)
            second_num = float(f'{randint(-1000, 1000)}.{randint(0, 1000)}')
            file.write(f'{first_num} | {second_num}\n')


def fill_file_names(rows: int, filename: str):
    with open(filename, 'w') as file:
        for _ in range(rows):
            print(generate_name(4, 7), file=file)


def generate_name(start, stop) -> str:
    return ''.join([choice(choice([VOVELS, CONSONANTS]))
                    for _ in range(randint(start, stop))]).capitalize()


def gen_random_files(min_len_name: int = 6,
                     max_len_name: int = 30,
                     min_count_bytes: int = 256,
                     max_count_bytes: int = 4096,
                     files_count: int = 42,
                     extensions: list[str] = None,
                     path: str = 'files_for_task4'):

    for _ in range(files_count):
        extension = choice(extensions)
        filename = generate_name(min_len_name, max_len_name)
        try:
            write_to_file(path, filename,
                          extension,
                          min_count_bytes, max_count_bytes)
        except FileNotFoundError:
            mkdir(path)
            write_to_file(path, filename,
                          extension,
                          min_count_bytes, max_count_bytes)


def gen_random_files_with_extensions(extensions: list[str],
                                     num_files: int,
                                     path: str = 'files_for_task4'):
    gen_random_files(
        extensions=extensions,
        files_count=num_files,
        path=path
    )


def write_to_file(path,
                  filename,
                  extension,
                  min_count_bytes,
                  max_count_bytes):
    with open(f'{path}/{filename + extension}', 'w') as file:
        data = bytes(randint(1, 255) for _ in range(randint(min_count_bytes,
                                                            max_count_bytes)))
        file.write(str(data))

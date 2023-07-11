from file_utils.file_generator import gen_random_files_with_extensions

gen_random_files_with_extensions(
    extensions=['.txt', '.md', '.csv', '.json'],
    num_files=12
)

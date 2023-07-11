import os


def batch_rename_files(desired_name, num_digits, source_extension, target_extension, name_range):
    directory = '.'  
    file_list = os.listdir(directory)

    for i, file_name in enumerate(file_list):
        file_extension = os.path.splitext(file_name)[1]

        if file_extension == source_extension and name_range[0] <= i + 1 <= name_range[1]:
            original_name = file_name[:-len(file_extension)]
            new_name = original_name[name_range[0] - 1:name_range[1]] + '_' + desired_name + str(i + 1).zfill(
                num_digits) + target_extension
            os.rename(os.path.join(directory, file_name), os.path.join(directory, new_name))


batch_rename_files('rename', 2, '.txt', '.md', [3, 6])

import os


def validate_folder(folder_path):
    """
    Check if folder_path exists and is a valid directory.
    :param folder_path: (str) path to the folder to be validated
    :return: (bool) True if folder_path is valid, False otherwise
    """
    if not os.path.exists(folder_path):
        return False

    if not os.path.isdir(folder_path):
        return False

    return True

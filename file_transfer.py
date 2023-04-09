import os
import shutil
import logging

class FileTransfer:
    def __init__(self, folder_pairs):
        self.folder_pairs = folder_pairs

    def move_files(self):
        for folder_pair in self.folder_pairs:
            source_folder = folder_pair["source_folder"]
            dest_folder = folder_pair["dest_folder"]
            file_extensions = folder_pair["file_extensions"].replace(" ", "").split(",")

            if not os.path.isdir(dest_folder):
                logging.error("Destination folder is not valid: {}".format(dest_folder))
                continue

            for filename in os.listdir(source_folder):
                if any(filename.endswith(extension) for extension in file_extensions):
                    shutil.move(os.path.join(source_folder, filename), dest_folder)
                    logging.info("Moved file {} from {} to {}".format(filename, source_folder, dest_folder))

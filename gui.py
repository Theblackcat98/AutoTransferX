import tkinter as tk
from tkinter import filedialog, messagebox


class FileTransferGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Transfer App")
        self.folder_pairs = []
        
        self.source_label = tk.Label(master, text="Source Folders:")
        self.source_label.grid(row=0, column=0)

        self.dest_label = tk.Label(master, text="Destination Folder:")
        self.dest_label.grid(row=0, column=1)

        self.add_button = tk.Button(master, text="Add Folder Pair", command=self.add_folder_pair)
        self.add_button.grid(row=0, column=2)

        self.move_button = tk.Button(master, text="Move Files", command=self.move_files)
        self.move_button.grid(row=0, column=3)

    def add_folder_pair(self):
        source_folder = filedialog.askdirectory()
        if source_folder:
            dest_folder = filedialog.askdirectory()
            if dest_folder:
                file_extensions = filedialog.askstring("File Extensions", "Enter file extensions separated by comma: ")
                folder_pair = {"source_folder": source_folder, "dest_folder": dest_folder, "file_extensions": file_extensions}
                self.folder_pairs.append(folder_pair)
                row = len(self.folder_pairs) + 1
                source_var = tk.StringVar()
                source_var.set(source_folder)
                dest_var = tk.StringVar()
                dest_var.set(dest_folder)
                source_entry = tk.Entry(self.master, textvariable=source_var, state=tk.DISABLED)
                source_entry.grid(row=row, column=0)
                dest_entry = tk.Entry(self.master, textvariable=dest_var, state=tk.DISABLED)
                dest_entry.grid(row=row, column=1)
                check_var = tk.IntVar()
                check_button = tk.Checkbutton(self.master, variable=check_var)
                check_button.grid(row=row, column=2)
                self.folder_pairs[-1]["source_var"] = source_var
                self.folder_pairs[-1]["dest_var"] = dest_var
                self.folder_pairs[-1]["check_var"] = check_var
                self.folder_pairs[-1]["source_entry"] = source_entry
                self.folder_pairs[-1]["dest_entry"] = dest_entry
                self.folder_pairs[-1]["check_button"] = check_button

    def move_files(self):
        # Move files from source folders to destination folders
        pass


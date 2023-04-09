import tkinter as tk
from tkinter import filedialog, messagebox
import json
import os
import shutil
from datetime import datetime

class FileTransferApp:
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

        # create log file
        self.log_file = open('file_transfer_log.txt', 'a')
        
    def add_folder_pair(self):
        source_folder = filedialog.askdirectory()
        if source_folder:
            dest_folder = filedialog.askdirectory()
            if dest_folder:
                file_extensions = tk.simpledialog.askstring("File Extensions", "Enter file extensions separated by comma: ")
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
                self.folder_pairs[-1]["source_var"] = str(source_var)
                self.folder_pairs[-1]["dest_var"] = str(dest_var)
                self.folder_pairs[-1]["check_var"] = check_var
                self.folder_pairs[-1]["source_entry"] = source_entry
                self.folder_pairs[-1]["dest_entry"] = dest_entry
                self.folder_pairs[-1]["check_button"] = check_button


    def move_files(self):
        for folder_pair in self.folder_pairs:
            source_folder = folder_pair["source_folder"]
            dest_folder = folder_pair["dest_folder"]
            file_extensions = folder_pair["file_extensions"].replace(" ", "").split(",")
            source_var = folder_pair["source_var"]
            dest_var = folder_pair["dest_var"]
            check_var = folder_pair["check_var"]
            source_entry = folder_pair["source_entry"]
            dest_entry = folder_pair["dest_entry"]
            check_button = folder_pair["check_button"]
            
            if check_var.get():
                if not os.path.isdir(dest_folder):
                    tk.messagebox.showerror("Error", "Destination folder is not valid.")
                    self.log_error("Error: Destination folder is not valid.")
                    return

                # create a log entry for this folder pair
                self.log_folder_pair(source_folder, dest_folder, file_extensions)

                for filename in os.listdir(source_folder):
                    if any(filename.endswith(extension) for extension in file_extensions):
                        shutil.move(os.path.join(source_folder, filename), dest_folder)
                tk.messagebox.showinfo("Success", "Files moved successfully from {} to {}.".format(source_folder, dest_folder))
                self.log_success("Success: Files moved successfully from {} to {}.".format(source_folder, dest_folder))

                folder_pair["source_var"] = str(source_var)
                folder_pair["dest_var"] = str(dest_var)
        
        with open("folder_pairs.json", "w") as f:
            json.dump(self.folder_pairs, f, default=str)

    def log_folder_pair(self, source_folder, dest_folder, file_extensions):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"{current_time} - Files transferred from {source_folder} to {dest_folder} with extensions {file_extensions}"
        self.log_file.write(message + "\n")
        
    def check_files(self):
        for folder_pair in self.folder_pairs:
            # ...
            if files_exist:
                self.log_folder_pair(folder_pair)
                self.move_files()
        self.after(5000, self.check_files)



root = tk.Tk()
app = FileTransferApp(root)
root.mainloop()
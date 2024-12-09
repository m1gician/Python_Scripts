import os

file_path = "/home/msmith/Py_Backups/Test.cfg"

try:
	if os.path.exists(file_path):
	    os.chmod(file_path, 0o666)

            print("File permissions modified successfully!")
	else:
	    print("File not found:", file_path)
except PermissionError:
	print("Permission denied: You don't have the necessary permissions to change the permissions of this file.")

with open(file_path, "w") as file:
	new_content = "New content to replace the existing content"
	file.write(new_content)

print("File content modified successfully!")

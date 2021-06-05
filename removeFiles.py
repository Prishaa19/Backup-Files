import os
import shutil
import time

def main():

	
	deletedFolderCount = 0
	deletedFilesCount = 0
	path = "sample.txt"
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)
	if os.path.exists(path):
		for rootFolder, folders, files in os.walk(path):
			if seconds >= get_file_or_folder_age(rootFolder):
				remove_folder(rootFolder)
				deletedFolderCount += 1 
				break

			else:
				for folder in folders:
					folderpath = os.path.join(rootFolder, folder)
					if seconds >= get_file_or_folder_age(folderpath):
						remove_folder(folderpath)
						deletedFolderCount += 1 
				for file in files:
					file_path = os.path.join(rootFolder, file)
					if seconds >= get_file_or_folder_age(file_path):
						remove_file(file_path)
						deletedFilesCount += 1 

		else:
			if seconds >= get_file_or_folder_age(path):
				remove_file(path)
				deletedFilesCount += 1 
	else:
		print(f'"{path}" is not found')
		deletedFilesCount += 1 

	print(f"Total folders deleted: {deletedFolderCount}")
	print(f"Total files deleted: {deletedFilesCount}")


def remove_folder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")

	else:
		print(f"Unable to delete the "+path)



def remove_file(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")

	else:
		print("Unable to delete the "+path)


def get_file_or_folder_age(path):
	ctime = os.stat(path).st_ctime
	return ctime


if __name__ == '__main__':
	main()
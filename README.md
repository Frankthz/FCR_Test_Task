Programming language and libraries used:
Python
Libraries: os, shutil, logging, time, argparse


Structure:

setup_logging(file_path) - setup logging package; format log string and link to log file. receive file path by argument.  

sync_folders(source_folder, replica_folder): Sync all files from two folders. Check if all files in source folder exists on replica folder, if not create them, and remove all files that not exist on source folder. All of this actions are logged in console and log file, including “synchronization error”.  

main(): parse command line arguments and execute sycn_folders function according to the time interval received in the arguments.

To run the script you should go to the terminal and type:
python3 main.py [source_folder] [replica_folder] [period] [log_file]
args:
source_folder: path to the original folder.
replica_folder: path to the backup folder.
period: synchronization interval, in seconds.
log:file: path to the log file.
example: python3 main.py ./source ./replica 60 ./log_file.txt

import os
import shutil
import time
import logging
import argparse


def setup_logging(log_file_path):
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


def sync_folders(source_folder, replica_folder):
    logging.info(f"Synchronization started: {source_folder} -> {replica_folder}")

    try:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_folder)
                replica_path = os.path.join(replica_folder, relative_path)

                os.makedirs(os.path.dirname(replica_path), exist_ok=True)

                shutil.copy2(source_path, replica_path)
                logging.info(f"Copied: {source_path} -> {replica_path}")

        for root, dirs, files in os.walk(replica_folder):
            for file in files:
                replica_path = os.path.join(root, file)
                source_path = os.path.join(source_folder, os.path.relpath(replica_path, replica_folder))

                if not os.path.exists(source_path):
                    os.remove(replica_path)
                    logging.info(f"Removed: {replica_path}")

        logging.info("Synchronization successful")

    except Exception as e:
        logging.error(f"Synchronization failed: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description='Folder Synchronization')
    parser.add_argument("source_folder")
    parser.add_argument("replica_folder")
    parser.add_argument("period", type=int)
    parser.add_argument("log_file")

    args = parser.parse_args()

    setup_logging(args.log_file)

    while True:
        sync_folders(args.source_folder, args.replica_folder)
        time.sleep(args.period)


if __name__ == "__main__":
    main()


# Code for running app on terminal
# python3 main.py ./source ./replica 60 ./log_file.txt
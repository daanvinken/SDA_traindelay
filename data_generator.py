import os
import subprocess
import sys

# Current program path
path = os.getcwd()

# Destination data folder
dest_folder = path + '/data'

# Destination for core data
dest_file = path + '/data/vertrektijden.csv'

# Link to remote core data
link = 'https://www.dropbox.com/s/yfgwigjqav5xi0h/vertrektijden.csv?dl=0'

# Make sure data directory doesn't exist yet
if os.path.exists(dest_folder):
    print(dest_folder, "already exists, skipping")
else:
    try:
        # Create data folder
        os.mkdir(dest_file)

    except OSError:
        print("Creation of {} failed".format(dest_folder))

        sys.exit()
    else:
        print("Creation of {} succesful".format(dest_folder))

# Run command
try:
    print("Fetching csv from", link)
    print("Saving file to", dest_file)

    subprocess.check_call(["wget", "-nv", "-O", dest_file, link])
except subprocess.CalledProcessError:
    print("Failed to execute command", 'wget -nv -O {} "{}"'.format(dest_file, link))

    sys.exit()
else:
    print("Successfully fetched and stored data in", dest_file)

# Generate necessary data files
subprocess.check_call([
    "python3",
    "split.py",
    "--delay=1"
    "--file=delay.csv"
])

subprocess.check_call([
    "python3",
    "split.py",
    "--transporter=NS"
    "--file=ns_vertrektijden.csv"
])

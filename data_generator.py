from importlib import util
import os
import subprocess
import sys
from trajecten import get_paths

# Current program path
path = os.getcwd()

# Destination data folder
dest_folder = path + '/data'

# Destination for core data
dest_file = path + '/data/vertrektijden.csv'

# Link to remote core data
link = 'https://www.dropbox.com/s/yfgwigjqav5xi0h/vertrektijden.csv?dl=0'

print()
print("Creating data folder...")

# Make sure data directory doesn't exist yet
if os.path.exists(dest_folder):
    print(dest_folder, "already exists, skipping")
else:
    try:
        # Create data folder
        os.mkdir(dest_file)

    except OSError:
        print("Creation of {} failed, aborting".format(dest_folder))

        sys.exit()
    else:
        print("Creation of {} succesful".format(dest_folder))

print()
print("Gathering external data...")

if not os.path.isfile(dest_file):
    # Download and save file
    try:
        print("Fetching csv from", link)
        print("Saving file to", dest_file)

        subprocess.check_call(["wget", "-nv", "-O", dest_file, link])
    except subprocess.CalledProcessError:
        print("Failed to execute command", 'wget -nv -O {} "{}", aborting'.format(dest_file, link))

        sys.exit()
    else:
        print("Successfully fetched and stored data in", dest_file)
else:
    print(dest_file, "already exists, skipping")

print()
print("Generating required files...")

# Generate necessary data files

if not os.path.isfile(dest_folder + '/delay.csv'):
    print("Generating file with delayed trains...")

    try:
        subprocess.check_call([
            "python3",
            "split.py",
            "--delay=1",
            "--transporter=NS",
            "--file=delay.csv"
        ])
    except subprocess.CalledProcessError:
        print("Failed to generate file with delayed NS trains, aborting")

        sys.exit()
else:
    print(dest_folder + "/delay.csv", "already exists, skipping")

if not os.path.isfile(dest_folder + '/ns_vertrektijden.csv'):
    print("Generating file with only NS trains...")

    try:
        subprocess.check_call([
            "python3",
            "split.py",
            "--transporter=NS",
            "--file=ns_vertrektijden.csv"
        ])
    except subprocess.CalledProcessError:
        print("Failed to generate file with only NS trains, aborting")

        sys.exit()
else:
    print(dest_folder + "/ns_vertrektijden.csv", "already exists, skipping")

if not os.path.isfile(dest_folder + '/ns_paths.txt'):
    print("Could not find", dest_folder + '/ns_paths.txt', "did you download the project correctly?")
    print("Generating graph data, this may take up to an hour...")

    # Generate graph data
    get_paths(dest_folder + "/ns_vertrektijden.csv")
else:
    print(dest_folder + "/ns_paths.txt", "already exists, skipping")

if not os.path.isfile(dest_folder + '/ams_centraal.csv'):
    print("Generating file with delayed trains...")

    try:
        subprocess.check_call([
            "python3",
            "split.py",
            "--station=ASD"
        ])
    except subprocess.CalledProcessError:
        print("Failed to generate file with delayed NS trains, aborting")

        sys.exit()
else:
    print(dest_folder + "/ams_centraal.csv", "already exists, skipping")

if not os.path.isfile(dest_folder + '/neerslag.txt'):
    print("[WARNING]: Could not find", dest_folder + '/neerslag.txt')
    print("Did you download the project correctly?")

if not os.path.isfile(dest_folder + '/wind_per_uur.txt'):
    print("[WARNING]: Could not find", dest_folder + '/wind_per_uur.txt')
    print("Did you download the project correctly?")

print()

# Required modules
modules = [
    "datetime",
    "statistics",
    "csv",
    "networkx",
    "matplotlib",
    "numpy",
    "scipy",
    "sys",
    "getopt",
    "plfit",
    "time",
    "pylab",
    "math"
]

not_found = []

for i in modules:
    spam_spec = util.find_spec(i)
    found = spam_spec is not None

    if not found:
        not_found.append(i)

print("Looking for required modules...")

if len(not_found) > 0:
    print("[WARNING] Project requires the following modules:", ", ".join(modules))
    print("Your system is missing", len(not_found), "modules:", ", ".join(not_found))
    print("Install missing modules before proceeding")

    sys.exit()
else:
    print("All required modules found")

print("\nSuccesfully gathered all necessary data, ending gracefully...")

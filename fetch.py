import os
import subprocess
import urllib.request
import zipfile

# Define the target build directory
BUILD_DIR = "esp32_sdcard_build"
os.makedirs(BUILD_DIR, exist_ok=True)

# 1. Direct File Downloads (Minified JS libraries)
DIRECT_DOWNLOADS = {
    "Three.js": ("https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js", "three.min.js"),
    "Pixi.js": ("https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.2.4/pixi.min.js", "pixi.min.js"),
}

# 2. Git Repositories to Clone
GIT_REPOS = [
    ("https://github.com/pkalogiros/AudioMass.git", "audiomass", "-b production"),
    ("https://github.com/piskelapp/piskel.git", "piskel", ""),
    ("https://github.com/HeyPuter/blender-wasm.git", "blender-wasm", ""),
    ("https://github.com/taniarascia/chip8.git", "chip8", ""),
    ("https://github.com/cotestatnt/async-esp-fs-webserver.git", "async-esp-fs-webserver", ""),
    ("https://github.com/Orama-Interactive/Pixelorama.git", "pixelorama", "")
]

# 3. Release Archives (Godot Web, ZzFX)
ARCHIVES = {
    "Godot_Web": "https://github.com/godotengine/godot/releases/download/4.2.1-stable/Godot_v4.2.1-stable_web_editor.zip",
    "ZzFX": "https://github.com/KilledByAPixel/ZzFX/archive/refs/heads/master.zip"
}

def download_file(url, dest_folder, filename):
    print(f"Downloading {filename}...")
    dest_path = os.path.join(dest_folder, filename)
    try:
        urllib.request.urlretrieve(url, dest_path)
    except Exception as e:
        print(f"Failed to download {filename}: {e}")

def clone_repo(repo_url, dest_name, branch_flag):
    dest_path = os.path.join(BUILD_DIR, dest_name)
    if not os.path.exists(dest_path):
        print(f"Cloning {dest_name}...")
        cmd = f"git clone {branch_flag} {repo_url} {dest_path}"
        subprocess.run(cmd, shell=True)
    else:
        print(f"Repository {dest_name} already exists. Skipping.")

def fetch_and_extract(url, name):
    print(f"Fetching archive for {name}...")
    zip_path = os.path.join(BUILD_DIR, f"{name}.zip")
    extract_path = os.path.join(BUILD_DIR, name)
    try:
        urllib.request.urlretrieve(url, zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        os.remove(zip_path)
    except Exception as e:
        print(f"Failed to fetch or extract {name}: {e}")

print("Initializing local dev suite asset acquisition...")

# Execute Downloads
for name, (url, filename) in DIRECT_DOWNLOADS.items():
    download_file(url, BUILD_DIR, filename)

# Execute Git Clones
for repo, name, flag in GIT_REPOS:
    clone_repo(repo, name, flag)

# Execute Archive Fetching
for name, url in ARCHIVES.items():
    fetch_and_extract(url, name)

print(f"\nAcquisition complete. Assets compiled in ./{BUILD_DIR}/")
print("Note: Run necessary build commands (e.g., 'npm run build') inside complex repos like Piskel before moving strictly the output files to your ESP32-C3 external storage.")

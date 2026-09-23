import os
import subprocess
import urllib.request
import zipfile

BUILD_DIR = "esp32_sdcard_build"
os.makedirs(BUILD_DIR, exist_ok=True)

# Additional Missing Repositories and Archives
MISSING_REPOS = [
    ("https://github.com/KeithClark/ZzFXM.git", "zzfxm", ""),
    ("https://github.com/guillaumechereau/goxel.git", "goxel", ""),
    ("https://github.com/etro-js/etro.git", "etro", ""),
    ("https://github.com/strudel-repl/strudel.git", "strudel", "")
]

# Additional Direct URLs / CodeMirror modes
# CodeMirror legacy modes can be cloned or sub-moduled from their archive
CODE_MIRROR_URL = "https://code.haverbeke.berlin/codemirror/legacy-modes/-/archive/master/legacy-modes-master.zip"

def clone_repo(repo_url, dest_name, branch_flag):
    dest_path = os.path.join(BUILD_DIR, dest_name)
    if not os.path.exists(dest_path):
        print(f"Cloning missing repo {dest_name}...")
        cmd = f"git clone {branch_flag} {repo_url} {dest_path}"
        subprocess.run(cmd, shell=True)
    else:
        print(f"Repo {dest_name} already exists.")

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
        print(f"Failed to fetch {name}: {e}")

print("Fetching remaining missing development suite assets...")

for repo, name, flag in MISSING_REPOS:
    clone_repo(repo, name, flag)

fetch_and_extract(CODE_MIRROR_URL, "codemirror_legacy_modes")

print(f"\nAll missing components acquired in ./{BUILD_DIR}/")

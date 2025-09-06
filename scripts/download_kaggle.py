"""
Helper to download the Kaggle dataset (run in Colab after uploading kaggle.json).
Usage (Colab):
  !python3 scripts/download_kaggle.py
"""
import os
import zipfile
import subprocess

DATASET = "capple7/yelp-open-data-philly-restaurants"
OUT = "/content/yelp_philly"

def run():
    os.makedirs(OUT, exist_ok=True)
    # download using kaggle CLI
    subprocess.check_call(["kaggle","datasets","download","-d",DATASET,"-p","/content/","--force"])
    zip_path = "/content/yelp-open-data-philly-restaurants.zip"
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path,"r") as z:
            z.extractall(OUT)
        print("Extracted to", OUT)
    else:
        print("Zip not found; ensure kaggle.json is configured")

if __name__ == "__main__":
    run()

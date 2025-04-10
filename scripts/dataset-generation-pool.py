import multiprocessing as mp
import os.path as osp
import subprocess
from glob import glob

from tqdm import tqdm

# Sesuaikan dengan path direktori input di Windows
input_dir = "../mit-bih/*.atr"
ecg_data = sorted([osp.splitext(i)[0] for i in glob(input_dir)])
pbar = tqdm(total=len(ecg_data))


def run(file):
    # Pada Windows, gunakan 'python' saja, bukan 'python3'
    params = ["python", "dataset-generation.py", "--file", file]
    subprocess.check_call(params)
    pbar.update(1)


if __name__ == "__main__":
    # Gunakan 'mp.cpu_count()' untuk menghitung jumlah CPU
    p = mp.Pool(processes=mp.cpu_count())
    p.map(run, ecg_data)

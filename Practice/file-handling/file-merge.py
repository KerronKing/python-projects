from datetime import datetime
import glob

files = glob.glob('*.txt')

with open(datetime.now().strftime("%Y-%m-%d" + ".txt"), 'w') as filename:
    for file in files:
        with open(file, 'r') as f:
            filename.write(f.read() + '\n')

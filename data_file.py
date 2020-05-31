import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dataset')

args = parser.parse_args()

dataset = args.dataset

for subset in os.listdir(f"../darknet_datasets/labels/{dataset}"):
    text_file = f"data/{subset}.txt"
    if os.path.exists(text_file): os.remove(text_file)
    for image in os.listdir(f"../darknet_datasets/images/{dataset}/{subset}"):
        with open(text_file, 'a') as file:
            file.write(f"../darknet_datasets/images/{dataset}/{subset}/{image}\n")
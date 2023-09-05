import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="dir mode")
args = parser.parse_args()

directories = [] 
image_c = 1
for root, dirs, files in os.walk(args.directory):
    # print("----", "root---\t", root,  "\n")
    # print("new path", "_".join(root.split("/")[1:]))
    prefix = os.path.basename(root)
    for f in files:
        new_file_name = f'{"_".join(root.split("/")[1:])}_{image_c}.png'
        os.rename(os.path.join(root, f), os.path.join(root, new_file_name))
        image_c +=1
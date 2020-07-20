import os
import sys

photo_dir = "/Users/sarahjade/Projects/juliegoz-site/docs/assets/images/production_photos"
relpath_to_photo_dir = "assets/images/production_photos"

file_object = open("production_photos_filenames.txt", "w")
photos_list = os.listdir(photo_dir)

for photo in photos_list:
    if "DS_Store" in photo:
        photos_list.remove(photo)

for index, photo in enumerate(photos_list):
    proj_rel_path = os.path.join(relpath_to_photo_dir, photo)
    file_object.write("  - url: " + proj_rel_path + "\n")
    file_object.write("    image_path: " + proj_rel_path + "\n")
    file_object.write("    alt: Production image" + str(index + 1) + "\n")
    file_object.write("    title: Production image" + str(index + 1) + "\n")

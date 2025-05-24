for img in *.png *.bmp *.gif *.tiff; do
  # Check if file exists (in case no files match pattern)
  [ -e "$img" ] || continue
  filename="${img%.*}"
  magick "$img" "$filename.jpg"

  echo "Converted $img to $filename.jpg"
done

# mkdir images
# cd images
# sudo apt update
# sudo apt install imagemagick
# wget https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/1200px-Instagram_icon.png
# nano pngtojpg.sh
# chmod +x pngtojpg.sh
# ./pngtojpg.sh
# ls



#!/bin/bash
# if ! command -v convert &> /dev/null; then
#   echo "Error: ImageMagick is not installed."
#   exit 1
# fi

# for file in *.{png,gif,bmp,tiff}; do
#   [ -f "$file" ] || continue
#   filename="${file%.*}"
#   convert "$file" "$filename.jpg"
#   echo "Converted $file to ${filename}.jpg"
# done

# echo "Conversion completed."

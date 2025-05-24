#!/bin/bash
if ! command -v convert &> /dev/null; then
  echo "Error: ImageMagick is not installed."
  exit 1
fi

for file in *.{png,gif,bmp,tiff}; do
  [ -f "$file" ] || continue
  filename="${file%.*}"
  convert "$file" "$filename.jpg"
  echo "Converted $file to ${filename}.jpg"
done

echo "Conversion completed."

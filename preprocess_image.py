import sys
from PIL import Image, ImageFilter, ImageOps
import subprocess

def main():

    if len(sys.argv) != 3:
        sys.exit("usage: python preprocess_image.py threshold filename")


    thresh = int(sys.argv[1])
    filename = sys.argv[2]


    image_filter = ImageFilter.Kernel(
        size=(3, 3),
        kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
        scale=1
    )

    img = Image.open(filename).convert("RGB")
    filtered = img.filter(image_filter)

    # filtered = ImageOps.grayscale(filtered)
    
    fn = lambda x : 0 if x > thresh else 255
    filtered = filtered.convert('L').point(fn, mode='1')
    # filtered.show()

    output_filename = filename.split('.')[0] + "_filtered.bmp"
    svg_filename = filename.split('.')[0] + "_filtered.svg"

    filtered.save(output_filename, "BMP")
    subprocess.call(["potrace", output_filename, "-b", "svg"])

    subprocess.call(["java", "-jar", "svgeq-release.jar", svg_filename, "--transform=scale(1, -1)"])
if __name__ == "__main__":
    main()


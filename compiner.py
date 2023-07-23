from PIL.Image import new, Image, open as open_image
from os import listdir
from generator import SIZE

freq_folder = "./freq/"
freq_files = listdir(freq_folder)
freq_images = {file[:-4]: open_image(freq_folder + file) for file in freq_files}


def new_freq_mask(freq_image, intensity=255):
    img = new("L", size=SIZE)
    img.paste(freq_image, mask=intensity)
    return img


def new_img(color=(0, 0, 0)):
    return new("RGB", size=SIZE, color=color)


def add_freq(img, freq_mask, color):
    img.paste(new("RGB", img.size, color), mask=freq_mask)


def main():
    image = new_img((255, 255, 255))
    add_freq()
    image.show()


if __name__ == '__main__':
    main()

from PIL.Image import new
from math import cos, pi

SIZE = (64, 64)


# def generate(fx, fy, size=(64, 64)):
#     width, height = size
#     p_img = new("L", size)
#     p_name = f"./freq/{fx}x{fy}.png"
#     p_data = p_img.load()
#     fx, fy = fx * pi / 64, fy * pi / 64
#     for x in range(width):
#         for y in range(height):
#             p_data[x, y] = int(255 * (1 + (cos(fx * x) * cos(fy * y))) / 2)
#     p_img.save(p_name)
#     return p_img
# from PIL.ImageOps import flip, mirror
# def generate_flip(fx, fy, size=(64, 64)):
#     img = generate(fx, fy, size)
#     if fx % 2:
#         mirror(img).save(f"./freq/-{fx}x{fy}.png")
#     elif fy % 2:
#         flip(img).save(f"./freq/-{fx}x{fy}.png")


def generate_pn(fx, fy, size=SIZE):
    width, height = size
    p_name = f"./freq/{fx}x{fy}.png"
    n_name = f"./freq/-{fx}x{fy}.png"
    p_img = new("L", size)
    n_img = new("L", size)
    p_data = p_img.load()
    n_data = n_img.load()
    fx, fy = fx * pi / 32, fy * pi / 32
    for x in range(width):
        for y in range(height):
            p_data[x, y] = int(255 * (1 + (cos(fx * x) * cos(fy * y))) / 2)
            n_data[x, y] = int(255 * (1 - (cos(fx * x) * cos(fy * y))) / 2)
    p_img.save(p_name)
    n_img.save(n_name)
    return p_img, n_img


def generate_all(size=SIZE):
    images = []
    for x in range(9):
        for y in range(9):
            images.append(generate_pn(x, y, size))


def main():
    generate_all()


if __name__ == '__main__':
    main()

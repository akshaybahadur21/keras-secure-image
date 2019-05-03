from PIL import Image
import math
import os


def perform_encryption():
    pass


def encrypt(src_dir, dest_dir, image_x, image_y, password):
    hash_val = hash(password) % 101
    if hash_val < 30:
        hash_val = hash_val * 2
    BLKSZ = hash_val

    for filename in os.listdir(os.path.join(src_dir)):
        if not filename.endswith('.jpg'):
            for file in os.listdir(os.path.join(src_dir, filename)):
                if file.endswith('.jpg'):
                    full_path = os.path.join(src_dir, filename, file)
                    if not os.path.exists(os.path.join(dest_dir, filename)):
                        os.mkdir(os.path.join(dest_dir, filename))
                    im = Image.open(full_path, "r")
                    im_resized = im.resize((image_x, image_y), Image.ANTIALIAS)
                    arr = im_resized.load()  # pixel data stored in this 2D array
                    for i in range(2, BLKSZ + 1):
                        for j in range(int(math.floor(float(image_x) / float(i)))):
                            for k in range(int(math.floor(float(image_y) / float(i)))):
                                rot(arr, i, j * i, k * i)
                    for i in range(3, BLKSZ + 1):
                        for j in range(int(math.floor(float(image_x) / float(BLKSZ + 2 - i)))):
                            for k in range(int(math.floor(float(image_y) / float(BLKSZ + 2 - i)))):
                                rot(arr, BLKSZ + 2 - i, j * (BLKSZ + 2 - i), k * (BLKSZ + 2 - i))
            im_resized.save("ST1OUT " + str(BLKSZ) + ".png", path=os.path.join(dest_dir, filename,file))
        else:
            full_path = os.path.join(src_dir, filename)
            im = Image.open(full_path, "r")
            im_resized = im.resize((image_x, image_y), Image.ANTIALIAS)
            arr = im_resized.load()  # pixel data stored in this 2D array
            for i in range(2, BLKSZ + 1):
                for j in range(int(math.floor(float(image_x) / float(i)))):
                    for k in range(int(math.floor(float(image_y) / float(i)))):
                        rot(arr, i, j * i, k * i)
            for i in range(3, BLKSZ + 1):
                for j in range(int(math.floor(float(image_x) / float(BLKSZ + 2 - i)))):
                    for k in range(int(math.floor(float(image_y) / float(BLKSZ + 2 - i)))):
                        rot(arr, BLKSZ + 2 - i, j * (BLKSZ + 2 - i), k * (BLKSZ + 2 - i))
            im_resized.save(os.path.join(dest_dir, filename))


def rot(A, n, x1, y1):  # this is the function which rotates a given block
    temple = []
    for i in range(n):
        temple.append([])
        for j in range(n):
            temple[i].append(A[x1 + i, y1 + j])
    for i in range(n):
        for j in range(n):
            A[x1 + i, y1 + j] = temple[n - 1 - i][n - 1 - j]

# xres = 200
# yres = 200
# name = "Akshay"
# hash_val = hash(name) % 101
# if hash_val < 30:
#     hash_val = hash_val * 2
# BLKSZ = hash_val
#
# im = Image.open("F:\\projects\\SIT_Sample\\AutoPilot\\driving_dataset\\500.jpg", "r")
# im_resized = im.resize((xres, yres), Image.ANTIALIAS)
# arr = im_resized.load()  # pixel data stored in this 2D array
#
#
# def rot(A, n, x1, y1):  # this is the function which rotates a given block
#     temple = []
#     for i in range(n):
#         temple.append([])
#         for j in range(n):
#             temple[i].append(arr[x1 + i, y1 + j])
#     for i in range(n):
#         for j in range(n):
#             arr[x1 + i, y1 + j] = temple[n - 1 - i][n - 1 - j]
#
#
# for i in range(2, BLKSZ + 1):
#     for j in range(int(math.floor(float(xres) / float(i)))):
#         for k in range(int(math.floor(float(yres) / float(i)))):
#             rot(arr, i, j * i, k * i)
# for i in range(3, BLKSZ + 1):
#     for j in range(int(math.floor(float(xres) / float(BLKSZ + 2 - i)))):
#         for k in range(int(math.floor(float(yres) / float(BLKSZ + 2 - i)))):
#             rot(arr, BLKSZ + 2 - i, j * (BLKSZ + 2 - i), k * (BLKSZ + 2 - i))
#
# im_resized.save("ST1OUT " + str(BLKSZ) + ".png")
# print("Done!")

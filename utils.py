import cv2
from matplotlib import pyplot as plt
import uuid
from math import ceil


def show_img(img: cv2.Mat, title = ""):
    plt.figure(f"{title} {uuid.uuid4()}", figsize=(8, 8))
    plt.title(title, fontdict={'color': 'red', 'fontweight': 'bold'})
    plt.xticks ([])
    plt.yticks ([])
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def show_img_grid(img_data: dict, ncols=3, title = ""):
    fig, axs = plt.subplots(2 if ncols == 1 else ceil(len(img_data) / ncols), ncols, figsize=(18, 13))
    axs = axs.flatten()
    for img, ax in zip(img_data.items(), axs):
        ax.set_title(img[0], fontdict={'color': 'red', 'fontweight': 'bold'})
        ax.imshow(cv2.cvtColor(img[1], cv2.COLOR_BGR2RGB))
    plt.show()


def show_hist(img: cv2.Mat, title = ""):
    plt.figure(f"{title} {uuid.uuid4()}", figsize=(18, 13))
    plt.title(title, fontdict={'color': '#fff', 'fontweight': 'bold'})
    plt.xlabel("Intensidade", fontdict={'color': 'red', 'fontweight': 'bold'})   # título do eixo x
    plt.xticks(color="#fff", ticks=[i for i in range(0, 261, 10)])
    plt.ylabel("Qtde de Pixels", fontdict={'color': 'red', 'fontweight': 'bold'}) # título do eixo y
    plt.yticks(color="#fff")
    plt.hist(img.ravel(), 256, [0, 256])


def show_hist_grid(hist_data: dict, ncols=3):
    _, axs = plt.subplots(2 if ncols == 1 else len(hist_data) // ncols, ncols, figsize=(18, 6))
    axs = axs.flatten()
    for hist, ax in zip(hist_data.items(), axs):
        ax.set_title(hist[0], fontdict={'color': 'red', 'fontweight': 'bold'})
        ax.hist(hist[1].ravel(), 256, [0, 256])
    plt.show()

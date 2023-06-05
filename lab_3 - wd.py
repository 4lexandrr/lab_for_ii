import numpy as np
import random
from PIL import Image
import os
import re


# Конвертирование матрицы в массив
def mat2vec(x):
    m = x.shape[0] * x.shape[1]
    tmp1 = np.zeros(m)

    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i, j]
            c += 1
    return tmp1


# Создание матрицы весов для изображения
def create_W(x):
    if len(x.shape) != 1:
        print("На вход подан не вектор")
        return
    else:
        w = np.zeros([len(x), len(x)])
        for i in range(len(x)):
            for j in range(i, len(x)):
                if i == j:
                    w[i, j] = 0
                else:
                    w[i, j] = x[i] * x[j]
                    w[j, i] = w[i, j]
    return w


# Конвертирование изображения в массив
def readImg2array(file, size, threshold=145):
    pilIN = Image.open(file).convert(mode="L")
    pilIN = pilIN.resize(size)
    imgArray = np.asarray(pilIN, dtype=np.uint8)
    x = np.zeros(imgArray.shape, dtype=float)
    x[imgArray > threshold] = 1
    x[x == 0] = -1
    return x


# Конвертирование массива в изображение
def array2img(data, outFile=None):
    y = np.zeros(data.shape, dtype=np.uint8)
    y[data == 1] = 255
    y[data == -1] = 0
    img = Image.fromarray(y, mode="L")
    if outFile is not None:
        img.save(outFile)
    return img


def update(w, y_vec, theta=0.5, time=100):
    for s in range(time):
        m = len(y_vec)
        i = random.randint(0, m - 1)
        u = np.dot(w[i][:], y_vec) - theta

        if u > 0:
            y_vec[i] = 1
        elif u < 0:
            y_vec[i] = -1

    return y_vec


def hopfield(train_files, test_files, theta=0.5, time=1000, size=(100, 100), threshold=60, current_path=None):
    # Чтение изображения и перевод в numpy массив
    print("Чтение изображений и создание матрицы весов")
    num_files = 0
    for path in train_files:
        print(path)
        x = readImg2array(file=path, size=size, threshold=threshold)
        x_vec = mat2vec(x)
        print(len(x_vec))
        if num_files == 0:
            w = create_W(x_vec)
            num_files = 1
        else:
            tmp_w = create_W(x_vec)
            w = w + tmp_w
            num_files += 1

    print("Матрица весов создана")

    # Импорт test изображений
    counter = 0
    for path in test_files:
        y = readImg2array(file=path, size=size, threshold=threshold)
        oshape = y.shape
        y_img = array2img(y)
        y_img.show()
        print("Импорт test изображений")

        y_vec = mat2vec(y)
        print("Восстановление изображений")
        y_vec_after = update(w=w, y_vec=y_vec, theta=theta, time=time)
        y_vec_after = y_vec_after.reshape(oshape)
        if current_path is not None:
            outfile = current_path + "/after_" + str(counter) + ".jpeg"
            array2img(y_vec_after, outFile=outfile)
        else:
            after_img = array2img(y_vec_after, outFile=None)
            after_img.show()
        counter += 1


# Theta порог активации нейрона
# threshold порог для отсечения бинаризации изображения (от 0 до 255)

if __name__ == '__main__':
    # Задание train изображений
    current_path = os.getcwd()
    train_paths = []
    path = current_path + "/test/"
    for i in os.listdir(path):
        if re.match(r'[0-9a-zA-Z-]*.jp[e]*g', i):
            train_paths.append(path + i)

    # Задание test изображений
    test_paths = []
    path = current_path + "/test/"
    for i in os.listdir(path):
        if re.match(r'[0-9a-zA-Z-_]*.jp[e]*g', i):
            test_paths.append(path + i)

    # Запуск нейросети
    hopfield(train_files=train_paths, test_files=test_paths, theta=0.5, time=30000, size=(500, 500), threshold=100,
             current_path=current_path)
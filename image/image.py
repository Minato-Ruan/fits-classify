#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/27
#  This software is released under the MIT License.
import os
from abc import ABCMeta, abstractmethod

from astropy.io import fits
import numpy as np
from PIL import Image as PImg
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style


class Image(metaclass=ABCMeta):
    @abstractmethod
    def read(self, path: str):
        """
        Read Image file, return image as a numpy array
        :param path:None, if path is not None, read image from new path.
        :return: numpy array
        """
        pass

    @abstractmethod
    def save(self, path: str):
        """
        Save image.
        :param path: Target Path
        :return: Path
        """
        pass


class XImage(Image):
    def __init__(self, path: str = None):
        self.path = path
        self.data = None

    def read(self, path: str = None):
        if path is not None:
            self.path = path
        info = fits.open(self.path)[1].header
        image_data = fits.open(self.path)[1].data
        x_max, y_max = info["TLMAX2"], info["TLMAX3"]

        event_list = zip(image_data.X, image_data.Y)
        self.data = np.zeros((x_max, y_max), dtype="int16")

        for px, py in event_list:
            self.data[px, py] += 1

        return self.data

    def save(self, path: str):
        # TODO: Fits File Save.
        raise NotImplementedError


class PNG(Image):
    def __init__(self, path=None):
        self.path = path
        self.data = None

    def read(self, path: str = None):
        if path is not None:
            self.path = path
        self.data = np.array(Image.open(self.path))

        return self.data

    def save(self, path: str = None):
        if path is None:
            if self.path is None:
                raise ValueError

            path = self.path

        if path.split(".")[-1] != "png" and path.split(".")[-1] != "PNG":
            path += ".png"

        if self.data.ndim == 3:
            plot = PImg.fromarray(self.data.astype("float") * 255.0 / self.data.max())
            plot = plot.convert("RGB")
        elif self.data.ndim == 2:
            plot = PImg.fromarray(self.data.astype("float") * 255.0 / self.data.max())
            plot = plot.convert("L")
        else:
            raise TypeError

        file_path, _ = os.path.split(path)
        if os.path.exists(file_path):
            os.mkdir(file_path)

        plot.save(path)


class NpyImage(Image):
    def __init__(self, path=None):
        self.path = path
        self.data = None

    def read(self, path: str = None):
        if path is not None:
            self.path = path
        self.data = np.load(self.path)

        return self.data

    def save(self, path: str = None):
        if path is None:
            if self.path is None:
                raise ValueError
            path = self.path

        file_path, _ = os.path.split(path)
        if os.path.exists(file_path) is not True:
            os.mkdir(file_path)

        np.save(path, self.data)


if __name__ == '__main__':
    pass

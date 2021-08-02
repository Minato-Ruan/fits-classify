#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/28
#  This software is released under the MIT License.
from abc import ABCMeta, abstractmethod

import numpy as np

from xrt.image import Image, XImage, NpyImage


class Target(metaclass=ABCMeta):
    @abstractmethod
    def get_min(self):
        """
        Get lower of Bounding Box which you want to cut out.
        :return: x_min, y_min [int]
        """
        pass

    @abstractmethod
    def get_max(self):
        """
        Get upper of Bounding Box which you want to cut out.
        :return: x_max, y_max [int]
        """
        pass


class ImageTarget(Target):
    def __init__(self, *args, **kwargs):
        """
        Information of Part you want to cut out.
        :param args: {"pos":(x,y), "size":(x_size, y_size), "name":name, "path": file path}
        :param kwargs: pos, x, y, size, x_size, y_size, name, path
        """
        if len(args) == 1:
            args = args[0]
            if type(args) is dict:
                try:
                    self.pos = args["pos"]
                    self.size = args["size"]
                    self.name = args["name"]
                    self.path = args["path"]
                except KeyError:
                    raise ValueError
            if isinstance(args, Image):
                # TODO: if Image
                pass
        elif len(args) > 1:
            raise ValueError
        elif len(args) == 0:
            if "pos" in kwargs:
                self.pos = kwargs["pos"]
            if "x" in kwargs:
                self.pos[0] = kwargs["x"]
            if "y" in kwargs:
                self.pos[1] = kwargs["y"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x_size" in kwargs:
                self.size[0] = kwargs["x_size"]
            if "y_size" in kwargs:
                self.size[1] = kwargs["y_size"]
            if "name" in kwargs:
                self.name = kwargs["name"]
            if "path" in kwargs:
                self.path = kwargs["path"]

    def get_min(self):
        return int(self.pos[0] - (self.size[0] / 2)), int(self.pos[1] - (self.size[1] / 2))

    def get_max(self):
        return int(self.pos[0] + (self.size[0] / 2)), int(self.pos[1] + (self.size[1] / 2))


class Cutter(metaclass=ABCMeta):
    @abstractmethod
    def cut(self, target: Target):
        """
        Cut Target Object
        :param target: Target Object
        :return: Result Object
        """
        pass


class ImageCutter(Cutter):
    def cut(self, target: ImageTarget):
        """
        Cut XImage Object
        :param target: Image Obj
        :return: Result NpyImage
        """
        target_image = XImage(target.path)
        target_image = target_image.read()

        x_min, y_min = target.get_min()
        x_max, y_max = target.get_max()

        npy_image = NpyImage()
        npy_image.data = target_image[x_min:x_max, y_min:y_max]

        return npy_image


class TargetList:
    def __init__(self):
        self.list = []
        self._index = 0

    def __len__(self):
        return len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.list):
            self._index += 1
            return self.list[self._index - 1]

        raise StopIteration

    def append(self, new_target: Target):
        self.list.append(new_target)


if __name__ == '__main__':
    pass

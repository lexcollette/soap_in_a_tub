import cv2
import dataclasses
import numpy as np


@dataclasses.dataclass
class Droplets:
    """
    Data class to hold droplet information. x, y, speed
    """
    x: int
    y: int
    speed: int


class ShowerHead:
    """
    Simulate a shower head. Generate droplets and update their positions.
    """

    def __init__(self):
        self.num_droplets = 0
        self.total_droplets = 0
        self.droplets = []

    def generate_droplet(self, image, number_of_droplets):
        """
        Generate droplets. Randomly place them at the top of the image. Random speed.
        :param image:
        :param number_of_droplets:
        :return:
        """
        while len(self.droplets) < number_of_droplets:
            self.droplets.append(Droplets(  # x, y, speed
                np.random.randint(0, image.shape[1]),
                np.random.randint(0, image.shape[0]),
                np.random.randint(3, 20)
            ))
        self.total_droplets += number_of_droplets

    def update_droplets(self, image):
        """
        Update droplet positions based on speed. Remove droplets that have fallen off the image.
        :param image:
        :return:
        """
        updated_droplets = []
        for droplet in self.droplets:
            y = droplet.y + droplet.speed
            if y < image.shape[1]:
                updated_droplets.append(Droplets(droplet.x, y, droplet.speed))
        self.droplets.clear()
        self.droplets = updated_droplets.copy()

    def draw_droplets(self, image, droplets):
        """
        Draw droplets on the image.
        :param image:
        :param droplets:
        :return:
        """
        [cv2.circle(image, (droplet.x, droplet.y), 2, 150, -1) for droplet in droplets]


    def remove_droplets(self, droplets):
        """
        Remove droplets that have impacted the soap. They will be removed from the list of droplets.
        :param droplets:
        :return:
        """

        self.droplets = [droplet for droplet in self.droplets if droplet not in droplets]
        self.num_droplets -= len(droplets)
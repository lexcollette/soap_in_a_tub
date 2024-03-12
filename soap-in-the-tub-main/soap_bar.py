import numpy as np
import cv2


class SoapBar:
    """
    Simulate a bar of soap. The soap is represented by a 2D array of pixel values, created from an image file.
    """
    def __init__(self, soap_filename="assets/bar_of_soap.png"):
        """
        :param soap_filename:
        """
        self.soap = self._load_soap(soap_filename)
        self.soap = cv2.resize(self.soap, (300, 300))
        self.initial_size = self.size()
        self.soap_threshold = 255

    def _load_soap(self, soap_filename):
        """
        Load the soap image file and convert it to a 2D array of pixel values.
        :param soap_filename:
        :return:
        """
        soap = cv2.imread(soap_filename, cv2.IMREAD_GRAYSCALE)
        return soap

    def size(self):
        """
        Return the number of zero pixels in the soap array. The location of the soap is represented by zero.
        :return:
        """
        return (self.soap.shape[0] * self.soap.shape[1]) - np.count_nonzero(self.soap)

    def percentage_remaining(self):
        """
        Return the percentage of soap remaining. The initial size of the soap is used to calculate the percentage.
        :return:
        """
        return int((self.size() / self.initial_size) * 100)

    def erode(self, droplets):
        """
        Erode the soap based on the impact of droplets. The soap is eroded based on the speed of the droplet.
        :param droplets:
        :return:
        """
        droplet_impact = []
        for droplet in droplets:
            x = droplet.x
            y = droplet.y
            speed = droplet.speed
            if self.soap[y, x] < self.soap_threshold:
                while self.soap[y-1, x] < self.soap_threshold:
                    x -= 1
                erode = self.soap[y, x] + (speed * 10)
                if erode > 255:
                    erode = 255
                self.soap[y, x] = erode
                droplet_impact.append(droplet)
        return droplet_impact


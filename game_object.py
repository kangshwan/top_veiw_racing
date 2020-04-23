from abc import ABCMeta, abstractmethod
import point_n_rect as pnr

class Gameobject(metaclass=ABCMeta):
    def __init__(self, *args):
        # args should add in (x,y) tuple
        self.position = pnr.Point(args[0],args[1])
    
    @abstractmethod
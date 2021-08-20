#!/usr/bin/python
import lxml.etree as ET
from constants import *
from elemBuilder import elemBuilder

class OnceOnlyController(elemBuilder):
    def __init__(self, name='Once Only Controller'):
        super().__init__(ONCE_ONLY_CONTROLLER, name)

class RandomController(elemBuilder):
    def __init__(self, name='Random Controller'):
        super().__init__(RANDOM_CONTROLLER, name)
    
    def configRC_ignoreSubcontrollerBlocks(self,Ignore=False):
        flag = 1
        if Ignore == True:
            flag = 0
        self.Element.find('.//intProp[@name="InterleaveControl.style"]').text = flag
        return
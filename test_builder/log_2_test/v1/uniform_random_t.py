#!/usr/bin/env python

from elemBuilder import elemBuilder
import lxml.etree as ET
from constants import *


class UniformRandom(elemBuilder):
    def __init__(self, name='think time'):
        super().__init__(UNIFORM_RANDOM_TIMER, name)

    def set_offset(self, delay):
        elem = self.Element.find('.//stringProp[@name="ConstantTimer.delay"]')
        elem.text = delay

    def set_range(self, range):
        elem = self.Element.find('.//stringProp[@name="RandomTimer.range"]')
        elem.text = range

test = UniformRandom()
test.set_offset('1000')
test.print()
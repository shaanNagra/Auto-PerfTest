#!/usr/bin/env python

from test_builder.log_2_test.elemBuilder import elemBuilder
import lxml.etree as ET
from constants import *
import functions as funcs


class testFragmentBuilder(elemBuilder):

    def __init__(self, name):
        super().__init__(TEST_FRAGMENT, name)

    def configTestFragment(self, comments):
        pass

#!/usr/bin/env python

from elemBuilder import elemBuilder
import lxml.etree as ET
from constants import *
import functions as funcs
import random


class simpleBuilder(elemBuilder):
    def __init__(self, name='simple controller'):
        super().__init__(SIMPLE_CONTROLLER, name)

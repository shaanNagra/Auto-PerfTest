#!/usr/bin/env python

from elemBuilder import elemBuilder
import lxml.etree as ET
from constants import *
import functions as funcs
import random


class WSCBuilder(elemBuilder):
    def __init__(self, name='wsc'):
        # self.cases = list(dict())
        super().__init__(BZM_WEIGHTED_SWITCH_CONTROLLER, name)

    def addCase(self, caseName, weight):
        collProp = ET.Element('collectionProp', name=caseName+'Props')
        nameProp = ET.Element('stringProp', name=caseName+"Name")
        nameProp.text = caseName
        weightProp = ET.Element('stringProp', name=caseName+'Weight')
        weightProp.text = weight
        enableProp = ET.Element('stringProp', name=caseName+'Enabled')
        enableProp.text = self.Bool2Bool(True)
        collProp.append(nameProp)
        collProp.append(weightProp)
        collProp.append(enableProp)
        self.Element.find('.//collectionProp[@name="Weights"]').append(collProp)
        pass

    def toString(self):
        return ET.tostring(self.Element)
    # def changeCaseWeight(self, caseName, weight):
        # pass

test = WSCBuilder('poobum')
test.addCase('poo', '80')
test.addCase('bum', '20')
test.print()

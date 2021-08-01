#!/usr/bin/python
# import xml.etree.ElementTree as ET
import lxml.etree as ET
from constants import *
import functions as funcs
import threadGroupBuilder


class jmeterTestPlanBuilder:
    def __init__(self,version,properties,jmeter):
        self.__header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"

        self.Element = ET.Element('jmeterTestPlan')
        self.Element.set('version',version)
        self.Element.set('properties',properties)
        self.Element.set('jmeter',jmeter)
        self.hashTree = ET.fromstring(HASH_TREE)
        self.Element.append(self.hashTree)  

    def append(self,elem):
        self.hashTree.extend(elem)
        return

    def print(self):
        print(ET.tostring(self.Element))
        return
    
    def toString(self):
        return ET.tostring(self.Element)

    def enable(self,enable=True):
        self.Element.set('enabled',self.Bool2Bool(enable))
        return


    def Bool2Bool(self,bool):
        if bool == False:
            return "false"
        elif bool == True:
            return "true"
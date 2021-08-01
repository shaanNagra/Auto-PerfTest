from constants import *
import lxml.etree as ET

class elemBuilder:
    def __init__(self,element,name):
        self.Element = ET.fromstring(element)
        self.Element.set('testname',name)
        self.TempRoot = ET.Element('temproot')
        self.TempRoot.append(self.Element)
        self.Element.addnext(ET.fromstring(HASH_TREE))
        pass

    def append(self,elem):
        self.Element.getnext().extend(elem)
        return

    def getElem(self):
        return self.TempRoot.getchildren()

    def print(self):
        print(ET.tostring(self.Element))
        print(ET.tostring(self.Element.getnext()))
        return

    def enable(self,enable=True):
        self.Element.set('enabled',self.Bool2Bool(enable))
        return


    def Bool2Bool(self,bool):
        if bool == False:
            return "false"
        elif bool == True:
            return "true"
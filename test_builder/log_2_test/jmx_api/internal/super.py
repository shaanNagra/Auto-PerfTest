#!/usr/bin/python

import lxml.etree as ET

from .constants import HASH_TREE


class BaseElem:
    def __init__(self, element, name):
        self.Element = ET.fromstring(element)
        self.Element.set('testname', name)
        self.TempRoot = ET.Element('temproot')
        self.TempRoot.append(self.Element)
        self.Element.addnext(ET.fromstring(HASH_TREE))
        pass

    def append(self, elem):
        self.Element.getnext().extend(elem)
        return

    def get_elem(self):
        return self.TempRoot.getchildren()

    def print(self):
        print(ET.tostring(self.Element))
        print(ET.tostring(self.Element.getnext()))
        return

    def enable(self, enable=True):
        self.Element.set('enabled', self.Bool2Bool(enable))
        return

    def bool_2_bool(self, bool):
        if bool is False:
            return "false"
        elif bool is True:
            return "true"

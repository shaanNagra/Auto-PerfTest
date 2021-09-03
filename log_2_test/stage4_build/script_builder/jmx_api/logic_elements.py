#!/usr/bin/env python

# EXTERNAL IMPORTS
import lxml.etree as ET

# INTERNAL IMPORTS
from jmx_api.internal.base_element import BaseElem
from jmx_api.internal.constants import (BZM_WEIGHTED_SWITCH_CONTROLLER,
                                        SIMPLE_CONTROLLER,
                                        RANDOM_CONTROLLER,
                                        ONCE_ONLY_CONTROLLER,
                                        MODULE_CONTROLLER)

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////



# ------------------------------------------
#
# ------------------------------------------
class WeightedSwitchController(BaseElem):
    def __init__(self, name='wsc'):
        # self.cases = list(dict())
        super().__init__(BZM_WEIGHTED_SWITCH_CONTROLLER, name)

    def addCase(self, caseName, weight):
        collProp = ET.Element('collectionProp', name=caseName+'Props')

        nameProp = ET.Element('stringProp', name=caseName+"Name")
        nameProp.text = caseName

        weightProp = ET.Element('stringProp', name=caseName+'Weight')
        weightProp.text = str(weight)

        enableProp = ET.Element('stringProp', name=caseName+'Enabled')
        enableProp.text = self.bool_2_bool(True)

        collProp.append(nameProp)
        collProp.append(weightProp)
        collProp.append(enableProp)

        self.Element.find(
            './/collectionProp[@name="Weights"]'
            ).append(collProp)


# ------------------------------------------
#
# ------------------------------------------
class SimpleController(BaseElem):
    def __init__(self, name='simple controller'):
        super().__init__(SIMPLE_CONTROLLER, name)


# ------------------------------------------
#
# ------------------------------------------
class RandomController(BaseElem):
    def __init__(self, name='Random Controller'):
        super().__init__(RANDOM_CONTROLLER, name)

    def configRC_ignoreSubcontrollerBlocks(self, Ignore=False):

        flag = 1

        if Ignore is True:
            flag = 0

        self.Element.find(
            './/intProp[@name="InterleaveControl.style"]'
            ).text = flag

        return


# ------------------------------------------
#
# ------------------------------------------
class OnceOnlyController(BaseElem):
    def __init__(self, name='Once Only Controller'):
        super().__init__(ONCE_ONLY_CONTROLLER, name)


# ------------------------------------------
#
# ------------------------------------------
class ModuleController(BaseElem):
    def __init__(self, name='Module Controller'):
        super().__init__(MODULE_CONTROLLER, name)

    def add_path(self, path):
        path_elem = self.Element.find(
            './/collectionProp[@name="ModuleController.node_path"]'
            )
        old_path = path_elem.getchildren()
        if old_path is None:
            for item in old_path:
                path_elem.remove(item)

        for item in path:
            newElem = ET.Element('stringProp', name=item+"PathProp")
            newElem.text = item
            path_elem.append(newElem)


# test = ModuleController()
# test.add_path(['the','path','lol'])
# test.print()

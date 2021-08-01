#!/usr/bin/python
# import xml.etree.ElementTree as ET
import lxml.etree as ET
import constants
import functions as funcs
import threadGroupBuilder


class testPlanBuilder:
    def __init__(self,name,version,properties,jmeter):
        self._header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"

        self.__Element = ET.Element('jmeterTestPlan')
        self.__Element.set('version',version)
        self.__Element.set('properties',properties)
        self.__Element.set('jmeter',jmeter)
        self.__testPlanElement = ''
        self.initTestPlan(name)
        hashTree = ET.Element('hashTree')
        hashTree.append(self.__testPlanElement)
        self.__Element.append(hashTree)        
        
    
    def initTestPlan(self,name='Test Plan'):
        self.__testPlanElement = ET.fromstring(constants.testPlan)
        self.__testPlanElement.set('testname',name)
        self.__testPlanElement.addnext(ET.fromstring(constants.hashTree))
        return

    def configTestPlan(self,comments,func_mode=False,tearDown_on_SD=False,s_tg=False):
        self.__testPlanElement.find('.//stringProp[@name="TestPlan.comments"]').text = comments
        self.__testPlanElement.find('.//boolProp[@name="TestPlan.functional_mode"]').text = funcs.Bool2Bool(func_mode)
        self.__testPlanElement.find('.//boolProp[@name="TestPlan.tearDown_on_shutdown"]').text = funcs.Bool2Bool(tearDown_on_SD)
        self.__testPlanElement.find('.//boolProp[@name="TestPlan.serialize_threadgroups"]').text = funcs.Bool2Bool(s_tg)
        return

# def initThreadGroup(self,name='Thread Group'):
    #     self._threadGroup = ET.fromstring(constants.threadGroup)
    #     self._threadGroup.set('testname',name)

    #     return

    # def configTG_loopCount(self,count,infinite=False):
        
    #     if infinite == False:
    #         newElem = ET.Element('stringProp',name='LoopController.loops')
    #         newElem.text = str(count)
    #     else:
    #         newElem = ET.Element('intProp',name='LoopController.loops')
    #         newElem.text = str(-1)

    #     if None == self._threadGroup.find('.//intProp[@name="LoopController.loops"]'):
    #         elem = self._threadGroup.find('.//stringProp[@name="LoopController.loops"]')

    #     else:
    #         elem = self._threadGroup.find('.//intProp[@name="LoopController.loops"]')

    #     elem.addnext(newElem)
    #     parent = elem.getparent()
    #     parent.remove(elem)
    #     print(ET.tostring(self._threadGroup))

    #     return

    # def configTG_onSampleError():
    #     return 

    # def configTG_specifyLifetime(self,toggle=False,Duration="",StartupDelay=""):
    #     schedElem = self._threadGroup.find('.//boolProp[@name="ThreadGroup.scheduler"]')
    #     duratElem = schedElem.getnext()
    #     delayElem = duratElem.getnext()
    #     if toggle == False:
    #         schedElem.text = Bool2Bool(toggle)
    #         duratElem.text = ''
    #         delayElem.text = ''
    #     else:
    #         schedElem.text = Bool2Bool(toggle)
    #         duratElem.text = str(Duration)
    #         delayElem.text = str(StartupDelay)

    # def configTG_other(self,sameUserOnIter=False,numThreads=1,rampTime=1):
    #     numThreadsElem = self._threadGroup.find('.//stringProp[@name="ThreadGroup.num_threads"]')
    #     rampTimeElem = numThreadsElem.getnext()
    #     sameUserElem = self._threadGroup.find('.//boolProp[@name="ThreadGroup.same_user_on_next_iteration"]')
    #     numThreadsElem.text = str(numThreads)
    #     rampTimeElem.text = str(rampTime)
    #     sameUserElem.text = Bool2Bool(sameUserOnIter)
    #     return



# cb = componentBuilder("testplanisname","1.2","5.0","5.4.1")
# cb.configTestPlan("dfs",True)

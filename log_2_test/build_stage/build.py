from sys import implementation
from log_2_test.build_stage.jmx_api.internal.constants import THREAD_GROUP
import markov_chain
from state import State
import jmx_api as jmx
from component_state import create_end_node,create_node,create_root

group = [
    ['8 1', '8 2', '9 1', '5 1'],
    ['8 1', '8 2', '9 1', '5 1', '3 1'],
    ['2 1', '1 1']
    ]
sss = []
sss.append([8, 8, 9, 5, 3, 2, 1])
sss.append([8, 8, 9, 5, 3, 2, 1, 8, 9, 8, 5, 2, 1])
# print(sss)

state_dict = markov_chain.testBuild(group, sss)
testplanname = 'testplannae'
jmeterScript = jmx.jmeter_test_script.jmeterTestPlanBuilder()
testplan = jmx.test_plan_element.testPlanBuilder(testplanname)

root_state = state_dict[1]
state_dict.pop(1)

end_node_state = state_dict[0]
state_dict.pop(0)


for sIndex in state_dict:
    testplan.append(create_node(sIndex, state_dict[sIndex]))

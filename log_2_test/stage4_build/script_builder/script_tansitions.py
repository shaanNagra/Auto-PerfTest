#!/usr/bin/env python

import jmx_api as jmx
import naming_function as naming_func


# ------------------------------------------
#
# ------------------------------------------
def create_transitions(next_states, test_plan_name):

    wsc = jmx.logic_elements.WeightedSwitchController()

    for ns in next_states:
        case_name = naming_func.getCaseName(ns)
        state_name = naming_func.getStateName(ns)

        wsc.addCase(case_name, next_states[ns]["prob"])
        wsc.append(
            __create_case(
                case_name,
                next_states[ns]["offset"],
                next_states[ns]["range"],
                ['Test Plan', test_plan_name, state_name]
                )
            )
    return wsc


# ------------------------------------------
#
# ------------------------------------------
def create_basic_transitions(next_states, test_plan_name):

    wsc = jmx.logic_elements.WeightedSwitchController()

    for ns in next_states:
        case_name = naming_func.getCaseName(ns)
        state_name = naming_func.getStateName(ns)

        wsc.addCase(case_name, next_states[ns])
        wsc.append(
            __create_basic_case(
                case_name,
                ['Test Plan', test_plan_name, state_name]
                )
            )
    return wsc


# ------------------------------------------
#
# ------------------------------------------
def __create_case(name, tt_offset, tt_range, path):
    simple_ctrl = jmx.logic_elements.SimpleController(name)

    simple_ctrl.append(__create_think_time(tt_offset, tt_range))
    simple_ctrl.append(__create_module(path))
    return simple_ctrl.get_elem()


def __create_basic_case(name, path):
    simple_ctrl = jmx.logic_elements.SimpleController(name)
    simple_ctrl.append(__create_module(path))
    return simple_ctrl.get_elem()


# ------------------------------------------
#
# ------------------------------------------
def __create_think_time(tt_offset, tt_range):

    tt = jmx.think_timer_element.ThinkTime()

    timer = jmx.timer_elements.UniformRandom()
    timer.set_offset(str(tt_offset))
    timer.set_range(str(tt_range))

    tt.append(timer)

    return tt.get_elem()


# ------------------------------------------
#
# ------------------------------------------
def __create_module(path):

    module = jmx.logic_elements.ModuleController()
    module.add_path(path)

    return module.get_elem()

# testinput = {
#         0: {'prob': 5, 'offset': 100, 'range': 50},
#         8: {'prob': 20, 'offset': 1000, 'range': 300},
#         3: {'prob': 17, 'offset': 10, 'range': 100}
#     }
# testwsc = create_switch(testinput, 'this is thename of my test plan')
# testwsc.print()
# test = create_case('go to x', '100', '3485', ['the', 'path', 'to'])
# test.print()
# testinput = {
#         0: {'prob': 5, 'offset': 100, 'range': 50},
#         8: {'prob': 20, 'offset': 1000, 'range': 300},
#         3: {'prob': 17, 'offset': 10, 'range': 100}
#     }

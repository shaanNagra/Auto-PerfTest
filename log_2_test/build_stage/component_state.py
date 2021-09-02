
from state import State
import jmx_api as jmx
import component_branch
import component_sampler


def create_root(state,index):
    thread_group = jmx.thread_group_element.threadGroup()
    wsc = component_branch.create_basic_switch(state.getNextGroup())
    thread_group.append(wsc.get_elem())
    pass


def create_node():
    pass


def create_end_node():
    pass

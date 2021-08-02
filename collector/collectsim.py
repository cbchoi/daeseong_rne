import contexts
from config import *

import sys,os

from evsim.system_simulator import SystemSimulator
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

from clock import Clock
from periodic_image_capture import PIC

# Simulation Configuration
se = SystemSimulator()

se.register_engine("sname", SIMULATION_MODE, TIME_DENSITY)

clock = PIC(0, 10, "clock", "sname")

se.get_engine("sname").insert_input_port("start")
se.get_engine("sname").register_entity(clock)

se.get_engine("sname").coupling_relation(None, "start", clock, "start")

se.get_engine("sname").insert_external_event("start", 'msg')
se.get_engine("sname").simulate()
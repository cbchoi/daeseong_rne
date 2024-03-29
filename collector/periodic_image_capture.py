from evsim.system_simulator import SystemSimulator
from evsim.behavior_model_executor import BehaviorModelExecutor
from evsim.system_message import SysMessage
from evsim.definition import *

import os
import datetime

from config import *

import math
import cv2

class PIC(BehaviorModelExecutor):
    def __init__(self, instance_time, destruct_time, name, engine_name):
        BehaviorModelExecutor.__init__(self, instance_time, destruct_time, name, engine_name)
        self.init_state("IDLE")
        self.insert_state("IDLE", Infinite)
        self.insert_state("WAKE", 1)
  
        self.insert_input_port("start")
        self.insert_input_port("end")
        
        self.sim_time = 0
        self.cap = cv2.VideoCapture(0)
        print("init")

    def ext_trans(self,port, msg):
        if port == "start":
            print("in")
            self._cur_state = "WAKE"
        if port == "end":
            self._cur_state = "IDLE"
                        
    def output(self):
        #print("out")
        if self._cur_state == "WAKE":
            self.sim_time += 1
            print(self.convert_unit_time())

            r, f = self.cap.read()
            cv2.imwrite(f"./{self.sim_time}.png", f)
            #print("out")

    def int_trans(self):
        if self._cur_state == "WAKE":
            self._cur_state = "WAKE"
    
    def convert_unit_time(self):
        return '{0} day {1} Hour'.format(math.trunc(self.sim_time / 24), self.sim_time % 24)
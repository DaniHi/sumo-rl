import os
import sys
from pathlib import Path

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare the environment variable 'SUMO_HOME'")
import traci
import sumolib


class InductionLoops:

    def __init__(self, env, i_id, delta_time, min_length):
        self.env = env
        self.id = i_id
        self.delta_time = delta_time
        self.min_length = min_length
        lane = traci.inductionloop.getLaneID(self.id)
        results = traci.inductionloop.getTimeSinceDetection(self.id)

    def has_car(self):
        return traci.inductionloop.getTimeSinceDetection(self.id) == 0.0

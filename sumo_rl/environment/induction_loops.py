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

    def __init__(self, env, i_id, delta_time, min_length, occupancy=70):
        self.env = env
        self.id = i_id
        self.delta_time = delta_time
        self.min_length = min_length
        self.backlog_occupancy = occupancy
        self.lane = traci.inductionloop.getLaneID(self.id)

    def last_detection(self):
        return traci.inductionloop.getTimeSinceDetection(self.id)

    def car_on_detector(self):
        return self.last_detection() == 0.0

    def car_passing(self):
        return self.last_detection() <= self.min_length

    def occupancy(self):
        return traci.inductionloop.getLastStepOccupancy(self.id)

    def has_backlog(self):
        return self.occupancy() > self.backlog_occupancy



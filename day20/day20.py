import re
import copy
from collections import defaultdict
from more_itertools import difference
LOW = -1
HIGH = 1
PULSES = defaultdict(int)
class ConjuntionModule:
    def __init__(self, name, destination_modules) -> None:
        self.destinationModules = destination_modules
        self.name = name
        self.incomingPulses = {}

    def add_incoming(self, incoming):
        self.incomingPulses[incoming] = LOW
    def transmit(self, pulse):
        newPulses = []
        for d in self.destinationModules:
            PULSES[pulse] += 1
            newPulses.append((pulse, self.name, d))
        return newPulses
    def receive(self, pulse, sender):
        self.incomingPulses[sender] = pulse
        if sum(self.incomingPulses.values()) == len(self.incomingPulses.values()):
            return self.transmit(LOW)
        else:
            return self.transmit(HIGH)
    def print(self):
        print(f"Module {self.name}, incomingPulses = {self.incomingPulses.items()}, DestinationModules = {self.destinationModules}")
class BroadCastModule:
    def __init__(self, name, destination_modules) -> None:
        self.destinationModules = destination_modules
        self.name = name
    def transmit(self, pulse):
        newPulses = []
        for d in self.destinationModules:
            PULSES[pulse] += 1
            newPulses.append((pulse, self.name, d))
        return newPulses
    
    def receive(self, pulse, sender):
        return self.transmit(pulse)

    def print(self):
        print(f"Broadcaster: {self.name}, destinations = {self.destinationModules}")
class FlipFlopModule:
    def __init__(self, name, destination_modules) -> None:
        self.destinationModules = destination_modules
        self.name = name
        self.on = -1
    def transmit(self, pulse):
        newPulses = []
        for d in self.destinationModules:
            PULSES[pulse] += 1
            newPulses.append((pulse, self.name, d))
        return newPulses
    def receive(self, pulse, sender):
        if pulse == LOW and self.on == 1:
            self.on *= -1
            return self.transmit(LOW)
        elif pulse == LOW and self.on == -1:
            self.on *= -1
            return self.transmit(HIGH)
        else:
            return []
    def print(self):
        print(f"Module {self.name}, Power on: {self.on}, DestinationModules = {self.destinationModules}")

def main():
    data = open("day20/input.txt","r").readlines()
    graph = {}
    pattern = r"\w+"
    conjunction_modules = []
    for d in data:
        match = re.findall(pattern, d)
        module = match[0]
        destination_modules = match[1:]
        if d[0] == "%":
            graph[module] = FlipFlopModule(module, destination_modules)
        elif d[0] == "&":
            graph[module] = ConjuntionModule(module, destination_modules)
            conjunction_modules.append(module)
        else:
            graph[module] = BroadCastModule(module, destination_modules)

    for d in data: # Initialize conjunction incoming pulses to Low
        match = re.findall(pattern, d)
        module = match[0]
        destination_modules = match[1:]
        for c in conjunction_modules:
            if c in destination_modules:
                graph[c].add_incoming(module)
    
    high_to_tg = defaultdict(list)
    for ix in range(10000):
        PULSES[LOW] += 1
        #       Pulse,      sender  receiver
        pulses = [(LOW, "button", "broadcaster")]
        while pulses:
            newPulses = []
            for p in pulses:
                if p[2] == "tg" and p[0] == HIGH:
                    high_to_tg[p[1]].append(ix)
                if p[2] in graph.keys():
                    newPulses.extend(graph[p[2]].receive(p[0], p[1]))
            pulses = copy.deepcopy(newPulses)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm_of_list(numbers):
        lcm_result = 1
        for num in numbers:
            lcm_result = (lcm_result * num) // gcd(lcm_result, num)
        return lcm_result
    
    cycles = []
    for v in high_to_tg.values():
        cycles.append(list(difference(v, initial=0))[0])
    print(lcm_of_list(cycles))
if __name__ == "__main__":
    main()
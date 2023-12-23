import re
from turtle import position

def parse_workflows(data):
    workflows = {}
    for line in data.split("\n"):
        name = line.split("{")[0]
        allRules = line.split("{")[1]
        allRules = "".join(allRules).split(",")
        workflows[name] = allRules
    return workflows

def main():
    data = open("day19/input.txt", "r").read().split("\n\n")
    workflows = data[0]
    workflows = parse_workflows(workflows)
    parts = data[1].split("\n")
    pattern = r"\d+"
    tot_sum = 0
    for p in parts:
        values = re.findall(pattern, p)
        x = int(values[0])
        m = int(values[1])
        a = int(values[2])
        s = int(values[3])

        partVals = [x,m,a,s]
        position = "in"
        while position not in ["A", "R"]:
            rules = workflows[position]
            for r in rules:
                r = r.replace("}", "")
                if ":" in r:
                    condition, destination = r.split(":")
                    if eval(condition):
                        position = destination
                        break
                else:
                    position = r
        if position == "A":
            print(x, m, a, s)
            for p in partVals:
                tot_sum += int(p)
    print(tot_sum)

if __name__ == "__main__":
    main()
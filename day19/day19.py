from collections import defaultdict
import re

def parse_workflows(data):
    workflows = {}
    for line in data.split("\n"):
        name = line.split("{")[0]
        allRules = line.split("{")[1]
        allRules = "".join(allRules).split(",")
        workflows[name] = allRules
    return workflows

def reverseCondition(condition):
    if "<" in condition:
        return "<", ">="
    elif ">" in condition:
        return ">", "<="
    else:
        raise Exception("error")
    
def main():
    data = open("day19/input.txt", "r").read().split("\n\n")
    data = open("day19/test.txt", "r").read().split("\n\n")

    workflows = data[0]
    workflows = parse_workflows(workflows)
    positions = [("in", [])]
    ARules = []
    while positions:
        position, pos_conditions = positions.pop(0)
        if position in ["A"]:
            ARules.append(pos_conditions)
            continue
        if position in ["R"]:
            continue
        rules = workflows[position]
        reverseConditions = []
        addedRules = []
        for r in rules:
            r = r.replace("}", "")
            if ":" in r:
                condition, destination = r.split(":")
                to_replace, replacement = reverseCondition(condition)
                reversedCondition = condition.replace(to_replace, replacement)

                newTuple = (destination, [*pos_conditions, *addedRules, condition])
                positions.append(newTuple)
                reverseConditions.append(reversedCondition)
                addedRules.append(reversedCondition)
            else:
                newTuple = (r, [*pos_conditions, *reverseConditions])
                positions.append(newTuple)

    pattern1 = r"[a-z]"
    pattern2 = r"\W+"
    pattern3 = r"\d+"
    tot_sum = 0
    conditions = []
    for a in ARules:
        baseCondition = {"x": [1,4000], "m": [1,4000], "a": [1,4000], "s": [1,4000]}
        for condition in a:
            charCond = re.findall(pattern1, condition)[0]
            minMax = re.findall(pattern2, condition)[0]
            digit = re.findall(pattern3, condition)[0]
            if minMax == "<":
                baseCondition[charCond][1] = min(int(digit)-1, baseCondition[charCond][1])
            elif minMax == "<=":
                baseCondition[charCond][1] = min(int(digit), baseCondition[charCond][1])
            elif minMax == ">":
                baseCondition[charCond][0] = max(int(digit)+1, baseCondition[charCond][0])
            elif minMax == ">=":
                baseCondition[charCond][0] = max(int(digit), baseCondition[charCond][0])
            else:
                raise Exception("error")
        conditions.append(baseCondition)

    
    solved = [list(conditions[0].values())]
    for p in conditions:
        print(p)
    tot_sum = 0
    for p in conditions:
        tmp = 1
        for x,y in p.values():
            tmp *= (y-x+1)
        tot_sum += tmp
    print(tot_sum)

    if tot_sum == 167409079868000:
        print("Correct on the test!!")
    else:
        print("incorrect", 167409079868000-tot_sum)
    print(len(solved))
    print(len(conditions))
if __name__ == "__main__":
    main()
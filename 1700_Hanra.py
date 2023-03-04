# BaekJoon 1700 multi-tab optimization problem

# 2 7
numTab, N = map(int, input().split())
# 2 3 2 3 1 2 7
electronics = list(map(int, input().split()))
# counting unplug
result = 0
# multi-tab
multitab = []

for idx, elec in enumerate(electronics):
    # scenario 1 : if elec is in the tab
    if elec in multitab:
        continue
    # scenario 2 : if multi-tab is not full
    elif len(multitab) < numTab:
        multitab.append(elec)
    # scenario 3 : if multi-tab is full
    # 2 cases can be here
    # 1. if the electronic will be no longer used in the future, unplug it
    # 2. if the electrnoic will be used for the most last
    else:
        temp = 0
        tempElec = multitab[0]
        for e in multitab:
            if e not in electronics[idx+1:]:
                tempElec = e
                break
            elif electronics[idx+1:].index(e) > temp:
                    temp = electronics[idx+1:].index(e)
                    tempElec = e
        # print(elec, multitab, tempElec)
        multitab.remove(tempElec)
        multitab.append(elec)
        result += 1

print(result)

from person import Person

people = []
modalities = set()
tiers = {'20-24' : [], '25-29' : [], '30-34' : [], '35-39' : []}

def parseCSV():
    file = open("emd.csv", "r", encoding='utf-8')

    lines = file.readlines()

    for line in lines[1::]:
        values = line.strip().split(',')
        modalities.add(values[8])
        people.append(Person(values))

def parseInfo():
    total = 0
    fit = 0
    unfit = 0
    for p in people:

        if p.isFit() == 'true':
            fit += 1
        else:
            unfit += 1

        total += 1
        
        age = p.getAge()
        if age // 5 == 4:
            tiers['20-24'].append(p)
        elif age // 5 == 5:
            tiers['25-29'].append(p)
        elif age // 5 == 6:
            tiers['30-34'].append(p)
        else:
            tiers['35-39'].append(p)
        

    return fit, unfit, total
    
        

if  __name__ == '__main__':
    parseCSV()
    fit, unfit, total = parseInfo()
    print(f'Modalidades encontradas: {sorted(modalities, key=lambda x: x.lower())}')
    print(f'Atletas Aptos: {round((fit / total) * 100, 2)}%')
    print(f'Atletas Inaptos: {round((unfit / total) * 100, 2)}%')
    print()
    for tier, person in tiers.items():
        print(f'------------ Tier {tier}------------')
        for p in person:
            print(p)
        print()

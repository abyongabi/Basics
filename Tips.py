staff = {}

def cal():
    res = {}
    amt = float(input("Enter total: "))
    tot_hrs = 0
    while True:
        name = input("Enter staff's name: ").strip().upper()
        val = float(input(f"Enter {name}'s working hour: "))
        tot_hrs += val
        res[name] = val
        choice = input("Are you done? [y/n]" ).lower()
        if choice == 'y':
            break
    por = amt/tot_hrs
    for i in res.keys():
        res[i] = res[i] * por
    return res

print(cal())


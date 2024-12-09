def tabla_verdad():
    print("x | y | z | F")
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                f = (not x and (y or not z)) and z
                print(f"{x} | {y} | {z} | {int(f)}")

tabla_verdad()

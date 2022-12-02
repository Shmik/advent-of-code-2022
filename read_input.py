def read_input(day, part): 
    import csv
    with open(f"day-{day}/part-{part}-input.txt", "r") as f:
        reader = csv.reader(f)
        x = []
        for a in reader:
            if len(a) > 0:
                x.append(a[0])
            else:
                x.append(None)
    return x
    
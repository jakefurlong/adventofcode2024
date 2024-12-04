with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

safe = 0

for line in lines:
    report = []
    for i in line.split():
        report.append(int(i))

    score = 0
    print("Processing report...", report)

    if len(set(report)) == len(report):
        score += 1
        print("Safe (no duplicates):", report)

    if sorted(report) == report:
        score += 1
        print("Safe (Integers are ascending):", report)

    if sorted(report, reverse=True) == report:
        score += 1
        print("Safe (Integers are descending):", report)

    for i in range(len(report) - 1):
        if len(report) > 1 and abs(report[0] - report[1]) <= 3:
            report = report[1:]
            if len(report) == 1:
                score += 1
                print("Safe (Integers are no more than 2 apart):")
        else:
            break

    print("\n")

    if score == 3:
        safe += 1

print(safe)
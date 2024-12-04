# 1
def is_safe(report):
    differences = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
    if not all(1 <= diff <= 3 for diff in differences):
        return False
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    return increasing or decreasing

# 2
def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    
    return False

file_path = "day_2.txt"
with open(file_path, "r") as file:
    reports = [list(map(int, line.split())) for line in file.readlines()]

safe_reports_count_1 = sum(is_safe(report) for report in reports)
print(f"Number of safe reports 1: {safe_reports_count_1}")

safe_reports_count_2 = sum(is_safe_with_dampener(report) for report in reports)
print(f"Number of safe reports 2: {safe_reports_count_2}")
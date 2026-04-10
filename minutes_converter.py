def convert_minutes(n):
    hrs = n // 60
    mins = n % 60
    if hrs > 0:
        return f"{hrs} hr {mins} minutes"
    else:
        return f"{mins} minutes"

print(convert_minutes(130))

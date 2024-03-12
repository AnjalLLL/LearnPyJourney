def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars=d.split("$")
    return int("".join(dollars))


def percent_to_float(p):
    percent=p.split("%")
    return int("".join(percent))


main()
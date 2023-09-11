""""program som fongar flera tuper av fel i koden"""

try:
    x = int(input("tal1? "))
    y = int(input("tal2? "))
    print(x/y)

except ZeroDivisionError:
    print("oj, du dividerade du med noll")

except ValueError:
    print("det där är inte ett tal!")

except Exception:
    print(f"Ett oförutsett problem uppstod")

## Vineyard planting. 

# грядки(м) - R
# виноград. лоза(шт) - V
# земля под опору(м) - E
# расстояние между лозами(м) S

# сколько нужно виноградных лоз под посадку?

def vine(r, e, s):
    global V
    v = int((r - 2 * e) / s)
    print(f"You need {v} vines to plant.")

print("Program for calculating vines (plugs). Enter the following values.\n")
r = float(input("The length of the beds(meters): "))
e = float(input("The support space(meters): "))
s = float(input("Distance between vines(meters): "))

vine(r, e, s)


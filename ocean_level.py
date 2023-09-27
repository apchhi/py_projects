# # ocean level
# up per year by (mm)
up_ocean = 1.6
# meters
level = 3.2
# all years
years = 25

print("Years\t\t\tOcean level(m)")
print("---------------------------------------------")
for count in range(years):
  year = count + 1
  level = level + (up_ocean / 1000)
  print("{}\t\t\t\t{:.5f}".format(year, level))


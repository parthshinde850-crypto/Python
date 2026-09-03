import matplotlib.pyplot as plt

# Sample data
years = [2015, 2016, 2017, 2018, 2019, 2020]
population = [50, 55, 60, 67, 73, 80]

# Line plot
plt.plot(years, population)

# Labels and title
plt.xlabel("Years")
plt.ylabel("Population (in thousands)")
plt.title("Population Growth Over Years")
plt.grid(True)
plt.show()
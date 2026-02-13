class planet():   # instantiate like this: earth = planet("Earth", "blue", 3)
    def __init__(self, name, color="blue", radius=1):
        self.color = color
        self.radius = radius
        self.name = name
        self.moon_list = []


class moon():
    def __init__(self, name, color="white", radius=1,
                 tidally_locked=False, planet_companion=None):
        self.name = name
        self.radius = radius
        self.color = color
        self.planet_companion = planet_companion
        self.tidally_locked = tidally_locked

    def update_planet(self):
        if self.planet_companion is not None:
            self.planet_companion.moon_list.append(self)


def print_largest(pl):
    largest = None
    for m in pl.moon_list:
        if largest is None:
            largest = m
        else:
            if largest.radius < m.radius:
                largest = m
    if largest is not None:
        print(f"The largest moon of {pl.name} is {largest.name}")


import pandas as pd

df = pd.read_csv('planet_data.csv', index_col='eName')
df = df[['isPlanet', 'meanRadius', 'orbit_type', 'orbits']]

planet_d = dict()
moon_d = dict()

# First loop: create planet objects
for index, row in df.iterrows():
    if row['isPlanet'] is True:
        planet_d[index] = planet(name=index, radius=row['meanRadius'])
        

# Second loop: create moon objects
for index, row in df.iterrows():
    if row['isPlanet'] is False:
        moon_d[index] = moon(
            name=index,
            radius=row['meanRadius'],
            planet_companion=planet_d[row['orbits']]
        )

# Attach moons to planets
for key, val in moon_d.items():
    val.update_planet()

# Print largest moon for each planet
for key, val in planet_d.items():
    print_largest(val)

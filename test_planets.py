from planet_classes import planet, moon


def test_planet_creation():
    earth = planet("Earth", radius=6371)
    assert earth.name == "Earth"
    assert earth.radius == 6371
    assert earth.moon_list == []


def test_update_planet():
    earth = planet("Earth", radius=6371)
    moon1 = moon("Moon", radius=1737, planet_companion=earth)

    moon1.update_planet()

    assert moon1 in earth.moon_list


def test_multiple_moons():
    jupiter = planet("Jupiter", radius=69911)

    io = moon("Io", radius=1821, planet_companion=jupiter)
    europa = moon("Europa", radius=1560, planet_companion=jupiter)

    io.update_planet()
    europa.update_planet()

    assert len(jupiter.moon_list) == 2

# Bugs - the Robobunny
# Kevin McAleer April 2022

from bunny import Bunny
from time import sleep

bunny = Bunny()
bunny.name = "Bugs"

while True:

    bunny.hop()
    sleep(10)



import glob
from spleeter.separator import Separator
print(glob.glob("./Audio/*"))

print("Flag 1")
# Using embedded configuration.
separator = Separator('spleeter:2stems')
print("Flag 2")
separator.separate_to_file('./Audio/song.mp3', './Audio')
print("Flag 3")


print(glob.glob("./Audio/song/*"))
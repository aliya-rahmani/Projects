# Find all words have dupplicated characters
import re


## Data
text = '''
Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.
Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.
HOW IT SPREADS
The virus that causes COVID-19 is mainly transmitted through droplets generated when an infected person coughs, sneezes, or exhales. These droplets are too heavy to hang in the air, and quickly fall on floors or surfaces.
You can be infected by breathing in the virus if you are within close proximity of someone who has COVID-19, or by touching a contaminated surface and then your eyes, nose or mouth.
'''


duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)


## Results
print(duplicates)
# [('fall', 'l'), ('will', 'l'), ('transmitted', 't'), ('sneezes,', 'e'), ('too', 'o'), ('fall', 'l'), ('floors', 'o')]
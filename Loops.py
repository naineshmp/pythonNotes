# TODO: ENUMEARTION WITH INDEX, NON INDEX LOOPS AND SO ON...
from tqdm.auto import tqdm

list = [1, 2, 3, 4, 5, 6]

for i in list:
    print(i)


# enumerate returns tuple!!! with position, value
for count, value in enumerate(list):
    print(f"{count} - {value}");


# range looping with reverse order
# range(start, stop, step)
for i in range(5, -1, -1):
    print(i)


i = 99
while i >= 98:
    i -= 1
    print(i)

# for i in tqdm(range(len(list))):
#     print(i)

# ######################################  CRAZZY SHORTCUTS  ##########################################

# Swap values!
list[0], list[2] = list[2], list[0]


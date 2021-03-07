# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
#

#
#

# TODO: ENUMEARTION WITH INDEX, NON INDEX LOOPS AND SO ON...

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

from tqdm.auto import tqdm
for i in tqdm(range(len(df))):
    print(i)
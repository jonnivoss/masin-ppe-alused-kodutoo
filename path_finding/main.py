import bfs
import greedy
import a_star

lava_map1 = [
    "      **               **      ",
    "     ***     D        ***      ",
    "     ***                       ",
    "                      *****    ",
    "           ****      ********  ",
    "           ***          *******",
    " **                      ******",
    "*****             ****     *** ",
    "*****              **          ",
    "***                            ",
    "              **         ******",
    "**            ***       *******",
    "***                      ***** ",
    "                               ",
    "                s              ",
]
lava_map2 = [
    "     **********************    ",
    "   *******   D    **********   ",
    "   *******                     ",
    " ****************    **********",
    "***********          ********  ",
    "            *******************",
    " ********    ******************",
    "********                   ****",
    "*****       ************       ",
    "***               *********    ",
    "*      ******      ************",
    "*****************       *******",
    "***      ****            ***** ",
    "                               ",
    "                s              ",
]

with open("cave300x300") as f:
    map_data1 = [l.strip() for l in f.readlines() if len(l)>1]
with open("cave600x600") as f:
    map_data2 = [l.strip() for l in f.readlines() if len(l)>1]
with open("cave900x900") as f:
    map_data3 = [l.strip() for l in f.readlines() if len(l)>1]

print("300x300 tulemused")
bfs.search(map_data1)
greedy.search(map_data1)
a_star.search(map_data1)

print("600x600 tulemused")
bfs.search(map_data2)
greedy.search(map_data2)
a_star.search(map_data2)

print("900x900 tulemused")
bfs.search(map_data3)
greedy.search(map_data3)
a_star.search(map_data3)



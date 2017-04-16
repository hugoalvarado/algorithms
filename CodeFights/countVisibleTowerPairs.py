'''
CodeFights

Define a tower as a straight vertical segment with a bottom end on the X axis.

Consider some towers in pairwise distinct positions. A pair of towers is called visible if the segment that connects the top points of those towers doesn't cross any other tower (but may touch the tops of some towers).

Given positions on which the towers stand and heights of the towers, find the number of visible pairs of towers.

Example

for position = [3, 0, 6, 10], height = [2, 1, 4, 6] output should be 4

[input] array.integer position

[input] array.integer height

array of positive integers. i-th elements of both arrays correspond to the same tower [output] integer
'''
def countVisibleTowerPairs(position, height):

    towers = {position[i]:height[i] for i in range(len(position)) }

    sorted_position = sorted(position)

    visible_towers = 0

    print(sorted(towers))


    for p1 in sorted(towers):

        middle_towers = []

        for p2 in sorted(towers):

                if p2 <= p1:
                    #we've already checked this pair of towers
                    continue


                if adjacent_towers(p1, p2, sorted_position):
                    #add to list of visible
                    visible_towers += 1
                    #add to list of in-between
                    middle_towers.append(p2)
                    print(p1,p2,':!!',visible_towers)
                    continue


                m = (towers[p2]-towers[p1])/(p2-p1)
                b = towers[p1]-(m*p1)

                print()
                print(p1,p2,':',visible_towers)

                #print(m, towers[p2], towers[p1], p2, p1)


                visible = True

                for middle_position in middle_towers:

                    x = middle_position
                    y = towers[middle_position]

                    print('m',middle_position, y)
                    print(m, b)

                    if y > m*x+b:
                        visible = False
                        break

                if visible:
                    visible_towers += 1
                    print(p1,p2,':!',visible_towers)

                middle_towers.append(p2)














                #print(p, towers[p])
                #
    return visible_towers


def adjacent_towers(p1,p2,positions):
    return abs(positions.index(p1)-positions.index(p2)) == 1



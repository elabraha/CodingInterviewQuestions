# If an egg is dropped from above that floor, it will break. If it is dropped
# from that floor or below, it will be completely undamaged and you can drop the
# egg again.
#
# Given two eggs, find the highest floor an egg can be dropped from without
# breaking, with as few drops as possible.

def floor_egg_break(floors):
    # This is my first attempt, it just involves going 2 floors at a time:
    # drop_point = 0
    # for i in range(0, len(floors), 2):
    #     if floors[i]:
    #         drop_point = i
    #         break
    # if drop_point >= 1:
    #     if not floors[drop_point - 1]:
    #         return drop_point - 1 # returning the floor starting at 0
    #     else:
    #         return drop_point
    # An equally dumb idea is to go up by half of the floors (50) and then if
    # it breaks go up from the first floor to the 50th and if it doesn't
    # go up from the 50th to the 100th and where ever it breaks, the floor
    # before that is the answer. I think it has the same runtime as the above.

    # So a better idea is the make the drop point somewhere between 50 and 2.
    # How about we try 10. I'm not sure what the perfect jumps are it would be
    # trial and error for me to know because I don't know the math.
    # drop_point = 100
    # for i in range(10, 100, 10):
    #     if floors[i]:
    #         drop_point = i
    #         break
    # for i in range(drop_point - 10, drop_point):
    #     if floors[i]:
    #         drop_point = i - 1
    #         break
    # return drop_point
    # Maybe there's a certain point at which the division of 100 is not worth
    # it going up by 5 is too small worst case is already maybe 24? Going up by
    # 20. Worst case is 5 plus the 19 you'll have to go up which is exactly the
    # same. As before 24. My current method is 10 plus the 9 that it will take
    # to search. the last one. I can do better maybe 15 which does not divide
    # evenly so you have about 7 divisions and then one will be shorter but it
    # is still not great. In fact it is worse, it's at 20. So maybe smaller is
    # better 8. Worst case is 19 maybe 21? Still not any better,

    # I did a combo of trial and error plus a hint. what if we tried to even
    # out the jumps. There are less on the lower end and high on the higher
    # end. I feel like I thought that but since I increased the size of the
    # jumps that would be better but it's not becuase than you have to check
    # in between the jumps in floors. I was dumb and didn't think to only have
    # a high number in the beginning. I just did trial and error to see where
    # I should start in terms of the number from 10+9+8+7... Then tried 11,
    # 12, 13

    jump_height = 14
    drop_point = 100
    i = jump_height
    while i < 100:
        if floors[i]:
            drop_point = i
            break
        jump_height-=1
        i+=jump_height

    for j in range(drop_point - jump_height, drop_point):
        if floors[j]:
            drop_point = j - 1
            break
    return drop_point
    # Ugh another arithmatic sum series thing n^2 - n all over 2 equals 100.
    # solve for n. n is 13 plus some fraction.

def main():
    floors = [False for _ in range(0, 48)] # at floor 48 if we are starting at 1
    for _ in range(48, 100):
        floors.append(True)
    print("egg will not break up to floor:", floor_egg_break(floors))

main()

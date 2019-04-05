def hanoi(num,fromPole, toPole, via):
    if num >= 1:
        hanoi(num-1,fromPole,via,toPole)
        print("move disk from",fromPole,"to",toPole)
        hanoi(num-1,via,toPole,fromPole)

#main; test case 3
#move from "A" to "B"
hanoi(3,"A","B","C")

#result
#move disk from A to B
#move disk from A to C
#move disk from B to C
#move disk from A to B
#move disk from C to A
#move disk from C to B
#move disk from A to B

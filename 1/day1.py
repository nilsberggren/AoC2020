def main():
    with open('input.txt') as input:
        Lines = input.readlines()

    target = 2020

#Part 1
#Find the two entries that sum to 2020; what do you get if you multiply them together?
    for line in Lines:
        line.strip()
        for i in Lines:
            i.strip()
            answer = int(line)+int(i)
            if answer == target:
                solution = int(line)*int(i)
                break
    print("Part 1: "+str(solution))
    answer = 0

#Part 2
#Find the three entries that sum to 2020; what do you get if you multiply them together?
    for line in Lines:
        line.strip()
        for i in Lines:
            i.strip()
            for j in Lines:
                j.strip()
                answer = int(line)+int(i)+int(j)
                if answer == target:
                    solution = int(line)*int(i)*int(j)
                    break                
    print("Part 2: "+str(solution))

if __name__ == "__main__": main()
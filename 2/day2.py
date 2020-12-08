def main():
    
    with open('input.txt') as input:
        lines = input.readlines()

    #Part 1
    dataCount = 0
    solution = 0

    for line in lines:
        count = 0
        dataCount += 1
        data = line.strip().split()

        count = data[2].count(data[1][0])
        min = int(data[0].split("-")[0])
        max = int(data[0].split("-")[1])

        if count > max or count < min:
            pass
        else:
            solution += 1
    

    #Part 2 - some error in this one, answer should be 711 but below code gives 485 for some reason
    solution2 = 0

    for line in lines:
        
        validation1 = False
        validation2 = False
        counter = 0
        data = line.strip().split()
        pos1 = int(data[0].split("-")[0])
        pos2 = int(data[0].split("-")[1])
        password = str(data[2])
        needed_char = str(data[1][0])
        
        while pos1 and pos2 in range(len(password)) and counter < 1:
            
            #Logging to see what's going on since we get wrong result at the end
            print(password+" should contain "+needed_char+" at position "+str(pos1)+" or "+str(pos2))
            print(line)
            print(password[pos1-1])
            print(password[pos2-1])
            
            if password[pos1-1] is needed_char:
                validation1 = True
                print("First pos OK")
            
            if password[pos2-1] is needed_char:
                validation2 = True
                print("Last pos OK")

            if validation1 ^ validation2 is True:
                solution2 += 1

            counter += 1
            
    #Print total amount of passwords in file (should be 1k) and solution for part 1 and 2
    print("Total passwords: "+str(dataCount))
    print("Valid passwords part 1: "+str(solution))
    print("Valid passwords part 2: "+str(solution2))


if __name__ == "__main__": main()
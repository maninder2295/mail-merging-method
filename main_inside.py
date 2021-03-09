#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("./Input/Names/invited_names.txt") as f:
    for name in f:
        names.append(name)

    for i in range(len(names)):
        with open("./Input/Letters/starting_letter.txt") as f:
            data = f.read()
            n = data.replace('[name]', names[i])

        names_all = names[i].replace("\n", '.')
        # or I can use strip() method to deduce the space
        #names_all = names[i].strip()

        with open(f"./Output/ReadyToSend/Letter_for_{names_all}.txt", "w") as ink:
            ink.write(n)








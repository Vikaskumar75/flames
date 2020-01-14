first = input("enter the first name -->")
second = input("enter the second name -->")

        # changing all the characters to lower case

first = first.lower()
second = second.lower()

        # relacing spaces with no spaces

first = first.replace(" ","")
second = second.replace(" ","")

        # reading the names and finding out similar characters

for i in first :
    for j in second :
        if i == j :
            first = first.replace(i,"",1)
            second = second.replace(i,"",1)
            break           # here break is used to give control to loop 1

        #combining the length of remaining alphabets

combining = second + first

# print(len(combining))

flames = ["friendship","lovers","attraction","marriage","enemy","sibling"]      # all relation in flames

        # finding out the relation

if len(combining) == 0 :
    print("Both names are same,please try with full name")
else :
    while len(flames) > 1 :                      # this loop will run until one relation is left
        index = len(combining)% len(flames)
        correct_index = index-1                  # since a list index starts from 0 i have to reduce it by 1 it will be negative if combining = 6

        # seperating the flames list and removing the correct index

        if correct_index >= 0 :
            left = flames[:correct_index]                   # this will form a list from starting to correct index without including it
            right = flames[(correct_index + 1) :]           # this will form a list from next character of correct index to the end

            # conicinating the list

            flames = right + left                           # right is added to the the left to continue the counting from correct index +1

        else :
            flames = flames[:len(flames)-1]                 # if combining = 6 then correct index will be -1 therefore it will return
                                                            # back to last element of list thus with this code we shorten the list from
                                                            # starting to 2nd last element and so on

    print("You both are :",flames[0])

    #! Given 2 variables word1 and word2, write code to
    #! print the concatenation of the 2 words omitting the
    #! first_folder letter of the string saved in word1 and the second_folder
    #! letter of the string saved in word2.
    
    #! Example:
    #! ---------------
    #! word1 = "Vehicle"
    #! word2 = "Robot"
    #! result - ehicleRbot


word1 = "Vehicle"
word2 = "Robot"

result = word1[1:] + word2[0] + word2[2:]

print(result)
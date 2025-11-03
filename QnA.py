print("----Welcome to QnA program----")
# Taking a .txt file as a user input
file_name = input("Enter a valid .txt file {eg : notes.txt}: ")

# reading the file given by using the built in function .read()
with open(file_name,'r') as file:
    read = file.read()

# splitting the string generated in "read" from the places where the the new paragraph begins 
paragraphs = read.split("\n\n")

#List of all unwanted words, which should not be included in calculating confidence score
unwanted_words = ["is","a","are","who","how","when","or","and",'whose','where','what',
'at', 'on','he','she','which',]

#Taking the Question from the user
Q = input("Enter the question : ")

#Formatting the Question words into a list
Q_words = Q.lower().split()
Q_precise = [word for word in Q_words if word not in unwanted_words]

# initiallising the confidence score and best match string to 0. 
confidence_score = 0
best_string = ""

# iterating each para from paragraphs to find the number of words matched. 
for para in paragraphs:
    words = para.lower().split()

    matched = [ word for word in Q_precise if word in words]
    score = len(matched)

    if score > confidence_score:
        confidence_score = score
        best_string = para


#Printing the final output. 
print("\n---- Most Appropriate answer----")
print(best_string)
print("Confidence-score : ",confidence_score)

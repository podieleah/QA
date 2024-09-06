# general comments
#2/3 generic lines

# Engagement and punctuality
#1 line

# Suggestions for further learning
#1 line

# requirements:

# type in all student names as an input
# prompt for each student to rate 1-4 in the following areas:
#     - understanding level
#     - contribution level
#     - lab completion level 
#     - punctuality level
#     - engagement level
#     - further-learning level

# mapa general template of the feedback and a map for score to descriptive word/phrases.

# output
# - individual file for each student with feedback in it
    
# optional
# - open the file for manual editing 

# save files to a folder - file names constructed with student names included

def get_student_names():
    student_names = []
    while True: 
        name = input("Enter a student name or 'quit' to finish: ")
        if name.lower() == "quit":
            break
        student_names.append(name)
    return student_names

def get_student_ratings(student_name):
    ratings = {}
    catergories = ["Understanding", "Contribution", "Lab Completion", "Punctuality", "Engagement", "Further Learning"]
    for catergory in catergories:
        rating = int(input(f"Rate {student_name} in {catergory} (1-4): "))
        ratings[catergory] = rating
    return ratings

def generate_feedback(student_name, ratings):
    feedback = f"Blah Blah {student_name}\n"
    feedback += "General Comments: \n"
    feedback += f"{student_name} made good progress"
    feedback += "\n Engagement and Punctuality: \n"
    feedback += f"{ratings['Engagement']} {ratings['Punctuality']} \n"
    feedback += "\n Suggestions for Further Learning: \n"
    feedback += "Consider blah blah blah"
                                                    
    return feedback

def save_feedback(student_name, feedback):
    filename = f"{student_name}_feedback.txt"
    with open(filename, "w")as f:
        f.write(feedback)

def main():
    student_names = get_student_names()
    for student_name in student_names:
        ratings = get_student_ratings(student_name)
        feedback = generate_feedback(student_name, ratings)
        save_feedback(student_name, feedback)

main()
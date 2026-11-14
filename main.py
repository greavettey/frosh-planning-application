from random import randint, sample
from database import init_database, get_database


def main(): 
    init_database("technical_submission.db")

    db = get_database()

    db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER);")

    peopel = ["Alice", "Axel", "Greg the chud"]
    questions = [["What is Normandy?", "Country in Norway"], ["Who made the air frier", "marie curie"], ["What is the air friar", "religious air frier or something"], ["who killed stalin", "joseph joestar"], ["how many r's are there in strawberrrry", "idk vro"]]
    answers = {}

    for person in peopel:
        db.execute("INSERT INTO users (name, age) VALUES (?, ?);", (person, randint(18, 99)))
        answers[person] = sample(list(range(len(questions))), 3) #this is probably the worst line of code ive ever written it flattens the array into an array of indicies that i then sample so that each person has an array of question array indicies assigned to them. 
        #i could've done this nicer but i liked my nested question answer format and whatever now you know im creative

    db.execute("CREATE TABLE IF NOT EXISTS scav_questions (id INTEGER PRIMARY KEY, question TEXT NOT NULL, answer TEXT NOT NULL, who_answered TEXT NOT NULL);")

    for i in range(5): 
        db.execute("INSERT INTO scav_questions (question, answer, who_answered) VALUES (?, ?, ?);", (questions[i][0], questions[i][1], ", ".join(person for person in peopel if i in answers[person]))) #again, terible way to do this but im committed to my design.

    for person in peopel:
        print(f"{person} answered the following questions:")
        for i in answers[person]:
            print(f"Question: {questions[i][0]}, Answer: {questions[i][1]}")
        print("\n")    
    
    db.save();

if __name__ == "__main__":
    main()
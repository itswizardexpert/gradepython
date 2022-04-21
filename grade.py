last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

grade =  {
  "physics":98, 
  "calculus":97, 
  "poetry":85,
  "history":88
}

gradebook =  [
  ["physics",98], 
  ["calculus",97], 
  ["poetry",85],
  ["history",88]
]

gradebook.append(["computer science",100])
gradebook.append(["visual arts", 93])
gradebook[5][1] = 98
gradebook.append(["pass"])

if gradebook[2][1] <= 50:
  gradebook.remove(["poetry",5])

del grade["poetry"]

grade["computer science"] = 100
grade["visual arts"] = 93

full_gradebook = gradebook + last_semester_gradebook
grade.update(last_semester_gradebook)

print(grade)
print(gradebook)
print(full_gradebook)
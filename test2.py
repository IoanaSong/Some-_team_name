import sys
skills = []
nr_skills = 0

info = open("a_an_example.in.txt").read().split("\n")
first_line = info[0].split(" ")
i = 0
people = 0
projects = 0
while people < int(first_line[0]):
    nr_skills = 0
    print(info[i + 1])
    contributor = info[i+1].split(" ")
    # individual contributor class goes here
    skills = []
    for j in range(0, int(contributor[1])):
        skills.append(info[i+j+2])
        for skill in skills:
            list_skills = skill.split(" ")
            print(list_skills[0])  # add here class for skill
            print(list_skills[1])  # add here class for level
        nr_skills += 1
        # skills class
    i += nr_skills + 1
    print(skills)
    people += 1
# while projects < int(first_line[1]):
#     print(info[i+1]


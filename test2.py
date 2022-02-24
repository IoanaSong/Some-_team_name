import sys
skills = []
nr_skills = 0

info = open("a_an_example.in.txt").read().split("\n")
first_line = info[0].split(" ")
i = 0
people = 0
while people < int(first_line[0]):
    print(info[i + 1])
    contributor = info[i+1].split(" ")
    # individual contributor class goes here
    for j in range(0, int(contributor[1])):
        skills.append(info[i+j+1])
        nr_skills += 1
        # skills class
    i += nr_skills + 1
    print(skills)
    people += 1


# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

def run(child_name):
    print(f'{child_name} ran all crazy like!')
    
def swing(child_name):
    print(f'{child_name} swung real high!')
    

def slide(child_name):
    print(f'{child_name} sild down the slide!')
    

def hide_and_seek(child_name):
    print(f'{child_name} played hide and seek!')


# For example, Jay ran like a fool! or Chantelle slid down the slide!.

# The following lists of children should be iterated, and the names sent to the appropriate functions.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

for kid in running_kids:
    run(kid)

for kid in swinging_kids:
    swing(kid)

for kid in sliding_kids:
    slide(kid)

for kid in hiding_kids:
    hide_and_seek(kid)


# # Function and variable names are snake case instead of camel case
# def create_person(first_name, last_name, age, occupation):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "age": age,
#         "occupation": occupation,
#     }

# melissa = create_person("Melissa", "Bell", 25, "Software Developer")
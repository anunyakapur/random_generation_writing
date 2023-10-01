import random

def create_person_id():
    string = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + "-" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + "-" + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) 
    return string

def create_person_name(index):
    with open("random_names.txt", "r") as file_in:
        name = file_in.readlines()
        chosen = name[index]
        return chosen

def create_random_occupation():
    with open("random_occupations.txt", "r") as file_in:
        job = file_in.readlines()
        chosen = random.choice(job) #fix
        return chosen

def salary():
    salary = random.randint(25, 125)
    return (f"${salary} 000")
    
def write_new_file():
    with open("random_entries.txt", "w") as file_out:
        for x in range(100):
            id_number = create_person_id()
            person_name = create_person_name(x)
            occupation = create_random_occupation()
            money = salary()
            entry = f'{id_number} ' + f'{person_name} ' + f'{occupation} ' + f'{money}' + '\n'
            file_out.write(entry)

write_new_file()

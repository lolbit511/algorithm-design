#print("Hello World!")
#print("this is my first program")

name = input("what is your name?")
age = int(input("what is your age?"))

def check_travel(name):
    travel = input("have you traveled lately?")
    if (travel == "yes" or travel == "YES"):
        print("moderate risk, isolate yourself immediately")
    else:
        print("low risk")

def check_for_covid(name,age):
    fever = input("do you have a fever?")
    if (fever == "YES" or fever == "yes"):
        med = input("do u have high blood presure or diabetes?")

        if (age > 50 or med =="YES" or med =="yes"):
            print("high risk")
        elif(age<6):
            print("high risk")
        else:
            check_travel(name)
    else:
        check_travel(name)

def main():
    symptoms = ["headache", "breathlessness", "sore throat", "body pain", "lost of taste"]

    yoursymptoms = input("what is your symptom")
    need_to_check = False
    for x in symptoms:
        if (x == yoursymptoms):
            need_to_check = True
        #else:
         #   need_to_check = False
    if (need_to_check == True):
        check_for_covid(name,age)
    else:
        print("no need for covid test")
#main()



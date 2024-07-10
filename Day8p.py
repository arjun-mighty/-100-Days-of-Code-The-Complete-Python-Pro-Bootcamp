def greet():
    name = input("Enter your name :")
   # print(f"Hello {name}")
    print("How do you do ?")
    print("Is int the weather sexy today ?")
    
greet()

#positional arguments
def greet_with_welcome(name,location):
    print(f"Welcome {name},to{location}")
   
    print("How do you do ?")
greet_with_welcome("Arjun,Scotland")
class Patient:
  #write a constructor
    def __init__(self, id, name, age, bloodgroup, next, prev):
        self.id = id
        self.name = name
        self.age = age
        self.bloodgroup = bloodgroup
        self.next = next
        self.prev = prev

class WRM:
    PatientCount = 0
    def __init__(self):
    #Creating the dummy head
        self.dh = Patient(None,None,None,None,None,None)
        self.dh.next = self.dh
        self.pointer = self.dh
        self.dh.prev = self.pointer
        

    def registerPatient(self,id, name, age, bloodgroup):

        self.pointer.next = Patient(id, name, age, bloodgroup, self.dh, self.pointer )
        self.pointer = self.pointer.next 
        #self.pointer.next = self.dh 
        print(f"{name} was Registered for Chikitsha\n")
        WRM.PatientCount+=1

    def servePatient(self):

        print(f"{self.dh.next.name} was given some Chikitsha\n")
        self.dh.next = self.dh.next.next
        self.dh.next.prev = self.dh
        self.pointer = self.dh.prev
        WRM.PatientCount-=1


    def showAllPatient(self):

        curr = self.dh.next
        i = 1
        while curr :
            print(f"{i} : Name: {curr.name}, ID: {curr.id}\n")
            i +=1
            curr = curr.next if curr.next != self.dh else None

    def canDoctorGoHome(self):
        if WRM.PatientCount!=0 :
            print("No Chuti for Doctor\n")
        else:
            print("Chuti is eligible\n")    

    def cancelAll(self):
        self.dh.next = self.dh
        self.pointer = self.dh
        self.dh.prev = self.pointer
        print("Khawa must be good cz all the appointments are cancelled\n")
        WRM.PatientCount = 0

    def ReverseTheLine(self):
            self.pointer.next = None
            self.dh.prev = None

            prev = None
            curr = self.dh.next
            
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            self.pointer = self.dh.next
            self.dh.next = prev
            prev.prev = self.dh
            self.pointer.next = self.dh
            self.dh.prev = self.pointer

            print("Bangladesh 1.0 happened , Current list\n ")
            self.showAllPatient()

#Write a Tester Code in this cell
WRM = WRM()
print("**Welcome to Waiting Room Management System**")
methods = [WRM.registerPatient,WRM.servePatient,WRM.showAllPatient,WRM.canDoctorGoHome,WRM.cancelAll,WRM.ReverseTheLine]
methods1 = ["registerPatient()","servePatient()","showAllPatient()","canDoctorGoHome()","cancelAll()","ReverseTheLine()"]
while True:
    
    print("***CHOOSE AN OPTION***\n")
    print("1.registerPatient()\n2. servePatient()\n3. showAllPatients()\n4. canDoctorGoHome()\n5. cancelAll()\n6. reverseTheLine()\n7. Exit")
    print("=================================================================")
    choice = int(input("Enter Your Choice: "))
    
    if 1<= choice <= 7:
        if choice == 7:
            break
        elif choice == 1:
            print(f"Executing {methods1[choice - 1]}")
            WRM.registerPatient(id= int(input("Enter ID: ")),name= input("Enter Name: "),age= input("Enter Age: "),bloodgroup= input("Enter BloodGroup: "))
        else:
            print(f"Executing {methods1[choice - 1]}\n")
            methods[choice - 1]()
    else:
        print("FROM 1 TO 7 BTW\n")        
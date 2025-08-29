# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:20:12 2023
@author: Admin
"""

import vs
import sys
class det():
    sd = {"vinay": "viay0000",
          "rakesh": "rash0000",
          "vasudendra": "vara0000",
          "dinesh": "dish0000"
          }
    rat = [1.0, 2.0, 3.0, 4.0, 5.0]
    ru = []
    ch = 0
    cho = 0
    crs = {"vinay": False, "rakesh": False, "vasudendra": False, "dinesh": False}

    def start(self):
        while self.ch != 2:
            print("---Welcome to RVVV institution official portal---")
            s = input("\n1. To login\n2. Exit\nSelect your choice: ")
            if not s.isdigit():
                print("Enter only numbers :)")
                continue
            s = int(s)
            if s == 1:
                print("---Welcome login to continue...")
                while True:
                    user = input("\nEnter user name: ")
                    ul = user.lower()  
                    if ul in self.sd:
                        f = self.sd[ul]
                        pas = input("Enter password: ")
                        if pas == f:
                            print("Welcome to RVVV portal")
                            i = input("\n1. To give rating\n2. To analyze\n3. To return back\nSelect one: ")
                            if not i.isdigit():
                                print("Enter only numbers :)")
                                continue
                            i = int(i)
                            if i == 1:
                                if not self.crs[ul]:
                                    if all(self.crs.values()):
                                        print("Ratings have been completed by all four people. Returning to the main menu.")
                                    else:
                                        c = 0
                                        na = input("Enter your name for giving rating: ")
                                        if na in vs.pr1:
                                            while c != 3:
                                                c += 1
                                                cs = input("\n1. Academic\n2. Sports\n3. Infrastructure\nSelect choice: ")
                                                if not cs.isdigit():
                                                    print("Enter only numbers :)")
                                                    continue
                                                cs = int(cs)
                                                if cs == 1:
                                                    print("See our academic performances....")
                                                    vs.pr()
                                                    vs.tr()
                                                    vs.cr()
                                                    tf = input("Rating for teaching faculty...(1.0-5.0): ")
                                                    try:
                                                        tf = float(tf)
                                                        if 1.0 <= tf <= 5.0:
                                                            print("done..")
                                                            vs.pr1[na]["Academic"] = tf
                                                        else:
                                                            print("Give the Rating in the range 1.0-5.0 ")
                                                            c -= 1
                                                    except ValueError:
                                                        print("Enter a valid number.")
                                                        c -= 1  
                                                elif cs == 2:
                                                    tf1 = input("Rating for ground maintainability...(1.0-5.0): ")
                                                    try:
                                                        tf1 = float(tf1)
                                                        if 1.0 <= tf1 <= 5.0:
                                                            print("done..")
                                                            vs.pr1[na]["GM"] = tf1
                                                        else:
                                                            print("Give the Rating in the range 1.0-5.0 ")
                                                            c -= 1  
                                                    except ValueError:
                                                        print("Enter a valid number.")
                                                        c -= 1  

                                                    tf2 = input("Rating for kits availability...(1.0-5.0): ")
                                                    try:
                                                        tf2 = float(tf2)
                                                        if 1.0 <= tf2 <= 5.0:
                                                            print("done..")
                                                            vs.pr1[na]["KA"] = tf2
                                                        else:
                                                            print("Give the Rating in the range 1.0-5.0 ")
                                                            c -= 1 
                                                    except ValueError:
                                                        print("Enter a valid number.")
                                                        c -= 1  

                                                    tf3 = input("Rating for students achievement in sports...(1.0-5.0): ")
                                                    try:
                                                        tf3 = float(tf3)
                                                        if 1.0 <= tf3 <= 5.0:
                                                            print("done..")
                                                            vs.pr1[na]["SAS"] = tf3
                                                        else:
                                                            print("Give the Rating in the range 1.0-5.0 ")
                                                            c -= 1  
                                                    except ValueError:
                                                        print("Enter a valid number.")
                                                        c -= 1 

                                                elif cs == 3:
                                                    tf4 = input("Rating for campus with all areas needed...(1.0-5.0): ")
                                                    try:
                                                        tf4 = float(tf4)
                                                        if 1.0 <= tf4 <= 5.0:
                                                            print("done..")
                                                            vs.pr1[na]["CampusWithAllAreasNeeded"] = tf4
                                                        else:
                                                            print("Give the Rating in the range 1.0-5.0 ")
                                                            c -= 1 
                                                    except ValueError:
                                                        print("Enter a valid number.")
                                                        c -= 1 

                                                    tf5 = input("Rating for Environment...(1.0-5.0): ")
                                                    try:
                                                        tf5 = float(tf5)
                                                        if 1.0 <= tf5 <= 5.0:
                                                            print("done..")
                                                            vs.pr1[na]["EN"] = tf5
                                                        else:
                                                            print("Give the Rating in the range 1.0-5.0 ")
                                                            c -= 1  
                                                    except ValueError:
                                                        print("Enter a valid number.")
                                                        c -= 1 

                                            
                                            self.crs[ul] = True
                                        else:
                                            print("Invalid name. Please enter a valid name.")
                                else:
                                    print("You have already given ratings. Returning to the main menu.")

                            elif i == 2:
                                if all(self.crs.values()):
                                    print("---Analysis of Ratings---")
                                    aac = sum(vs.pr1[name]["Academic"] for name in vs.pr1) / len(vs.pr1)
                                    agm = sum(vs.pr1[name]["GM"] for name in vs.pr1) / len(vs.pr1)
                                    aka = sum(vs.pr1[name]["KA"] for name in vs.pr1) / len(vs.pr1)
                                    asas = sum(vs.pr1[name]["SAS"] for name in vs.pr1) / len(vs.pr1)
                                    ae = sum(vs.pr1[name]["EN"] for name in vs.pr1) / len(vs.pr1)

                                    print("{:<20} {:<20}".format("Average Academic Rating:", aac))
                                    print("{:<20} {:<20}".format("Average Ground Maintainability Rating:", agm))
                                    print("{:<20} {:<20}".format("Average Kits Availability Rating:", aka))
                                    print("{:<20} {:<20}".format("Average Students Achievement in Sports Rating:", asas))
                                    print("{:<20} {:<20}".format("Average Environment Rating:", ae))
                                    oa=(aac+agm+aka+asas+ae)/6
                                    print("-----------------------------------------------------------------")
                                    print("Overall Average Rating for NAAC:", oa)
                                    if oa<=1.0:
                                        print("---B Grade---")
                                    elif oa<=2.5 and oa>=1.1:
                                        print("---B++ Grade---")
                                    elif oa<=3.5 and oa>=2.6:
                                        print("---A Grade---")
                                    elif oa<=5.0 and oa>=3.6:
                                        print("---A++ Grade---")
                                else:
                                    print("Analysis requires all four people to complete ratings.")
                            elif i == 3:
                                break
                            else:
                                print("Enter correct option :)")
                        else:
                            print("Your password is wrong :)")
                    else:
                        print("No name found!!")
                        break
        
            elif s==2:
                sys.exit()
            else: 
                 print("Enter correct choice:)")
d = det()
d.start()

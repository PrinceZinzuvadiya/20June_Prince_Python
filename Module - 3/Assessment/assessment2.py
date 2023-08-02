print("Hello there, Welcome to the Student Management system......")
print("")
print("\tPress 1 for Counsellor")
print("\tPress 2 for Faculty")
print("\tPress 3 for Student")
print("")

while True:
        userinp = (input("Please select a number: "))
        if userinp.isdigit():
            if userinp == '1':
                print("")
                print("\t1.Add student")
                print("\t2.Remove student")
                print("\t3.View all student")
                print("\t4.View specific student")
                print("")

                def counsellor_option(student_data, student_data2):
                    while True:
                        userinp1 = (input("Please select from above number: "))
                        if userinp1.isdigit():
                            if userinp1 == '1':
                                while True:
                                    student_id = input("Enter a student id: ")
                                    if student_id in student_id:
                                        break
                                    else:
                                        print("Please enter another student id")

                                while True:
                                    fnm = input("Enter a First name: ")
                                    if fnm.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break

                                while True:    
                                    lnm = input("Enter a Last name: ")
                                    if lnm.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break    
                                
                                while True:
                                    contact = input("Please enter contact number: ")
                                    if len(contact) == 10 and contact.isdigit():
                                        pass
                                    else:
                                        print("Please enter 10 digit contact number")
                                        continue
                                    break

                                while True:
                                    subject1 = input("Please enter a subject: ")    
                                    if subject1.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break  

                                while True:
                                    marks1 = input("Please enter marks: ")
                                    if marks1.isdigit() and marks1 >'100':
                                        pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break
                                
                                while True:
                                    fees1 = input("Enter a fees: ")    
                                    if fees1.isdigit():
                                            pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break

                                while True:        
                                    subject2 = input("Please enter a subject(if any): ")    
                                    if subject2== '':
                                        pass
                                            
                                    if subject2.isalpha():
                                            pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break

                                while True:        
                                    marks2 = input("Please enter marks: ")
                                    if marks2.isdigit() and marks2 >'100':
                                        pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break

                                while True:
                                    fees2 = input("Enter a fees: ")    
                                    if fees2.isdigit():
                                        pass
                                    else:
                                        print("Please enter marks in valid format")
                                        continue
                                    break

                                student_data.update({
                                    student_id: { "student_id": student_id,
                                    "first_name": fnm,
                                    "last_name": lnm,
                                    "contact": contact,
                                    "subject1": subject1,
                                    "marks1": marks1,
                                    "fees1": fees1,
                                    "subject2": subject2,
                                    "marks2": marks2,
                                    "fees2": fees2,
                                    }
                                })
                                
                                a = input("If you want to add more data then press yes otherwise press NO: ")
                                if a.lower() == 'yes':
                                        while True:
                                            student_id2 = input("Enter a student id: ")
                                            if student_id2!=student_id:
                                                break
                                            else:
                                                print("Please enter another student id")
                                                                        
                                        while True:
                                            fnm = input("Enter a First name: ")
                                            if fnm.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break

                                        while True:    
                                            lnm = input("Enter a Last name: ")
                                            if lnm.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break    
                                                    
                                        while True:
                                            contact = input("Please enter contact number: ")
                                            if len(contact) == 10 and contact.isdigit():
                                                pass
                                            else:
                                                print("Please enter 10 digit contact number")
                                                continue
                                            break

                                        while True:
                                            subject1 = input("Please enter a subject: ")    
                                            if subject1.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break  

                                        while True:
                                            marks1 = input("Please enter marks: ")
                                            if marks1.isdigit() and marks1 >'100':
                                                pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break
                                                    
                                        while True:
                                            fees1 = input("Enter a fees: ")    
                                            if fees1.isdigit():
                                                    pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break
                                        while True:        
                                            subject2 = input("Please enter a subject(if any): ")    
                                            if subject2== '':
                                                pass
                                                    
                                            if subject2.isalpha():
                                                    pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break

                                        while True:        
                                            marks2 = input("Please enter marks: ")
                                            if marks2.isdigit() and marks2 >'100':
                                                pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break

                                        while True:
                                            fees2 = input("Enter a fees: ")    
                                            if fees2.isdigit():
                                                pass
                                            else:
                                                print("Please enter marks in valid format")
                                                continue
                                            break

                                        student_data2.update({
                                            student_id2: { "student_id": student_id2,
                                            "first_name": fnm,
                                            "last_name": lnm,
                                            "contact": contact,
                                            "subject1": subject1,
                                            "marks1": marks1,
                                            "fees1": fees1,
                                            "subject2": subject2,
                                            "marks2": marks2,
                                            "fees2": fees2,
                                            }
                                        })               
                                
                            if userinp1 == '2':
                                print("There is no data in the dictionary please add atleast one data")
                                print('')
                                print(counsellor_option(student_data, student_data2))
                            
                            if userinp1 == '3':
                                print("There is no data in the dictionary please add atleast one data")
                                print('')
                                print(counsellor_option(student_data, student_data2))

                        else:
                            print("Please enter number only")
                            continue
                        break

                    def back_menu():    
                        backmenu = input("If you want to go back to the previous menu then press back: ")
                        if backmenu == 'back':
                            print("")
                            print("\t1.Add student")
                            print("\t2.Remove student")
                            print("\t3.View all student")
                            print("\t4.View specific student")
                            print("")

                            c = input("Please select your next function: ")
                            
                            if c == '1':
                                print(counsellor_option(student_data, student_data2))
                                print(back_menu())
                            elif c == '2':
                                A = input("Please provide the student id: ")
                                if A == '1':
                                    student_data.clear()
                                    print("Data is successfully deleted.")
                                    print(back_menu())
                                    
                                if A == '2':
                                    student_data2.clear()    
                                    print("Data is successfully deleted.")
                                    print(back_menu())
                            
                            elif c == '3':
                                print("Contents of student id 1:")
                                print(student_data)

                                print("\nContents of 'student id 2:")
                                print(student_data2)
                                print(back_menu())

                            elif c == '4':
                                view = input("Please enter student id: ")
                                if view == '1':
                                    print("Contents of student id 1:")
                                    print(student_data)
                                    print(back_menu())
                                elif view == '2':
                                    print("\nContents of 'student id 2:")
                                    print(student_data2)
                                    print(back_menu())
                        else:
                            pass
                    back_menu()
                student_data = {}
                student_data2 = {}
                counsellor_option(student_data, student_data2)

            elif userinp == '2':
                print('')
                print("\t1.Add marks to student")
                print("\t2.View all students")
                print('')

                def faculty_option(student_data, student_data2):
                    userinp2 = input("Please select from above number: ")
                    if userinp2 == '1':
                        add = input(("Please enter student id: "))
                        if add == '1' or '2':
                            # print("There is no data in the dictionary please add atleast one data")
                            print('')
                            while True:
                                student_id = input("Enter a student id: ")
                                if student_id in student_id:
                                    break
                                else:
                                    print("Please enter another student id")

                            while True:
                                    fnm = input("Enter a First name: ")
                                    if fnm.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break

                            while True:    
                                    lnm = input("Enter a Last name: ")
                                    if lnm.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break    
                                
                            while True:
                                    contact = input("Please enter contact number: ")
                                    if len(contact) == 10 and contact.isdigit():
                                        pass
                                    else:
                                        print("Please enter 10 digit contact number")
                                        continue
                                    break

                            while True:
                                    subject1 = input("Please enter a subject: ")    
                                    if subject1.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break  

                            while True:
                                    marks1 = input("Please enter marks: ")
                                    if marks1.isdigit() and marks1 >'100':
                                        pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break
                                
                            while True:
                                    fees1 = input("Enter a fees: ")    
                                    if fees1.isdigit():
                                            pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break

                            while True:        
                                    subject2 = input("Please enter a subject(if any): ")    
                                    if subject2== '':
                                        pass
                                            
                                    if subject2.isalpha():
                                            pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break

                            while True:        
                                    marks2 = input("Please enter marks: ")
                                    if marks2.isdigit() and marks2 >'100':
                                        pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break

                            while True:
                                    fees2 = input("Enter a fees: ")    
                                    if fees2.isdigit():
                                        pass
                                    else:
                                        print("Please enter marks in valid format")
                                        continue
                                    break

                            student_data.update({
                                    student_id: { "student_id": student_id,
                                    "first_name": fnm,
                                    "last_name": lnm,
                                    "contact": contact,
                                    "subject1": subject1,
                                    "marks1": marks1,
                                    "fees1": fees1,
                                    "subject2": subject2,
                                    "marks2": marks2,
                                    "fees2": fees2,
                                    }
                                })

                            a = input("If you want to add more data then press yes otherwise press NO: ")
                            if a.lower() == 'yes':
                                        while True:
                                            student_id2 = input("Enter a student id: ")
                                            if student_id2!=student_id:
                                                break
                                            else:
                                                print("Please enter another student id")
                                        while True:
                                            fnm = input("Enter a First name: ")
                                            if fnm.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break

                                        while True:    
                                            lnm = input("Enter a Last name: ")
                                            if lnm.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break    
                                                    
                                        while True:
                                            contact = input("Please enter contact number: ")
                                            if len(contact) == 10 and contact.isdigit():
                                                pass
                                            else:
                                                print("Please enter 10 digit contact number")
                                                continue
                                            break

                                        while True:
                                            subject1 = input("Please enter a subject: ")    
                                            if subject1.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break  

                                        while True:
                                            marks1 = input("Please enter marks: ")
                                            if marks1.isdigit() and marks1 >'100':
                                                pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break
                                                    
                                        while True:
                                            fees1 = input("Enter a fees: ")    
                                            if fees1.isdigit():
                                                    pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break
                                        while True:        
                                            subject2 = input("Please enter a subject(if any): ")    
                                            if subject2== '':
                                                pass
                                                    
                                            if subject2.isalpha():
                                                    pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break

                                        while True:        
                                            marks2 = input("Please enter marks: ")
                                            if marks2.isdigit() and marks2 >'100':
                                                pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break

                                        while True:
                                            fees2 = input("Enter a fees: ")    
                                            if fees2.isdigit():
                                                pass
                                            else:
                                                print("Please enter marks in valid format")
                                                continue
                                            break

                                        student_data2.update({
                                            student_id2: { "student_id": student_id2,
                                            "first_name": fnm,
                                            "last_name": lnm,
                                            "contact": contact,
                                            "subject1": subject1,
                                            "marks1": marks1,
                                            "fees1": fees1,
                                            "subject2": subject2,
                                            "marks2": marks2,
                                            "fees2": fees2,
                                            }
                                        })

                        print("Data is successfully added")
                        add_marks = input("Please enter student id: ")
                        if add_marks in student_data:
                            student_info = student_data[add_marks]
                            marks1 = student_info.get("marks1", "")
                            marks2 = student_info.get("marks2", "")
                            print("1.",subject1, ":", marks1)
                            print("2.",subject2, ":", marks2)
                            
                            add_marks_subject = input("Please provide the number of the subject: ")
                            if add_marks_subject == '1':
                                print("")
                                updated_marks = input("Please provide the updated marks: ")
                                student_data[add_marks]["marks1"] = updated_marks
                                print("Updated student_data:")
                                print(student_data)
                            elif add_marks_subject == '2':
                                updated_marks = input("Please provide the updated marks: ")
                                student_data[add_marks]["marks2"] = updated_marks
                                print("")
                                print("Updated student_data:")
                                print(student_data)

                        elif add_marks in student_data2:
                            student_info = student_data2[add_marks]
                            marks1 = student_info.get("marks1", "")
                            marks2 = student_info.get("marks2", "")
                            print("1.",subject1, ":", marks1)
                            print("2.",subject2, ":", marks2)
                            
                            add_marks_subject = input("Please provide the number of the subject: ")
                            if add_marks_subject == '1':
                                print("")
                                updated_marks = input("Please provide the updated marks: ")
                                student_data2[add_marks]["marks1"] = updated_marks
                                print("Updated student_data:")
                                print(student_data2)
                                
                            elif add_marks_subject == '2':
                                updated_marks = input("Please provide the updated marks: ")
                                student_data2[add_marks]["marks2"] = updated_marks
                                print("")
                                print("Updated student_data:")
                                print(student_data2)

                    elif userinp2 == '2':
                        print("There is no data in the dictionary please add atleast one data")
                        print('')
                        while True:
                                student_id = input("Enter a student id: ")
                                if student_id in student_id:
                                    break
                                else:
                                    print("Please enter another student id")

                        while True:
                                    fnm = input("Enter a First name: ")
                                    if fnm.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break

                        while True:    
                                    lnm = input("Enter a Last name: ")
                                    if lnm.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break    
                                
                        while True:
                                    contact = input("Please enter contact number: ")
                                    if len(contact) == 10 and contact.isdigit():
                                        pass
                                    else:
                                        print("Please enter 10 digit contact number")
                                        continue
                                    break

                        while True:
                                    subject1 = input("Please enter a subject: ")    
                                    if subject1.isalpha():
                                        pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break  

                        while True:
                                    marks1 = input("Please enter marks: ")
                                    if marks1.isdigit() and marks1 >'100':
                                        pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break
                                
                        while True:
                                    fees1 = input("Enter a fees: ")    
                                    if fees1.isdigit():
                                            pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break

                        while True:        
                                    subject2 = input("Please enter a subject(if any): ")    
                                    if subject2== '':
                                        pass
                                            
                                    if subject2.isalpha():
                                            pass
                                    else:
                                        print("Please enter alphabetic charcters only")
                                        continue
                                    break

                        while True:        
                                    marks2 = input("Please enter marks: ")
                                    if marks2.isdigit() and marks2 >'100':
                                        pass
                                    else:
                                        print("Please eenter marks in valid format")
                                        continue
                                    break

                        while True:
                                    fees2 = input("Enter a fees: ")    
                                    if fees2.isdigit():
                                        pass
                                    else:
                                        print("Please enter marks in valid format")
                                        continue
                                    break

                        student_data.update({
                                    student_id: { "student_id": student_id,
                                    "first_name": fnm,
                                    "last_name": lnm,
                                    "contact": contact,
                                    "subject1": subject1,
                                    "marks1": marks1,
                                    "fees1": fees1,
                                    "subject2": subject2,
                                    "marks2": marks2,
                                    "fees2": fees2,
                                    }
                                })

                        a = input("If you want to add more data then press yes otherwise press NO: ")
                        if a.lower() == 'yes':
                            while True:
                                            student_id2 = input("Enter a student id: ")
                                            if student_id2!=student_id:
                                                break
                                            else:
                                                print("Please enter another student id")
                            while True:
                                            fnm = input("Enter a First name: ")
                                            if fnm.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break

                            while True:    
                                            lnm = input("Enter a Last name: ")
                                            if lnm.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break    
                                                    
                            while True:
                                            contact = input("Please enter contact number: ")
                                            if len(contact) == 10 and contact.isdigit():
                                                pass
                                            else:
                                                print("Please enter 10 digit contact number")
                                                continue
                                            break

                            while True:
                                            subject1 = input("Please enter a subject: ")    
                                            if subject1.isalpha():
                                                pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break  

                            while True:
                                            marks1 = input("Please enter marks: ")
                                            if marks1.isdigit() and marks1 >'100':
                                                pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break
                                                    
                            while True:
                                            fees1 = input("Enter a fees: ")    
                                            if fees1.isdigit():
                                                    pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break
                            while True:        
                                            subject2 = input("Please enter a subject(if any): ")    
                                            if subject2== '':
                                                pass
                                                    
                                            if subject2.isalpha():
                                                    pass
                                            else:
                                                print("Please enter alphabetic charcters only")
                                                continue
                                            break

                            while True:        
                                            marks2 = input("Please enter marks: ")
                                            if marks2.isdigit() and marks2 >'100':
                                                pass
                                            else:
                                                print("Please eenter marks in valid format")
                                                continue
                                            break

                            while True:
                                            fees2 = input("Enter a fees: ")    
                                            if fees2.isdigit():
                                                pass
                                            else:
                                                print("Please enter marks in valid format")
                                                continue
                                            break

                            student_data2.update({
                                student_id2: { "student_id": student_id2,
                                "first_name": fnm,
                                "last_name": lnm,
                                "contact": contact,
                                "subject1": subject1,
                                "marks1": marks1,
                                "fees1": fees1,
                                "subject2": subject2,
                                "marks2": marks2,
                                "fees2": fees2,
                                }
                            })

                            print("")    
                            print("Contents of student id 1:")
                            print(student_data)
                            print("")
                            print("\nContents of 'student id 2:")
                            print(student_data2)
                            print("")

                    def back_menu2():
                        back_menu2 = input("Please enter back to go back to the previous menu: ")
                        if back_menu2 == 'back':
                            print("")
                            print("\t1.Add marks to student")
                            print("\t2.View all student")
                            print("")
                            
                            d = input("Please select your next function: ")
                            if d == '1':
                                print(faculty_option(student_data,student_data2))
                            elif d == '2':
                                print("")    
                                print("Contents of student id 1:")
                                print(student_data)
                                print("")
                                print("\nContents of 'student id 2:")
                                print(student_data2)
                                print("")
                                print(back_menu2())
                    back_menu2()
                student_data = {}
                student_data2 = {}
                faculty_option(student_data, student_data2)

            elif userinp == '3':
                print("")
                print("\t1.Admissions")
                print("\t2.Hostel facility")
                print("\t3.Transportation facility")
                print("")

                s = input("Please select your function: ")
                if s == '1':
                    print("")
                    while True:
                        name = input("Please enter your full name: ")
                        if name.isalpha():
                            break
                        else:
                            print("Please enter alphabets only")
                    
                    while True:
                        contact = input("Please enter your contact number: ")
                        if len(contact) == 10 and contact.isdigit():
                            break
                        else:
                            print("Please enter 10 digit contact number")

                    while True:
                        city = input("Please enter your city: ")
                        if city.isalpha():
                            break
                        else:
                            print("Please enter alphabets only")
                    
                    while True:
                        educational_qualification = input("Please enter your latest educational qualification: ")
                        if educational_qualification.isalpha():
                            break
                        else:
                            print("Please enter alphabets only")
                    
                    while True:
                        course = input("Please enter the course you are applying for: ")
                        if course.isalpha():
                            break
                        else:
                            print("Please enter alphabets only")
                    
                    print("")
                    print("Thank you for your response your data has been stored in our system successfully.")

                elif s == '2':
                    print("")
                    print("\t1.Air conditioning room (Single occupancy)")
                    print("\t2. Non-Air conditioning room (Single occupancy)")
                    print("")

                    while True:
                        hostel = input("Please enter your choice: ")
                        if hostel == '1':
                            print("")
                            print("\tPer Annum Fee : 1,60,000/-")
                            print("\tRegistration Fee: 5,000/-")
                            print("\t1st Intallment at the time of admission: 1,01,000/-")
                            print("\t2nd Installment: 64,000/-")
                            print("")

                        elif hostel == '2':
                            print("")
                            print("\tPer Annum Fee : 1,15,000/-")
                            print("\tRegistration Fee: 5,000/-")
                            print("\t1st Intallment at the time of admission: 74,000/-")
                            print("\t2nd Installment: 46,000/-")
                            print("")

                        else:
                            print("Please enter proper response")
                        break

                elif s == '3':
                    print("")
                    print("\tBus")
                    print("\tPer Annum Fee: 42,000/-")
                    print("\t1st Installment: 25,000/-")
                    print("\t2nd Installment: 17,000/-")
                    print("")

            def back_menu3():
                    while True:
                        back_menu3 = input("Please enter back to go back to the previous menu: ")
                        if back_menu3 == 'back':
                            print("")
                            print("\t1.Admissions")
                            print("\t2.Hostel facility")
                            print("\t3.Transportation facility")
                            print("")

                            back = input("Please enter your choice: ")
                            if back == '1':
                                print("")
                                while True:
                                    name = input("Please enter your full name: ")
                                    if name.isalpha():
                                        break
                                    else:
                                        print("Please enter alphabets only")
                                
                                while True:
                                    contact = input("Please enter your contact number: ")
                                    if len(contact) == 10 and contact.isdigit():
                                        break
                                    else:
                                        print("Please enter 10 digit contact number")

                                while True:
                                    city = input("Please enter your city: ")
                                    if city.isalpha():
                                        break
                                    else:
                                        print("Please enter alphabets only")
                                
                                while True:
                                    educational_qualification = input("Please enter your latest educational qualification: ")
                                    if educational_qualification.isalpha():
                                        break
                                    else:
                                        print("Please enter alphabets only")
                                
                                while True:
                                    course = input("Please enter the course you are applying for: ")
                                    if course.isalpha():
                                        break
                                    else:
                                        print("Please enter alphabets only")
                                
                                print("")
                                print("Thank you for your response your data has been stored in our system successfully.")

                                print(back_menu3())
                                back_menu3()    
                            
                            elif back == '2':
                                print("")
                                print("\t1.Air conditioning room (Single occupancy)")
                                print("\t2. Non-Air conditioning room (Single occupancy)")
                                print("")

                                while True:
                                    hostel = input("Please enter your choice: ")
                                    if hostel == '1':
                                        print("")
                                        print("\tPer Annum Fee : 1,60,000/-")
                                        print("\tRegistration Fee: 5,000/-")
                                        print("\t1st Intallment at the time of admission: 1,01,000/-")
                                        print("\t2nd Installment: 64,000/-")
                                        print("")

                                    elif hostel == '2':
                                        print("")
                                        print("\tPer Annum Fee : 1,15,000/-")
                                        print("\tRegistration Fee: 5,000/-")
                                        print("\t1st Intallment at the time of admission: 74,000/-")
                                        print("\t2nd Installment: 46,000/-")
                                        print("")

                                    else:
                                        print("Please enter proper response")
                                    break
                            
                            elif back == '3':
                                print("")
                                print("\tBus")
                                print("\tPer Annum Fee: 42,000/-")
                                print("\t1st Installment: 25,000/-")
                                print("\t2nd Installment: 17,000/-")
                                print("")
            back_menu3()
            break
        
        else:
            print("Please enter a number only")
            continue
        break

print("Thank you for visiting us!!!!!!")



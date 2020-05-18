import re
class Password:
    def validate():
        while True:
            f = open("mydict.txt", 'r')
            file_data = f.read()
            print("Original Password from mydict.txt file is : ", file_data)
            rev_file_data = file_data[::-1]
            print("Reverse Password from mydict.txt file is : ", rev_file_data)
            password_check = input("Enter Password to validate : ")
            if password_check == file_data and rev_file_data == password_check:
                print("Invalid")
            else:
                if len(password_check) < 8:
                    print("Make sure your password is at lest 8 letters: InValid")
                    break
                elif re.search('[A-Z]', password_check) is None:
                    print("Make sure your password has at least one uppercase letter in it")
                    break
                elif re.search('[a-z]', password_check) is None:
                    print("Make sure your password has at least one lowercase letter in it")
                    break
                elif re.search('[0-9]', password_check) is None:
                    print("Make sure your password has at least one number in it")
                    break
                elif re.search('[\W]', password_check) is None:
                    print("Make sure your password has at least one Special Character in it")
                    break
                else:
                    print("Your password seems fine")
                    break


p = Password
p.validate()
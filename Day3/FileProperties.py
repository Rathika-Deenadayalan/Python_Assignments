import os
import datetime
no_of_lines=0
no_of_letters=0

if os.path.exists("student.dat"):
    with open("student.dat",'r') as file:
        print("File_name: \t\t\t{}".format(os.path.basename("student.dat")))
        print("File Size: \t\t\t{} bytes".format(os.path.getsize("student.dat")))
        for each_line in file:
            no_of_lines=no_of_lines+1
            for letter in each_line:
                no_of_letters=no_of_letters+1
        print("No. of lines: \t\t{}".format(no_of_lines))
        print("No. of letters: \t{}".format(no_of_letters))
        mod_time = os.path.getmtime("student.dat")
        dt_m = datetime.datetime.fromtimestamp(mod_time)
        print("Modification time: \t{}".format(dt_m))

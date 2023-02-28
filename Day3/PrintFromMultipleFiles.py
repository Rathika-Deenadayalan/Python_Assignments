no_of_lines=0
with open('student_comma.dat','r') as File_st_com:
    for each_line in File_st_com:
        each_line=each_line.strip()
        print(each_line)
        no_of_lines=no_of_lines+1

with open('student_semi.dat','r') as File_st_se:
    for each_line in File_st_se:
        each_line = each_line.strip()
        print(each_line)
        no_of_lines = no_of_lines + 1

with open('student_double_semi.dat','r') as File_st_d_se:
    for each_line in File_st_d_se:
        each_line = each_line.strip()
        print(each_line)
        no_of_lines = no_of_lines + 1

print("Total no. of lines: {}",no_of_lines)


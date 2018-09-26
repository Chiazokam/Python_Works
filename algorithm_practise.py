def ls_break(ls):
    new_ls = []
    for i in ls:
        if i == 42:
            return new_ls
        new_ls.append(i)
"""ls = [1, 2, 88, 42, 99]
print(ls_break(ls))"""
#==========================================
def print_ast(n):
    for i in range(1, n + 1):
        print("* " * i)
#print_ast(5)
#==========================================
def print_ast_reverse(n):
    indent = 0
    for i in range((2*n-1), 0, -2):
        print(str(" " * indent) + "* " * i)
        indent += 2
#print_ast_reverse(20)
#==========================================
def count_dec_places(num):
    num_to_str = str(num)
    dot_index = num_to_str.index(".")
    dec_places = len(num_to_str[dot_index+1:])  #Cuts from the decimal and counts lenght of decimal digits
    return(dec_places)
#print(count_dec_places(52.366738954))
#==========================================
def fibo_num(num_limit):
    a = 0
    b = 1
    while a <= num_limit:
        print(a)
        c = a + b
        a = b       #a takes the value of b and is printed in the next loop
        b = c       #b takes the value of c and is used in the next loop.
#fibo_num(56)
#==========================================
def get_binary(num):
    #quotient = num
    binary_string = ""
    while num >= 0:
        remain = num % 2
    #print(remain)
        binary_string = str(remain) + binary_string
        num = num // 2
    binary_num = int(binary_string)
    return (binary_num)
#print(get_binary(20))
#==========================================
def get_binary_gap(num):
    num_to_bin = int(bin(num)[2:]) #Convert num to binary
#==========================================
def count_max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    count_max = 0
    for i in list:
        if i == max:
            count_max += 1
    return count_max
#print(count_max([4, 4, 1, 3, 4, 4]))
#=========================================
def time_converter(twelve_hour):
    twelve_hour_ls = twelve_hour.split(":")
    if twelve_hour_ls[2][2] == "A":
        if twelve_hour_ls[0] == "12":
            hour_time = "00"
        else:
            hour_time = twelve_hour_ls[0]
    elif twelve_hour_ls[2][2] == "P":
        if twelve_hour_ls[0] == "12":
            hour_time = "12"
        else:
            hour_time = str(int(twelve_hour_ls[0]) + 12)
    twelve_hour_ls[0] = hour_time
    seconds_time = []
    seconds_time.append(twelve_hour_ls[2][0])
    seconds_time.append(twelve_hour_ls[2][1])
    twelve_hour_ls[2] = "".join(seconds_time)
    return ":".join(twelve_hour_ls)
#print(time_converter("12:05:45AM"))
#=========================================
def round_grade(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            n = grade
            while n % 5 != 0:
                five_mult = n
                n += 1
            if n - grade < 3:
                rounded_grades.append(n)
            else:
                rounded_grades.append(grade)
    return rounded_grades
#print(round_grade([73, 67, 38, 33]))
#=========================================
def gen_rand(n, nlist):
    import random
    rand_list = list(set([x for x in range(n)]) - set(nlist))
    return (random.choice(rand_list))
#print(gen_rand(100, [x for x in range(20, 95)]))

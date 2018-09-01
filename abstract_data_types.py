
#Define the Stack Class
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

#===========================================================================
#Takes the file and extracts the opening and closing tags from  the html file
def read_file(filename):
    with open(filename,'r') as f:
        reader = f.read()
        file_char = []
        for row in reader:
            if row == '\n' or row == ' ':
                pass
            else:
                file_char.append(row)
        return file_char

#===========================================================================
#Takes the output from read_file function, extracts only the symbols and rearranges them
def remove_unwanted_char(file_char):
    new_symbol_open_string = []
    new_symbol_close_string = []
    for char in file_char:
        if char == "<":
            new_symbol_open_string.append(char)
        elif char == ">":
            new_symbol_close_string.append(char)
    for char in new_symbol_close_string:
        new_symbol_open_string.append(char)
    return new_symbol_open_string

#===========================================================================
#Takes the output from remove_unwanted_char and checks if symbols balance up
def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == "<":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


file_char = read_file('helloworld.html')
new_symbol_open_string = remove_unwanted_char(file_char)
print(par_checker(new_symbol_open_string))

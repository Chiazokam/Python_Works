def reverse_list(ls):
    if len(ls) == 1:
        return ls
    else:
        ls.append(ls.pop())
        reverse_list(ls)
    return new_ls
#lists = [3, 6, 5, 8, 10]
#=========================================
#print(reverse_list(lists))
def reverse_ls(ls):
    if len(ls) == 0:
        return []
    else:
        return [ls[-1]] + reverse_ls(ls[:-1])
lists = [3, 6, 5, 8, 10]
print(reverse_ls(lists))
#===========================================
#print(lists[:-1])
def count_num(num):
    if num == 0:
        return 1
    else:
        return count_num(num-1)

def rev_string(string):
    if len(string) == 0:
        return ""
    else:
        return string[-1] + rev_string(string[:-1])

string ="aibohphobia"
string = "merrywater"
#print(rev_string(string))

"""
n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()"""

def triangulo(n,k):

    if (k == 0) or (k == n):
      retorno = 1
    else:
      retorno = triangulo(n-1, k-1) + triangulo(n-1, k)
    return retorno

#print ("The Pascal's Triangle")
num = int(input('Enter the number of lines: '))
for n in range(0,num):
    for k in range(0,n+1):
        print (triangulo(n, k))
    #print

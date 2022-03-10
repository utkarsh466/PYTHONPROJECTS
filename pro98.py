
def swap(val1,val2):
    a = open(val1,'r')
    a_value=a.read()
    b = open(val2,'r')
    b_value=b.read()
    a_data=str(a_value)
    b_data=str(b_value)
    a = open(val1,'w')
    b = open(val2,'w')
    a.write(b_data)
    b.write(a_data)
    



file1_name = input("Enter first file name:-")    
file2_name = input("Enter second file name:-")    
swap(file1_name,file2_name)
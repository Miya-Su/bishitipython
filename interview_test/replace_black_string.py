#字符串替换空格
#第一种
def replace_black1(string,length):
    if string==None or length<=0:
        return
    black_count=string.count(' ')
    string_length=len(string)
    replaced_length=string_length+2*black_count

    if replaced_length>length:
        return
    string+=[""for i in range(replaced_length-string_length)]
    original_index=string_length-1
    new_index=replaced_length-1

    while new_index !=original_index:
        if string[original_index]==' ':
            new_index-=2
            string[new_index:new_index+3]='%20'
        else:
            string[new_index]=string[original_index]
        new_index-=1
        original_index-=1
#第二种
def replace_black2(string):
    new_string=[]
    for i in string:
        if  i ==' ':
            new_string.append('%20')
        else:
            new_string.append(i)
    print( ''.join(new_string))

test_string="we are happy now"
string_list=list(test_string)
# replace_black1(string_list,100)
# replace_black2(string_list)

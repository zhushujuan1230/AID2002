input_copy_file=input()
copy_file=None
try:
    copy_file=open(input_copy_file,"rb")
except Exception as e:
    print(e)

if copy_file:
    paste_file=open("副本"+ input_copy_file,"wb")
    while True:
        temp=copy_file.read(10)
        if temp:
            paste_file.write(temp)
        else:
            break







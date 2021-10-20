import sys
#add check of argc
def pullData():
    assert len(sys.argv )!=2 , "not correct number of inputs (should be 2 pathes)"
    print(sys.argv)
    fileinp=open(sys.argv[1],'r')
    fileout=open(sys.argv[2],'w')
    for lines in fileinp :
        try:
            arr=lines.replace('\n',"").split(" ")
            print(arr)
            assert (len(arr)==3 and  arr[0].isdigit() and  arr[1]  in "*/+-" and  arr[2].isdigit()),"The exspression is not in the right format of digit space operator space digit"
            if (arr[1]  is '*' ):
                fileout.write("%s * %s = %d\n"%(arr[0] , arr[2],int(arr[2])*int(arr[0])))
            if (arr[1] is '/'):
                fileout.write("%s / %s = %d\n"%(arr[0], arr[2], int(arr[0]) / int(arr[2])))
            if (arr[1] is '+'):
                fileout.write("%s + %s = %d\n"%(arr[0], arr[2], int(arr[2]) + int(arr[0])))
            if (arr[1] is '-'):
                fileout.write("%s - %s = %d\n"%(arr[0], arr[2], int(arr[0]) - int(arr[2])))
        except Exception as  error:
            fileout.write(str(error)+'\n')


pullData()
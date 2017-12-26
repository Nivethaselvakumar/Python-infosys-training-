def string_test(s):
    d={"UPPER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    

string_test('The quick Brow Fox')

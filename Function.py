#Functions
def double_it(number):
    return 2 * number   #double_it(number)

print double_it(2)
print double_it(3.5)
print double_it("hello")

#part 2
def calc_hypo(a,b):
    hypo = (a**2 + b**2)**0.5
    return hypo

print calc_hypo(3, 4)

#part 3
def calc_hypo(a,b):
    hypo = (a**2 + b**2)**0.5
    return hypo

result = calc_hypo(3, 4)

if type(result)== int:
    print "CORRECT"

elif type(result) == float:
    print "not correct"

else:
    print "all is good"


#part 4 for and b not(!=) an interger
def calc_hypo(a,b):
    if type(a) != int and type(a) != float:
        print "not true a "
        return False 
    if type(b) != int and type(b) != float:
        print "not true for b"   
        return False 

    if a >=0 and b <=0:
        hypo = (a**2 + b**2)**0.5
        return hypo
    else:
       return false

result = calc_hypo(0, -1)
result = calc_hypo("hello","fine")

print result



    


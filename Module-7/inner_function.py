# function is a first class object
def double_dacker():
    print('Starting the double dacker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun

print(double_dacker())
print(double_dacker()())

def do_something(work):
    print('work started')
    # print(work)
    work() #function parameter
    print('work ended')

# do_something(2)
# do_something('i am busy')
def coding():
    print('Coding in python')

# do_something(coding)

def sleeping():
    print('sleeping and dreaming in python')

do_something(sleeping)


# in,is,is not,not,not in
# >,<,>=,<=,==,!==
# and,or

a=2
boss=False
if a>5:
    print('Dalia')
elif a>3:
    print('Akter')
elif a==2:
    print('equal equal')
else:
    print('Bilkis')

# if boss is True:
#     print('tel er bakso ni astechi')
# else:
#     print('lunch er por asen')


if boss is not True:
    print('lunch er por asen')
else:
    print('tel er bakso ni astechi')


coin='head'
# nested conditions
if boss==True:
    print('boss you are joss')
    if coin=='tail':
        print('batting')
    else:
        print('bowling')
        if 5>2 or boss !=True:
            print('do something')
            if 8%2==0 and 5%2==1:
                print('even')
else:
    print('you are loss not a boss')

    
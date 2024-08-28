for cook in range(0,20+1):
    for hen in range(0,33+1):
        for biddy in range(3,99+1):
            if(5*cook+3*hen+biddy/3)==100:
                if(cook+hen+biddy)==100:
                    if biddy%3==0:
                        print("公鸡：",cook,"母鸡：",hen,"小鸡：",biddy)
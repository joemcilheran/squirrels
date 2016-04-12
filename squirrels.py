def sqirrelplaytest():
    squirrel_play = input("What is the temperature? \n")
    squirrel_play = int(squirrel_play)
    is_summer = input("is it summer? \n")
    if (is_summer == "yes"):
        is_summer = "True"
    else:
        is_summer = "False"    
    if (squirrel_play < 60) or (squirrel_play > 100):
        print("False")
    elif (squirrel_play > 90) and (is_summer == "False"):
        print("False")
    else:
        print("True")
sqirrelplaytest()

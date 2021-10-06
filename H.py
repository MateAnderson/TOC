M= input()
x= input()
output = Halting_decider_function(M,x)
if(output == Halt):
    Print(Halt)
    while(true):
        # do noting and
        # Run For Ever
if(output == RunForEver):
    Print(RunForEver)
    # and then Halt and exit from program
    return 1

#definition of a Function
def Halting_decider_function(M,x):
    # State can be Halt or loopforever
    State = null
    # \* do some work
    #      for finding out
    #              the state *\
    if(State == Halt):
        return Halt
    if(State == RunForEver):
        return RunForEver

    #end of function

     

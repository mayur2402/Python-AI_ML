def filterV2(Task,Elements):
    Result = []
    for no in Elements:
        if(Task(no) == True):
            Result.append(no)

    return Result

def mapV2(Task,Elements):
    Result = []
    for no in Elements:
        Result.append(Task(no))
    return Result

def reduceV2(Task,Elements):
    Result = 0
    for no in Elements:
        Result = Task(Result,no)
    return Result

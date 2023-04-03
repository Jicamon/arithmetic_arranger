def check_syntax(problem):

    try:
        firstOperator = int(problem[0])
        secondOperator = int(problem[2])
    except:
        return -1

    sign = problem[1]

    if firstOperator > 9999 or firstOperator < 0 or secondOperator > 9999 or secondOperator < 0:
        return -2

    if sign != '+' and sign != '-': return -3

    return 0


def problemSeparator(problem):
    separatedProblem = problem.split()
    return separatedProblem


def calculateResult(sections):
    fOp = int(sections[0])
    sign = sections[1]
    sOp = int(sections[2])

    if sign == '+':
        return fOp + sOp
    else:
        return fOp - sOp


def problem_arranger(fOperators, sOperators, signs, results, withResults):
    arrangedProblems = ''
    fLine = ''
    sLine = ''
    dLine = ''
    rLine = ''

    for x in range(len(fOperators)):
        fLine = fLine + '{:>7}'.format(str(fOperators[x])) + "\t"
        sLine = sLine + '{:>2} {:>4}'.format(signs[x], sOperators[x]) + "\t"
        dLine = dLine + '{:>7}'.format('------') + "\t"
        rLine = rLine + '{:>7}'.format(str(results[x])) + "\t"
        #arrangedProblems = arrangedProblems + f'{str(fOperators[x]):> 6}' + "\t\t"

    arrangedProblems = arrangedProblems + fLine + '\n' + sLine + '\n' + dLine 

    if withResults is True:
        arrangedProblems = arrangedProblems + '\n' + rLine

    return arrangedProblems


def arithmetic_arranger(problems, withResult):
    fOperators = list()
    sOperators = list()
    signs = list()
    results = list()
    hasErrors = False

    arranged_problems = list()
    errors = list()
    i = 1

    for problem in problems:

        sections = problemSeparator(problem)

        syntaxCheck = check_syntax(sections)

        if syntaxCheck == -1:
            errors.append(["Error: Numbers must only contain digits.", i])
        elif syntaxCheck == -2:
            errors.append(["Error: Numbers cannot be more than four digits.", i])
        elif syntaxCheck == -3:
            errors.append(["Error: Operator must be '+' or '-'.", i])

        if len(errors) > 5:        
            return "Error: Too many problems."

        if len(errors) > 0:
            hasErrors = True
            

        if syntaxCheck == 0:
            fOperators.append(sections[0])
            sOperators.append(sections[2])
            signs.append(sections[1])
            results.append(calculateResult(sections))

        arranged_problems = problem_arranger(fOperators, sOperators, signs, results, withResult)

        i += 1

    if hasErrors :
        return errors

    return arranged_problems

print(arithmetic_arranger(["9999 + 9999", "9999 - 9999", "1 + 1", "1 - 1", "9999 + 1"], True))
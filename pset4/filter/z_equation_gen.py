from fractions import Fraction
import sympy
import numbers
import fractions
import math
import random
import sympy as sp

# prerequisite imports and modules---------------------------------
import sympy as sp
import random

def One_step_Equations_With_Integers_1(option_difficulty):
    problemsets = ""
    answerset = ""
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    temp = random.choice([1, 2, 3])
    variables = []
    variable_values = []
    numerals = []
    pass_loop = False
    unique = []

    print('temp:',temp)
    if temp == 1:
        variables.append(random.choice(choices))
        sym_1 = random.choice(addition_expression)
        numerals.append(str(random.randint(2, 10))) if option_difficulty=="easy" else (numerals.append(str(random.randint(2, 30))) if option_difficulty=="medium" else numerals.append(str(random.randint(20, 50))))
        numerals.append(str(random.choice(negative))+str(random.randint(1, 10))) if option_difficulty=="easy" else (numerals.append(str(random.choice(negative))+str(random.randint(1, 60))) if option_difficulty=="medium" else numerals.append(str(random.choice(negative))+str(random.randint(20, 90))))
        x = sp.symbols(str(variables[0]))
        output = '{} {} {}'.format(str(variables[0]), sym_1, str(numerals[0])) if random.randint(1,2) == 1 else '{} {} {}'.format(str(numerals[0]), sym_1, str(variables[0]))
        other = '{}'.format(str(numerals[1]))
        equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

        problemsets = sp.latex(equation)
        answerset = sp.solve(equation, x)

    elif temp == 2:
        while pass_loop == False:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            problemsets=""
            answerset=""
            variables.append(random.choice(choices))
            variable_values.append(str(random.choice(negative)) + str(random.randint(2,10))) if option_difficulty=="easy" or option_difficulty=="medium" else variable_values.append(str(random.choice(negative)) + str(random.randint(5,15)))
            for i in range(1, int(abs(int(variable_values[0])) / 2) + 1):
                if int(abs(int(variable_values[0]))) % i == 0:
                    if i not in unique:
                        unique.append(i)
                    if int(abs(int(variable_values[0]))/i) not in unique:
                        unique.append(int(abs(int(variable_values[0])) / i))
            holder = random.choice(unique[1:])

            randomized = holder * random.randint(5, 10) if option_difficulty=="easy" else (holder * random.randint(5, 15) if option_difficulty=="medium" else holder * random.randint(10, 20))
            if randomized % int(variable_values[0]) != 0:
                randomized = randomized + (randomized % int(variable_values[0]))
            numerals.append(str(random.choice(negative)) + str(randomized))

            x = sp.symbols(str(variables[0]))

            output, other = '{}*{}'.format(str(variable_values[0]), str(variables[0])), '{}'.format(str(numerals[0]))
            equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets, answerset = sp.latex(equation), sp.solve(equation, x)

            output = str(answerset)

            output = output.replace('[', ''); output = output.replace(']', '')
            pass_loop = sp.sympify(output).is_integer

    elif temp == 3:
        variables.append(random.choice(choices))
        variable_values.append(str(random.choice(negative))+str(random.randint(2,10))) if option_difficulty=="easy" or option_difficulty=="medium" else variable_values.append(str(random.choice(negative))+str(random.randint(5,15)))
        numerals.append(str(random.choice(negative))+str(random.randint(2,15))) if option_difficulty=="easy" else (numerals.append(str(random.choice(negative))+str(random.randint(2,60))) if option_difficulty=="medium" else numerals.append(str(random.choice(negative))+str(random.randint(20,90))))

        x = sp.symbols(str(variables[0]))

        output, other = '{} / {}'.format(str(variables[0]), str(variable_values[0])), '{}'.format(str(numerals[0]))
        equation  = sp.Eq(sp.sympify(output), sp.sympify(other))

        problemsets, answerset = sp.latex(equation), sp.solve(equation, x)
    return(problemsets, answerset)
for i in range(20):
    a,b = One_step_Equations_With_Integers_1("easy")
    print(a,b)
for i in range(20):
    a,b = One_step_Equations_With_Integers_1("medium")
    print(a,b)
for i in range(20):
    a,b = One_step_Equations_With_Integers_1("hard")
    print(a,b)



    #------!!


def decimal_generator():
    integer_only = random.randint(1, 9)
    decimal = random.random()
    problem = "{:.1f}".format(integer_only + decimal) if integer_only % 2 == 0 else "{:.2f}".format(integer_only + decimal)
    return(problem)


def truncate(n):
    return int(round(n, 4) * 1000) / 1000


def find_replace(sent, replace, var, var_val):
    return sent.replace(replace, r'\frac{' + var + '}{' + var_val + '}')


def One_step_Equations_With_Decimals_1(temp=None):
    problemsets = ''
    answerset = ''
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    sym_1 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''
    other = ''
    equation = ''
    pass_loop = False
    holder = ''
    if temp==None:
        temp=random.choice([1, 2, 3])

    hip = ''
    print('temp:', temp)

    if temp == 1:
        variables.append(random.choice(choices))
        sym_1 = random.choice(addition_expression)
        numerals.append(str(decimal_generator()))
        numerals.append(str(random.choice(negative)) +
                        str(decimal_generator()))

        x = sp.symbols(str(variables[0]))

        if random.randint(1, 2) == 1:
            output = '{} {} {}'.format(
                str(variables[0]), sym_1, str(numerals[0]))
        else:
            output = '{} {} {}'.format(
                str(numerals[0]), sym_1, str(variables[0]))
        other = '{}'.format(str(numerals[1]))
        equation = sp.Eq(sp.sympify(output), sp.sympify(other))
        hip = sp.solve(equation, x)
        hip = str(hip)
        hip = hip.replace('[', '')
        hip = hip.replace(']', '')
        problemsets = sp.latex(equation)
        answerset = sp.N(hip, chop=True)

    elif temp == 2:
        while pass_loop == False:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            variables.append(random.choice(choices))
            variable_values.append(
                str(random.choice(negative)) + str(decimal_generator()))
            numerals.append(str(random.choice(negative)) +
                            str(decimal_generator()))

            x = sp.symbols(str(variables[0]))

            output = '{}*{}'.format(
                str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')

            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

            pass_loop = sp.sympify(hip).is_rational

    elif temp == 3:
        while pass_loop == False:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            variables.append(random.choice(choices))
            variable_values.append(
                str(random.choice(negative)) + str(decimal_generator()))
            numerals.append(str(random.choice(negative)) +
                            str(decimal_generator()))

            x = sp.symbols(str(variables[0]))

            output = '{} / {}'.format(str(variables[0]),
                                        str(variable_values[0]))
            other = '{}'.format(str(numerals[0]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            holder = output + ' = ' + other

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = find_replace(holder, output, str(
                variables[0]), str(variable_values[0]))
            answerset = sp.N(hip, chop=True)

            pass_loop = sp.sympify(hip).is_rational

    if len(str(float(answerset))) > 12:
        print("REDID")
        One_step_Equations_With_Decimals_1(temp)
    else:
        print(float(answerset))
        return(problemsets, float(answerset))

for i in range(20):
    a, b = One_step_Equations_With_Decimals_1()
    #print(a, b)

#-----




def decimal_generator(option_difficulty):
    problem = ""
    integer_only = 0
    decimal = 0.0
    decimal_2 = 0.0
    if option_difficulty == "easy":
        integer_only = random.randint(1, 9)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.1f}".format(integer_only + decimal)
        else:
            problem = "{:.2f}".format(integer_only + decimal)

    elif option_difficulty == "medium":
        integer_only = random.randint(1, 99)
        decimal = random.random()
        decimal_2 = "{:.2f}".format(decimal)
        if integer_only % 2 == 0:
            if (float(decimal_2) * 100) % 2 == 0:
                problem = "{:.1f}".format(integer_only + float(decimal))
            elif int(str(decimal_2 * 100)[:1]) % 3 == 0:
                problem = "{:.4f}".format(integer_only + float(decimal))
            else:
                problem = "{:.2f}".format(integer_only + float(decimal))
        else:  # add one more (ten thousandth place) if the front is divisible by 2
            problem = "{:.3f}".format(integer_only + float(decimal))

    elif option_difficulty == "hard":
        integer_only = random.randint(10, 100)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.6f}".format(integer_only + decimal)
        else:
            problem = "{:.5f}".format(integer_only + decimal)
            # will have two cutt off points
    return(problem)


def truncate(n):
    return int(round(n, 4) * 1000) / 1000


def find_replace(sent, replace, var, var_val):
    return sent.replace(replace, r'\frac{' + var + '}{' + var_val + '}')


def One_step_Equations_With_Decimals_1(option_difficulty, option_random):
    problemsets = ''
    answerset = ''
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2, 3]
    negative = ['-', '']
    temp = random.choice(case)
    sym_1 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''
    other = ''
    equation = ''
    pass_loop = False
    holder = ''

    hip = ''
    print('temp:', temp)

    if option_difficulty == "easy":
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(decimal_generator("easy")))
            numerals.append(str(random.choice(negative)) +
                            str(decimal_generator("easy")))

            x = sp.symbols(str(variables[0]))

            if random.randint(1, 2) == 1:
                output = '{} {} {}'.format(
                    str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(
                    str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("easy")))

                x = sp.symbols(str(variables[0]))

                output = '{}*{}'.format(
                    str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')

                problemsets = sp.latex(equation)
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

        elif temp == 3:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("easy")))

                x = sp.symbols(str(variables[0]))

                output = '{} / {}'.format(str(variables[0]),
                                          str(variable_values[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))
                holder = output + ' = ' + other

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = find_replace(holder, output, str(
                    variables[0]), str(variable_values[0]))
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

    elif option_difficulty == "medium":
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(decimal_generator("medium")))
            numerals.append(str(random.choice(negative)) +
                            str(decimal_generator("medium")))

            x = sp.symbols(str(variables[0]))

            if random.randint(1, 2) == 1:
                output = '{} {} {}'.format(
                    str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(
                    str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("medium")))

                x = sp.symbols(str(variables[0]))

                output = '{}*{}'.format(
                    str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')

                problemsets = sp.latex(equation)
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

        elif temp == 3:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("medium")))

                x = sp.symbols(str(variables[0]))

                output = '{} / {}'.format(str(variables[0]),
                                          str(variable_values[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))
                holder = output + ' = ' + other

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = find_replace(holder, output, str(
                    variables[0]), str(variable_values[0]))
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

    elif option_difficulty == "hard":
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(decimal_generator("hard")))
            numerals.append(str(random.choice(negative)) +
                            str(decimal_generator("hard")))

            x = sp.symbols(str(variables[0]))

            if random.randint(1, 2) == 1:
                output = '{} {} {}'.format(
                    str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(
                    str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("hard")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("hard")))

                x = sp.symbols(str(variables[0]))

                output = '{}*{}'.format(
                    str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')

                problemsets = sp.latex(equation)
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

        elif temp == 3:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("hard")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("hard")))

                x = sp.symbols(str(variables[0]))

                output = '{} / {}'.format(str(variables[0]),
                                          str(variable_values[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))
                holder = output + ' = ' + other

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = find_replace(holder, output, str(
                    variables[0]), str(variable_values[0]))
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

    answerset = str(truncate(answerset))
    return(problemsets, answerset)


print("EASY\n\n\n")
for i in range(20):
    a, b = One_step_Equations_With_Decimals_1("easy", False)
    print(a, b)

print("MEDIUM\n\n\n")
for i in range(20):
    a, b = One_step_Equations_With_Decimals_1("medium", False)
    print(a, b)

print("HARD\n\n\n")
for i in range(20):
    a, b = One_step_Equations_With_Decimals_1("hard", False)
    print(a, b)


# First Section


def fraction_generator(option_difficulty):
    problem = ""
    numerator = 4
    denominator = 4
    while float(numerator / denominator) == 1:
        # get rid of 74.90 <--- problem!!! (EDGE 0)
        if option_difficulty == "easy":
            numerator = random.randint(1, 4)
            denominator = random.randint(2, 5)
            problem = fractions.Fraction(numerator, denominator)

        elif option_difficulty == "medium":
            numerator = random.randint(2, 7)
            denominator = random.randint(2, 9)
            problem = fractions.Fraction(numerator, denominator)

        elif option_difficulty == "hard":
            numerator = random.randint(2, 25)
            denominator = random.randint(2, 12)
            problem = fractions.Fraction(numerator, denominator)
    return(problem)


def truncate(n):
    return int(round(n, 4) * 1000) / 1000


def One_step_Equations_With_Fractions_1(option_difficulty, option_random):
    problemsets = ''
    answerset = ''
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2]
    negative = ['-', '']
    temp = random.choice(case)
    sym_1 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''
    other = ''
    equation = ''
    pass_loop = False
    holder = ''

    hip = ''
    print('temp:', temp)

    if option_difficulty == "easy":
        if temp == 1:
            variables.append(random.choice(choices))
            variable_values.append(str(fraction_generator("easy")))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(2, 5)))

            x = sp.symbols(str(variables[0]))

            output = '{} * {}'.format(
                str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            variable_values.append(
                str(random.choice(negative)) + str(fraction_generator("easy")))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(1, 5)))

            x = sp.symbols(str(variables[0]))
            if random.randint(1, 2) == 1:
                output = '{} {} {}'.format(
                    str(variables[0]), sym_1, str(variable_values[0]))
            else:
                output = '{} {} {}'.format(
                    str(variable_values[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            holder = output + ' = ' + other

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

            pass_loop = sp.sympify(hip).is_rational

    elif option_difficulty == "medium":
        if temp == 1:
            variables.append(random.choice(choices))
            variable_values.append(str(fraction_generator("medium")))
            numerals.append(str(random.choice(negative)) +
                            str(fraction_generator("medium")))

            x = sp.symbols(str(variables[0]))

            output = '{} * {}'.format(
                str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(fraction_generator("medium")))
            numerals.append(str(random.choice(negative)) +
                            str(fraction_generator("medium")))

            x = sp.symbols(str(variables[0]))
            if random.randint(1, 2) == 1:
                output = '{} {} {}'.format(
                    str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(
                    str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            holder = output + ' = ' + other

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

    elif option_difficulty == "hard":
        if temp == 1:
            variables.append(random.choice(choices))
            variable_values.append(str(fraction_generator("hard")))
            numerals.append(str(random.choice(negative)) +
                            str(fraction_generator("hard")))

            x = sp.symbols(str(variables[0]))

            output = '{} * {}'.format(
                str(variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[0]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(fraction_generator("hard")))
            numerals.append(str(random.choice(negative)) +
                            str(fraction_generator("hard")))

            x = sp.symbols(str(variables[0]))
            if random.randint(1, 2) == 1:
                output = '{} {} {}'.format(
                    str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(
                    str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            holder = output + ' = ' + other

            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)
    answerset = str(truncate(answerset))
    answerset = sp.latex(sp.sympify(fractions.Fraction(answerset)))
    return(problemsets, answerset)


print("EASY\n\n\n")
for i in range(20):
    a, b = One_step_Equations_With_Fractions_1("easy", False)
    print(a, b)

print("MEDIUM\n\n\n")
for i in range(20):
    a, b = One_step_Equations_With_Fractions_1("medium", False)
    print(a, b)

print("HARD\n\n\n")
for i in range(20):
    a, b = One_step_Equations_With_Fractions_1("hard", False)
    print(a, b)


# First Section


def checker(a, b):
    a = int(a)
    b = int(b)
    if a == b or a % b == 0 or b % a == 0:
        print("------------")
        return False
    return True


def Two_step_Equations_With_Integers_1(option_difficulty='easy', expr='latex'):
    problemsets = []
    answerset = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2]
    negative = ['-', '']
    temp = random.choice(case)
    sym_1 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''
    other = ''
    equation = ''
    pass_loop = False
    unique = []
    holder = 0
    randomized = 0
    print('temp:', temp)
    if option_difficulty == "easy":
        if temp == 1:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                problemsets.clear()
                answerset.clear()
                variables.append(random.choice(choices))
                sym_1 = random.choice(addition_expression)
                numerals.append(str(random.randint(2, 10)))
                numerals.append(str(random.choice(negative)) +
                                str(random.randint(1, 10)))
                numerals.append(str(random.choice(negative)) +
                                str(random.randint(2, 10)))
                x = sp.symbols(str(variables[0]))
                if random.randint(1, 2) == 1:
                    output = '{}*{} {} {}'.format(str(numerals[2]), str(
                        variables[0]), sym_1, str(numerals[0]))
                else:
                    output = '{} {} {}*{}'.format(
                        str(numerals[0]), sym_1, str(numerals[2]), str(variables[0]))
                other = '{}'.format(str(numerals[1]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))

                problemsets.append(sp.latex(equation))
                answerset.append(sp.solve(equation, x))
                pass_loop = sp.sympify(sp.solve(equation, x).pop(0)).is_integer

        elif temp == 2:
            variables.append(random.choice(choices))
            variable_values.append(
                str(random.choice(negative)) + str(random.randint(2, 10)))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(2, 15)))
            numerals.append(str(random.randint(2, 15)))
            sym_1 = random.choice(addition_expression)
            x = sp.symbols(str(variables[0]))

            output = '{} / {} {} {}'.format(str(variables[0]), str(
                variable_values[0]), sym_1, str(numerals[1]))
            other = '{}'.format(str(numerals[0]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))

            problemsets.append(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    elif option_difficulty == "medium":
        if temp == 1:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(1, 40)))

            x = sp.symbols(str(variables[0]))

            output = '({} / {}) * {}'.format(
                str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{}'.format(str(numerals[2]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets.append(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

        elif temp == 2:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(2, 20)))
            numerals.append(str(random.randint(1, 30)))
            numerals.append(str(random.randint(2, 30)))

            x = sp.symbols(str(variables[0]))

            output = '({} / {}) * {}'.format(
                str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{} / {}'.format(str(numerals[2]), str(numerals[3]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets.append(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    elif option_difficulty == "hard":
        if temp == 1:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(30, 60)))

            x = sp.symbols(str(variables[0]))

            output = '({} / {}) * {}'.format(
                str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{}'.format(str(numerals[2]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets.append(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

        elif temp == 2:
            variables.clear()
            variable_values.clear()
            numerals.clear()
            problemsets.clear()
            answerset.clear()
            variables.append(random.choice(choices))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))
            numerals.append(str(random.randint(15, 30)))

            x = sp.symbols(str(variables[0]))

            output = '({} / {}) * {}'.format(
                str(numerals[0]), str(numerals[1]), str(variables[0]))
            other = '{} / {}'.format(str(numerals[2]), str(numerals[3]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets.append(sp.latex(equation))
            answerset.append(sp.solve(equation, x))

    return(problemsets, answerset)


print("EASY")
for i in range(5):
    a, b = Two_step_Equations_With_Integers_1("easy", "latex")
    print(a, b)
print("MEDIUM")
for i in range(5):
    a, b = Two_step_Equations_With_Integers_1("medium", "latex")
    print(a, b)

print("HARD")
for i in range(5):
    a, b = Two_step_Equations_With_Integers_1("hard", "latex")
    print(a, b)


# First Section (NOT DONE YETT)


def decimal_generator(option_difficulty):
    problem = ""
    integer_only = 0
    decimal = 0.0
    decimal_2 = 0.0
    # get rid of 74.90 <--- problem!!! (EDGE 0)
    if option_difficulty == "easy":
        integer_only = random.randint(1, 9)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.1f}".format(integer_only + decimal)
        else:
            problem = "{:.2f}".format(integer_only + decimal)

    elif option_difficulty == "medium":
        integer_only = random.randint(1, 99)
        decimal = random.random()
        decimal_2 = "{:.2f}".format(decimal)
        if integer_only % 2 == 0:
            if (float(decimal_2) * 100) % 2 == 0:
                problem = "{:.1f}".format(integer_only + float(decimal))
            elif int(str(decimal_2 * 100)[:1]) % 3 == 0:
                problem = "{:.4f}".format(integer_only + float(decimal))
            else:
                problem = "{:.2f}".format(integer_only + float(decimal))
        else:  # add one more (ten thousandth place) if the front is divisible by 2
            problem = "{:.3f}".format(integer_only + float(decimal))

    elif option_difficulty == "hard":
        integer_only = random.randint(10, 100)
        decimal = random.random()
        if integer_only % 2 == 0:
            problem = "{:.8f}".format(integer_only + decimal)
        else:
            problem = "{:.7f}".format(integer_only + decimal)
            # will have two cutt off points

    if str(problem)[-2] == "." and str(problem)[-1] == "0":
        problem = problem[:-2]

    return(problem)


def truncate(n):
    return int(n * 10000000000000) / 10000000000000


def Two_step_Equations_With_Decimals_1(option_difficulty='easy', expr='latex'):
    problemsets = ''
    answerset = ''
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    case = [1, 2]
    negative = ['-', '']
    temp = random.choice(case)
    sym_1 = ''
    variables = []
    variable_values = []
    numerals = []
    output = ''
    other = ''
    equation = ''
    pass_loop = False
    holder = ''
    sample = ""

    hip = ''
    print('temp:', temp)

    if option_difficulty == "easy":
        if temp == 1:  # generate divisible number first, then add/subtract
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(decimal_generator("easy")))
                sym_1 = random.choice(addition_expression)
                numerals.append(str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("easy")))

                if sym_1 == "-":
                    sample = float(numerals[1]) + float(numerals[0])
                else:
                    sample = float(numerals[1]) - float(numerals[0])

                holder = float(sample) / float(variable_values[0])
                if len(str(holder)) <= 7:
                    #print(True, len(str(holder)))
                    #print(holder, sample, numerals[1], numerals[0], variable_values[0])
                    pass_loop = True
            if random.randint(1, 2) == 1:
                output = '{} * {} {} {}'.format(str(variable_values[0]), str(
                    variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {} * {}'.format(str(numerals[0]),  sym_1, str(
                    variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets = sp.latex(equation)
            answerset = holder

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                sym_1 = random.choice(addition_expression)
                variable_values.append(str(decimal_generator("easy")))
                numerals.append(str(decimal_generator("easy")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("easy")))

                x = sp.symbols(str(variables[0]))

                output = '({} / {}) {} {}'.format(
                    str(variables[0]), str(variable_values[0]), sym_1, numerals[0])
                other = '{}'.format(str(numerals[1]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = r'\frac{' + str(variables[0]) + '}{' + str(
                    variable_values[0]) + '} ' + sym_1 + ' ' + numerals[0] + ' = ' + numerals[1]
                answerset = truncate(sp.N(hip, chop=True))

                pass_loop = sp.sympify(hip).is_rational

    elif option_difficulty == "medium":
        if temp == 1:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(str(decimal_generator("medium")))
                sym_1 = random.choice(addition_expression)
                numerals.append(str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("medium")))

                if sym_1 == "-":
                    sample = float(numerals[1]) + float(numerals[0])
                else:
                    sample = float(numerals[1]) - float(numerals[0])

                holder = float(sample) / float(variable_values[0])
                if len(str(holder)) <= 7:
                    #print(True, len(str(holder)))
                    #print(holder, sample, numerals[1], numerals[0], variable_values[0])
                    pass_loop = True
            if random.randint(1, 2) == 1:
                output = '{} * {} {} {}'.format(str(variable_values[0]), str(
                    variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {} * {}'.format(str(numerals[0]),  sym_1, str(
                    variable_values[0]), str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            problemsets = sp.latex(equation)
            answerset = holder

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                sym_1 = random.choice(addition_expression)
                variable_values.append(str(decimal_generator("medium")))
                numerals.append(str(decimal_generator("medium")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("medium")))

                x = sp.symbols(str(variables[0]))

                output = '({} {} {})'.format(
                    str(variables[0]), sym_1, str(numerals[0]))
                other = '{}'.format(
                    str(float(numerals[1]) * float(variable_values[0])))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))
                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                problemsets = r'\frac{' + str(variables[0]) + ' ' + sym_1 + ' ' + str(
                    numerals[0]) + '}{' + str(variable_values[0]) + '}' + ' = ' + numerals[1]
                answerset = sp.N(hip, chop=True)
                print(hip, truncate(answerset))
                answerset = truncate(answerset)
                if len(str(answerset)) <= 20:
                    pass_loop = True

    elif option_difficulty == "hard":
        if temp == 1:
            variables.append(random.choice(choices))
            sym_1 = random.choice(addition_expression)
            numerals.append(str(decimal_generator("hard")))
            numerals.append(str(random.choice(negative)) +
                            str(decimal_generator("hard")))

            x = sp.symbols(str(variables[0]))

            if random.randint(1, 2) == 1:
                output = '{} {} {}'.format(
                    str(variables[0]), sym_1, str(numerals[0]))
            else:
                output = '{} {} {}'.format(
                    str(numerals[0]), sym_1, str(variables[0]))
            other = '{}'.format(str(numerals[1]))
            equation = sp.Eq(sp.sympify(output), sp.sympify(other))
            hip = sp.solve(equation, x)
            hip = str(hip)
            hip = hip.replace('[', '')
            hip = hip.replace(']', '')
            problemsets = sp.latex(equation)
            answerset = sp.N(hip, chop=True)

        elif temp == 2:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("hard")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("hard")))

                x = sp.symbols(str(variables[0]))

                output = '{}*{}'.format(
                    str(variable_values[0]), str(variables[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')

                problemsets = sp.latex(equation)
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

        elif temp == 3:
            while pass_loop == False:
                variables.clear()
                variable_values.clear()
                numerals.clear()
                variables.append(random.choice(choices))
                variable_values.append(
                    str(random.choice(negative)) + str(decimal_generator("hard")))
                numerals.append(str(random.choice(negative)) +
                                str(decimal_generator("hard")))

                x = sp.symbols(str(variables[0]))

                output = '{} / {}'.format(str(variables[0]),
                                          str(variable_values[0]))
                other = '{}'.format(str(numerals[0]))
                equation = sp.Eq(sp.sympify(output), sp.sympify(other))

                hip = sp.solve(equation, x)
                hip = str(hip)
                hip = hip.replace('[', '')
                hip = hip.replace(']', '')
                answerset = sp.N(hip, chop=True)

                pass_loop = sp.sympify(hip).is_rational

    answerset = str(answerset)
    return(problemsets, answerset)


"""print("EASY\n\n\n")
for i in range(20):
    a,b = Two_step_Equations_With_Decimals_1("easy", "latex")
    print(a,b)"""

print("MEDIUM\n\n\n")
for i in range(20):
    a, b = Two_step_Equations_With_Decimals_1("medium", "latex")
    print(a, b)
"""print("HARD\n\n\n")
for i in range(20):
    a,b = Two_step_Equations_With_Decimals_1("hard", "latex")
    print(a,b)"""


def integer_1(var=""):
    output = random.randint(1, 20)
    if var == True:
        while int(output) == 1 or int(output) == 0:
            output = random.randint(1, 20)
        return output
    else:
        return output


def integer_2(var=""):
    output = random.randint(-10, 10)
    if var == True:
        while int(output) == 1 or int(output) == 0:
            output = random.randint(-10, 10)
        return output
    else:
        return output


def integer_3(var=""):
    output = random.randint(1, 50)
    if var == True:
        while int(output) == 1 or int(output) == 0:
            output = random.randint(1, 50)
        return output
    else:
        return output


def integer_4(var=""):
    output = random.randint(-50, 50)
    if var == True:
        while int(output) == 1 or int(output) == 0:
            output = random.randint(-50, 50)
        return output
    else:
        return output


def swapper(one, two):
    temp = ""
    temp = str(two)
    two = str(one)
    one = str(temp)
    return(one, two)


def Solving_Multi_Step_Inequalities(option_difficulty='easy', expr='latex'):
    problem = ""
    answer = ""
    temp = ""
    holder = ""

    half_1 = ""
    half_2 = ""

    sym_1 = random.choice(["+", "-"])
    sym_2 = random.choice(["+", "-"])

    var1 = random.choice(['x', 'y', 'a', 'b', 'z', 'p',
                         't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

    if option_difficulty == "easy":
        x = sympy.Symbol(var1)

        if random.randint(1, 2) == 1:
            half_1 = fr'{str(integer_1(True))} * {str(var1)} {str(sym_1)} {str(integer_1(True))} * {str(var1)}'
            half_2 = fr'{str(integer_2())}'
        else:
            half_1 = fr'{str(integer_1(True))} * {str(var1)} {str(sym_1)} {str(integer_1())} {str(sym_2)} {str(integer_1())}'
            half_2 = fr'{str(integer_2())}'

        if random.randint(1, 2) == 1:
            half_1, half_2 = swapper(half_1, half_2)

        if random.randint(1, 2) == 1:
            answer = sympy.latex(sympy.sympify(half_1, evaluate=False), order="none") + \
                r" = " + sympy.latex(sympy.sympify(half_2,
                                     evaluate=False), order="none")
        else:
            answer = sympy.latex(sympy.sympify(half_1, evaluate=False), order="lex") + \
                r" = " + sympy.latex(sympy.sympify(half_2,
                                     evaluate=False), order="lex")
        temp = sympy.Eq(sympy.sympify(half_1), sympy.sympify(half_2))
        holder = sympy.solve(temp, x)

    elif option_difficulty == "medium":
        x = sympy.Symbol(var1)
        rand = random.randint(1, 3)
        if rand == 1:
            half_1 = fr'{str(integer_1(True))} * {str(var1)} {str(sym_1)} {str(integer_1())} {str(sym_2)} {str(integer_1(True))} * {str(var1)}'
            half_2 = fr'{str(integer_2())}'
        elif rand == 2:
            half_1 = fr'{str(integer_1(True))} * ( {str(integer_3(True))} * {str(var1)} {str(sym_1)} {str(integer_3())} {str(sym_2)} {str(integer_1(True))} * {str(var1)} )'
            half_2 = fr'{str(integer_2())}'
        else:
            half_1 = fr'{str(integer_3(True))} * ( {str(integer_3())} {str(sym_1)} {str(integer_3(True))} * {str(var1)} )'
            half_2 = fr'{str(integer_4())}'

        if random.randint(1, 2) == 1:
            half_1, half_2 = swapper(half_1, half_2)

        if random.randint(1, 2) == 1:
            answer = sympy.latex(sympy.sympify(half_1, evaluate=False), order="none") + \
                r" = " + sympy.latex(sympy.sympify(half_2,
                                     evaluate=False), order="none")
        else:
            answer = sympy.latex(sympy.sympify(half_1, evaluate=False), order="lex") + \
                r" = " + sympy.latex(sympy.sympify(half_2,
                                     evaluate=False), order="lex")
        temp = sympy.Eq(sympy.sympify(half_1), sympy.sympify(half_2))
        holder = sympy.solve(temp, x)

    elif option_difficulty == "hard":
        sym_3 = random.choice(["+", "-"])
        x = sympy.Symbol(var1)
        rand = random.randint(1, 3)
        if rand == 1:
            half_1 = fr'{str(integer_3(True))} * {str(var1)} {str(sym_1)} {str(integer_3())} {str(sym_2)} {str(integer_3(True))} * {str(var1)} {str(sym_3)} {str(integer_3(True))} * {str(var1)}'
            half_2 = fr'{str(integer_4())}'
        elif rand == 2:
            half_1 = fr'{str(integer_3(True))} * {str(var1)} {str(sym_1)} {str(integer_3(True))} * ( {str(integer_4())} {str(sym_2)} {str(integer_3(True))} * {str(var1)} )'
            half_2 = fr'{str(integer_4())}'
        else:
            half_1 = fr'{str(integer_3(True))} * ( {str(integer_3())} {str(sym_1)} {str(integer_3(True))} * {str(var1)} ) {str(sym_2)} {str(integer_3())}'
            half_2 = fr'{str(integer_3())} {str(sym_3)} {str(integer_3(True))} * {str(var1)}'

        if random.randint(1, 2) == 1:
            half_1, half_2 = swapper(half_1, half_2)

        if random.randint(1, 2) == 1:
            answer = sympy.latex(sympy.sympify(half_1, evaluate=False), order="none") + \
                r" = " + sympy.latex(sympy.sympify(half_2,
                                     evaluate=False), order="none")
        else:
            answer = sympy.latex(sympy.sympify(half_1, evaluate=False), order="lex") + \
                r" = " + sympy.latex(sympy.sympify(half_2,
                                     evaluate=False), order="lex")
        # lex, grlex, or grevlex
        temp = sympy.Eq(sympy.sympify(half_1), sympy.sympify(half_2))
        holder = sympy.solve(temp, x)
        holder = holder.pop()
        if str(holder).find("/") != -1:
            holder = str(holder)
            # find numerator and denominator
        holder = sympy.sympify(fractions.Fraction(str(holder)))

    return(sympy.latex(holder, fold_short_frac=False, mode="inline"), str(answer))


print("EASY")
for i in range(3):
    a, b = Solving_Multi_Step_Inequalities("easy", 'latex')
    print(a, r'\\', '\n', b, r'\\')
    print(r'\\')
print("MEDIUM")
for i in range(3):
    a, b = Solving_Multi_Step_Inequalities("medium", 'latex')
    print(a, r'\\', '\n', b, r'\\')
    print(r'\\')
print("HARD")
for i in range(3):
    a, b = Solving_Multi_Step_Inequalities("hard", 'latex')
    print(a, r'\\', '\n', b, r'\\')
    print(r'\\')


# -----------------------------------------END OF PART 5-------------------------------------

# First Section


def Whole_Inequality_Graph_Template(line_length, symbol):
    line_length = int(line_length)
    number_line_size = -7  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 4  # plus minus 4
    while (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 3
        elif (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 3

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (14,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    out.append(r'\foreach \x in {1,2,...,13}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')
    copy = [
        r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (14,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    copy.append(r'\foreach \x in {1,2,...,13}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    # out.append(fr'{$\scriptstyle \the\numexpr-{number_line_size}+1*\x\relax$};)')-7 + 1*
    # out.append(r"{}{}{}".format('{$\scriptstyle \the\numexpr-', str(number_line_size), '+1*\x\relax$};)'))
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def Decimal_Inequality_Graph_Template(line_length, symbol):
    line_length = float(line_length)
    number_line_size = -2  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 1  # plus minus 4
    while (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 1
        elif (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 1

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (7,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    out.append(r'\foreach \x in {1,2,...,6}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')

    copy = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (7,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    copy.append(r'\foreach \x in {1,2,...,6}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def else_situation(sym_1):
    if sym_1 == '<':
        sym_1 = '>'
        return(sym_1)
    elif sym_1 == '>':
        sym_1 = '<'
        return(sym_1)
    elif sym_1 == '>=':
        sym_1 = '<='
        return(sym_1)
    elif sym_1 == '<=':
        sym_1 = '>='
        return(sym_1)


def Graphing_One_Variable_Inequalities_1(option_difficulty, option_random):
    problemsets = []
    answerset = []
    another = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    negative = ['-', '']
    sym_1 = ''
    variables = []
    numerals = []
    equation = ''
    receivant = ""
    inequal_symbols = ['>', '<', '>=', '<=']
    # greater/less than or equal to included (positive variables and number range from -5 to 5)
    if option_difficulty == "easy":
        variables.append(random.choice(choices))
        sym_1 = random.choice(inequal_symbols)
        numerals.append(str(random.choice(negative)) +
                        str(random.randint(1, 5)))

        x = sp.symbols(variables[0])

        if random.randint(1, 2) == 1:
            equation = '{} {} {}'.format(
                variables[0], str(sym_1), str(numerals[0]))
            problemsets.append(sp.latex(sp.sympify(equation),
                               fold_short_frac=False, mode="inline"))
            receivant = Whole_Inequality_Graph_Template(numerals[0], sym_1)
            answerset.append(receivant[0])
            another.append(receivant[1])
        else:
            equation = '{} {} {}'.format(
                str(numerals[0]), str(sym_1), variables[0])
            problemsets.append(sp.latex(sp.sympify(equation),
                               fold_short_frac=False, mode="inline"))
            receivant = Whole_Inequality_Graph_Template(
                numerals[0], else_situation(sym_1))
            answerset.append(receivant[0])
            another.append(receivant[1])

    elif option_difficulty == "medium":  # greater/less than or equal to included, but with a greater number threshhold and possibility of negative variables
        if str(random.choice(negative)) == '-':
            variables.append('-' + str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            filler = str(random.choice(negative)) + str(random.randint(1, 10))
            numerals.append(int(filler))
            if random.randint(1, 2) == 1:
                equation = '{} {} {}'.format(
                    variables[0], str(sym_1), str(numerals[0]))
                sym_1 = else_situation(sym_1)
                numerals[0] = int(filler) * -1
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Whole_Inequality_Graph_Template(numerals[0], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {}'.format(
                    str(numerals[0]), str(sym_1), variables[0])
                sym_1 = else_situation(sym_1)
                numerals[0] = int(filler) * -1
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Whole_Inequality_Graph_Template(
                    numerals[0], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
        else:
            variables.append(str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(1, 10)))
            if random.randint(1, 2) == 1:
                equation = '{} {} {}'.format(
                    variables[0], str(sym_1), str(numerals[0]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Whole_Inequality_Graph_Template(numerals[0], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {}'.format(
                    str(numerals[0]), str(sym_1), variables[0])
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Whole_Inequality_Graph_Template(
                    numerals[0], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])

    elif option_difficulty == "hard":  # fraction (mixed?)
        if str(random.choice(negative)) == '-':
            variables.append('-' + str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            filler = str(random.choice(negative)) + \
                str(random.randint(1, 10)) + "." + str(random.randint(1, 99))
            numerals.append(float(filler))
            if random.randint(1, 2) == 1:
                equation = '{} {} {}'.format(
                    variables[0], str(sym_1), str(numerals[0]))
                sym_1 = else_situation(sym_1)
                numerals[0] = float(filler) * -1
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Decimal_Inequality_Graph_Template(
                    numerals[0], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {}'.format(
                    str(numerals[0]), str(sym_1), variables[0])
                sym_1 = else_situation(sym_1)
                numerals[0] = float(filler) * -1
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Decimal_Inequality_Graph_Template(
                    numerals[0], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
        else:
            variables.append(str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            numerals.append(str(random.choice(
                negative)) + str(random.randint(1, 10)) + "." + str(random.randint(1, 99)))
            if random.randint(1, 2) == 1:
                equation = '{} {} {}'.format(
                    variables[0], str(sym_1), str(numerals[0]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Decimal_Inequality_Graph_Template(
                    numerals[0], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {}'.format(
                    str(numerals[0]), str(sym_1), variables[0])
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                receivant = Decimal_Inequality_Graph_Template(
                    numerals[0], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])

    return(problemsets[0], answerset[0], another[0])


for i in range(1):
    a, b, c = Graphing_One_Variable_Inequalities_1("easy", False)
    print(a, '\n', b, '\n', c)
for i in range(1):
    a, b, c = Graphing_One_Variable_Inequalities_1("medium", False)
    print(a, '\n', b, '\n', c)
for i in range(1):
    a, b, c = Graphing_One_Variable_Inequalities_1("hard", False)
    print(a, '\n', b, '\n', c)


# First Section


def Whole_Inequality_Graph_Template(line_length, symbol):
    line_length = int(line_length)
    number_line_size = -7  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 4  # plus minus 4
    while (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 3
        elif (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 3

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (14,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    out.append(r'\foreach \x in {1,2,...,13}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')
    copy = [
        r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (14,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    copy.append(r'\foreach \x in {1,2,...,13}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    # out.append(fr'{$\scriptstyle \the\numexpr-{number_line_size}+1*\x\relax$};)')-7 + 1*
    # out.append(r"{}{}{}".format('{$\scriptstyle \the\numexpr-', str(number_line_size), '+1*\x\relax$};)'))
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def else_situation(sym_1):
    if sym_1 == '<':
        sym_1 = '>'
        return(sym_1)
    elif sym_1 == '>':
        sym_1 = '<'
        return(sym_1)
    elif sym_1 == '>=':
        sym_1 = '<='
        return(sym_1)
    elif sym_1 == '<=':
        sym_1 = '>='
        return(sym_1)


def Solving_One_Step_Inequalities_Adding_Subtracting(option_difficulty='easy', expr='latex'):
    problemsets = []
    answerset = []
    another = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    addition_expression = ['+', '-']
    negative = ['-', '']
    sym_1 = ''
    sym_1 = ''
    variables = []
    numerals = []
    equation = ''
    ran = 0
    receivant = ""
    inequal_symbols = ['>', '<', '>=', '<=']
    # greater/less than or equal to included (positive variables and number range from -5 to 5)  x − 1 > 6
    if option_difficulty == "easy":
        variables.append(random.choice(choices))
        sym_1 = random.choice(inequal_symbols)
        sym_2 = random.choice(addition_expression)
        numerals.append(str(random.randint(1, 5)))
        numerals.append(str(random.choice(negative)) +
                        str(random.randint(1, 5)))

        x = sp.symbols(variables[0])

        ran = random.randint(1, 4)

        if ran == 1:
            equation = '{} {} {} {} {}'.format(
                variables[0], sym_2, numerals[0], str(sym_1), str(numerals[1]))
            problemsets.append(sp.latex(sp.sympify(equation),
                               fold_short_frac=False, mode="inline"))
            if sym_2 == '+':
                numerals[1] = int(numerals[1]) - int(numerals[0])
            else:
                numerals[1] = int(numerals[1]) + int(numerals[0])
            receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
            answerset.append(receivant[0])
            another.append(receivant[1])
        elif ran == 2:
            equation = '{} {} {} {} {}'.format(
                str(numerals[0]), sym_2, variables[0], str(sym_1), str(numerals[1]))
            problemsets.append(sp.latex(sp.sympify(equation),
                               fold_short_frac=False, mode="inline"))
            numerals[1] = int(numerals[1]) - int(numerals[0])
            if sym_2 == '-':
                sym_1 = else_situation(sym_1)
                numerals[1] = int(numerals[1]) * -1
            receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
            answerset.append(receivant[0])
            another.append(receivant[1])
        elif ran == 3:  # inequal first
            equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                sym_1), variables[0], sym_2, str(numerals[0]))
            problemsets.append(sp.latex(sp.sympify(equation),
                               fold_short_frac=False, mode="inline"))
            if sym_2 == '+':
                numerals[1] = int(numerals[1]) - int(numerals[0])
            else:
                numerals[1] = int(numerals[1]) + int(numerals[0])
            receivant = Whole_Inequality_Graph_Template(
                numerals[1], else_situation(sym_1))
            answerset.append(receivant[0])
            another.append(receivant[1])
        else:
            equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                sym_1), str(numerals[0]), sym_2, variables[0])
            problemsets.append(sp.latex(sp.sympify(equation),
                               fold_short_frac=False, mode="inline"))
            numerals[1] = int(numerals[1]) - int(numerals[0])
            if sym_2 == '-':
                sym_1 = else_situation(sym_1)
                numerals[1] = int(numerals[1]) * -1
            receivant = Whole_Inequality_Graph_Template(
                numerals[1], else_situation(sym_1))
            answerset.append(receivant[0])
            another.append(receivant[1])

    elif option_difficulty == "medium":  # greater/less than or equal to included, but with a greater number threshhold and possibility of negative variables -x−14>−12
        if str(random.choice(negative)) == '-':
            variables.append('-' + str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(1, 10)))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(1, 10)))

            x = sp.symbols(variables[0])

            ran = random.randint(1, 2)

            if ran == 1:
                equation = '{} {} {} {} {}'.format(
                    variables[0], sym_2, numerals[0], str(sym_1), str(numerals[1]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(
                    int(numerals[1]) * -1, else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:  # inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                    sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(
                    int(numerals[1]) * -1, sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
        else:
            variables.append(random.choice(choices))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(1, 10)))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(1, 10)))

            x = sp.symbols(variables[0])

            ran = random.randint(1, 4)

            if ran == 1:
                equation = '{} {} {} {} {}'.format(
                    variables[0], sym_2, numerals[0], str(sym_1), str(numerals[1]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 2:
                equation = '{} {} {} {} {}'.format(
                    str(numerals[0]), sym_2, variables[0], str(sym_1), str(numerals[1]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 3:  # inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                    sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(
                    numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                    sym_1), str(numerals[0]), sym_2, variables[0])
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(
                    numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])

    # all of the above, and some more... (larger num threshhold)
    elif option_difficulty == "hard":
        if str(random.choice(negative)) == '-':
            variables.append('-' + str(random.choice(choices)))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(10, 30)))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(10, 30)))

            x = sp.symbols(variables[0])

            ran = random.randint(1, 2)

            if ran == 1:
                equation = '{} {} {} {} {}'.format(
                    variables[0], sym_2, numerals[0], str(sym_1), str(numerals[1]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(
                    int(numerals[1]) * -1, else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:  # inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                    sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(
                    int(numerals[1]) * -1, sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
        else:
            variables.append(random.choice(choices))
            sym_1 = random.choice(inequal_symbols)
            sym_2 = random.choice(addition_expression)
            numerals.append(str(random.randint(10, 30)))
            numerals.append(str(random.choice(negative)) +
                            str(random.randint(10, 30)))

            x = sp.symbols(variables[0])

            ran = random.randint(1, 4)

            if ran == 1:
                equation = '{} {} {} {} {}'.format(
                    variables[0], sym_2, numerals[0], str(sym_1), str(numerals[1]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 2:
                equation = '{} {} {} {} {}'.format(
                    str(numerals[0]), sym_2, variables[0], str(sym_1), str(numerals[1]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(numerals[1], sym_1)
                answerset.append(receivant[0])
                another.append(receivant[1])
            elif ran == 3:  # inequal first
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                    sym_1), variables[0], sym_2, str(numerals[0]))
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                if sym_2 == '+':
                    numerals[1] = int(numerals[1]) - int(numerals[0])
                else:
                    numerals[1] = int(numerals[1]) + int(numerals[0])
                receivant = Whole_Inequality_Graph_Template(
                    numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])
            else:
                equation = '{} {} {} {} {}'.format(str(numerals[1]), str(
                    sym_1), str(numerals[0]), sym_2, variables[0])
                problemsets.append(
                    sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                numerals[1] = int(numerals[1]) - int(numerals[0])
                if sym_2 == '-':
                    sym_1 = else_situation(sym_1)
                    numerals[1] = int(numerals[1]) * -1
                receivant = Whole_Inequality_Graph_Template(
                    numerals[1], else_situation(sym_1))
                answerset.append(receivant[0])
                another.append(receivant[1])

    return(problemsets[0], answerset[0], another[0])


for i in range(3):
    a, b, c = Solving_One_Step_Inequalities_Adding_Subtracting("easy", False)
    print(a, '\\\ \n', b, '\\\ \n', c)
for i in range(3):
    a, b, c = Solving_One_Step_Inequalities_Adding_Subtracting("medium", False)
    print(a, '\\\ \n', b, '\\\ \n', c)
for i in range(3):
    a, b, c = Solving_One_Step_Inequalities_Adding_Subtracting("hard", False)
    print(a, '\\\ \n', b, '\\\ \n', c)


# First Section


def Whole_Inequality_Graph_Template(line_length, symbol):
    line_length = int(line_length)
    number_line_size = -7  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 4  # plus minus 4
    while (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 3
        elif (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 3

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (14,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    out.append(r'\foreach \x in {1,2,...,13}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')
    copy = [
        r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (14,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    copy.append(r'\foreach \x in {1,2,...,13}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    # out.append(fr'{$\scriptstyle \the\numexpr-{number_line_size}+1*\x\relax$};)')-7 + 1*
    # out.append(r"{}{}{}".format('{$\scriptstyle \the\numexpr-', str(number_line_size), '+1*\x\relax$};)'))
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def Decimal_Inequality_Graph_Template(line_length, symbol):
    line_length = float(line_length)
    number_line_size = -2  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 1  # plus minus 4
    while (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 1
        elif (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 1

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (7,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    out.append(r'\foreach \x in {1,2,...,6}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')

    copy = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (7,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    copy.append(r'\foreach \x in {1,2,...,6}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def else_situation(sym_1):
    if sym_1 == '<':
        sym_1 = '>'
        return(sym_1)
    elif sym_1 == '>':
        sym_1 = '<'
        return(sym_1)
    elif sym_1 == '>=':
        sym_1 = '<='
        return(sym_1)
    elif sym_1 == '<=':
        sym_1 = '>='
        return(sym_1)


def Solving_One_Step_Inequalities_Multiplication_Division(option_difficulty='easy', expr='latex'):
    problemsets = []
    answerset = []
    another = []
    choices = ['x', 'y', 'a', 'b', 'z', 'p', 't',
               'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v']
    all_expressions = ['+', '-', '*', '/']
    addition_expression = ['+', '-']
    mult_expression = ['*', '/']
    negative = ['-', '']
    sym_1 = ''
    sym_1 = ''
    variables = []
    variable_values = []
    numerals = []
    equation = ''
    receivant = ""
    inequal_symbols = ['>', '<', '>=', '<=']

    # greater/less than or equal to included (positive variables and number range from -5 to 5)
    if option_difficulty == "easy":
        sym_1 = random.choice(inequal_symbols)
        sym_2 = "*"
        numerals.append(str(random.randint(2, 5)))
        numerals.append(str(random.choice(negative)) +
                        str(random.randint(1, 5)))

        if str(random.choice(negative)) == '-':  # if variable is negative
            variables.append('-' + str(random.choice(choices)))
            x = sp.symbols(variables[0])
            if sym_2 == '*':  # var first
                if random.randint(1, 2) == 1:

                    equation = fr'{variables[0]} * {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    if str(numerals[1])[0] == '-' and str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), else_situation((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[1])[0] == '-':
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), else_situation((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[0])[0] == "-":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0])), (sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0])), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} * {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[0] == '-' and str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[1])[0] == '-':
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[0])[0] == "-":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0])), ((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:

                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), (sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])

        else:  # if variable is posititive
            variables.append(random.choice(choices))
            x = sp.symbols(variables[0])
            if sym_2 == '*':  # var first
                if random.randint(1, 2) == 1:
                    equation = fr'{variables[0]} * {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) / int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            float(numerals[1]), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            float(numerals[1]), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} * {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) / int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])

    elif option_difficulty == "medium":
        sym_1 = random.choice(inequal_symbols)
        sym_2 = "/"
        numerals.append(str(random.randint(2, 5)))
        numerals.append(str(random.choice(negative)) +
                        str(random.randint(1, 5)))

        if str(random.choice(negative)) == '-':  # if variable is negative

            variables.append('-' + str(random.choice(choices)))
            x = sp.symbols(variables[0])
            if sym_2 == '/':

                if random.randint(1, 2) == 1:
                    equation = fr'{variables[0]} / {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    if str(numerals[1])[0] == '-':
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), else_situation((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} / {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[0] == '-':
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), (sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])

        else:  # if variable is posititive
            variables.append(random.choice(choices))
            x = sp.symbols(variables[0])
            if sym_2 == '/':

                if random.randint(1, 2) == 1:
                    equation = fr'{variables[0]} / {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) * int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    receivant = Whole_Inequality_Graph_Template(
                        float(numerals[1]), sym_1)
                    answerset.append(receivant[0])
                    another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} / {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) * int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])

    elif option_difficulty == "hard":

        sym_1 = random.choice(inequal_symbols)
        sym_2 = random.choice(mult_expression)
        numerals.append(str(random.randint(2, 5)))
        numerals.append(str(random.choice(negative)) +
                        str(random.randint(1, 5)))

        if str(random.choice(negative)) == '-':  # if variable is negative

            variables.append('-' + str(random.choice(choices)))
            x = sp.symbols(variables[0])
            if sym_2 == '*':  # var first
                if random.randint(1, 2) == 1:

                    equation = fr'{variables[0]} * {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    if str(numerals[1])[0] == '-' and str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), else_situation((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[1])[0] == '-':
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), else_situation((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[0])[0] == "-":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0])), (sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0])), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} * {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[0] == '-' and str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[1])[0] == '-':
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    elif str(numerals[0])[0] == "-":
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0])), ((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) / (int(numerals[0]) * -1), (sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
            elif sym_2 == '/':
                if random.randint(1, 2) == 1:
                    equation = fr'{variables[0]} / {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    if str(numerals[1])[0] == '-':
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), else_situation((sym_1)))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} / {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[0] == '-':
                        receivant = Whole_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), (sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            int(numerals[1]) * (int(numerals[0]) * -1), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])

        else:  # if variable is posititive
            variables.append(random.choice(choices))
            x = sp.symbols(variables[0])
            if sym_2 == '*':  # var first
                if random.randint(1, 2) == 1:
                    equation = fr'{variables[0]} * {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) / int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            float(numerals[1]), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            float(numerals[1]), sym_1)
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} * {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) / int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
            elif sym_2 == '/':

                if random.randint(1, 2) == 1:
                    equation = fr'{variables[0]} / {numerals[0]} {sym_1} {numerals[1]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) * int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    receivant = Whole_Inequality_Graph_Template(
                        float(numerals[1]), sym_1)
                    answerset.append(receivant[0])
                    another.append(receivant[1])
                else:
                    equation = fr'{numerals[1]} {sym_1} {variables[0]} / {numerals[0]}'
                    problemsets.append(
                        sp.latex(sp.sympify(equation), fold_short_frac=False, mode="inline"))
                    numerals[1] = int(numerals[1]) * int(numerals[0])

                    # if ending value is not 0, the ncall on the decimal numberline
                    if str(numerals[1])[-1] == "0":
                        receivant = Whole_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])
                    else:
                        receivant = Decimal_Inequality_Graph_Template(
                            float(numerals[1]), else_situation(sym_1))
                        answerset.append(receivant[0])
                        another.append(receivant[1])

    return(problemsets[0], answerset[0], another[0])


for i in range(3):
    a, b, c = Solving_One_Step_Inequalities_Multiplication_Division(
        "easy", 'latex')
    print(a, r'\\', '\n', b, r'\\', '\n', c)
    print(r'\\')
for i in range(3):
    a, b, c = Solving_One_Step_Inequalities_Multiplication_Division(
        "medium", 'latex')
    print(a, r'\\', '\n', b, r'\\', '\n', c)
    print(r'\\')
for i in range(3):
    a, b, c = Solving_One_Step_Inequalities_Multiplication_Division(
        "hard", 'latex')
    print(a, r'\\', '\n', b, r'\\', '\n', c)
    print(r'\\')


def Whole_Inequality_Graph_Template(line_length, symbol):
    line_length = int(line_length)

    number_line_size = -7  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 4  # plus minus 4
    while (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 7) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 3
        elif (number_line_size + 7) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 3

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (14,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    out.append(r'\foreach \x in {1,2,...,13}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')
    copy = [
        r'\begin{tikzpicture}[line width=1pt,line cap=round,x=.5cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (14,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (14,0);')
    copy.append(r'\foreach \x in {1,2,...,13}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    # out.append(fr'{$\scriptstyle \the\numexpr-{number_line_size}+1*\x\relax$};)')-7 + 1*
    # out.append(r"{}{}{}".format('{$\scriptstyle \the\numexpr-', str(number_line_size), '+1*\x\relax$};)'))
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (12,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (2,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def Decimal_Inequality_Graph_Template(line_length, symbol):
    line_length = float(line_length)
    number_line_size = -2  # "the zero" starting place
    MINIMUM_NUMBERLINE_SIZE = 1  # plus minus 4
    while (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length or (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
        if (number_line_size + 2) + MINIMUM_NUMBERLINE_SIZE < line_length:
            number_line_size = number_line_size + 1
        elif (number_line_size + 2) - MINIMUM_NUMBERLINE_SIZE > line_length:
            number_line_size = number_line_size - 1

    deviation = 0
    number_line_domain = 0
    copy = []
    out = []
    out = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    out.append(r'\clip (0,-0.8) rectangle (7,1);')
    out.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    out.append(r'\foreach \x in {1,2,...,6}')
    out.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    out.append(r'{')
    out.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    out.append(r'};')

    copy = [r'\begin{tikzpicture}[line width=1pt,line cap=round,x=1cm,y=.5cm]']
    copy.append(r'\clip (0,-0.8) rectangle (7,1);')
    copy.append(r'\draw  [<->,thick]    (0,0) -- (7,0);')
    copy.append(r'\foreach \x in {1,2,...,6}')
    copy.append(r'\draw (\x,-2pt) -- (\x,2pt) node [anchor=north,below=3pt]')
    copy.append(r'{')
    copy.append(fr'$\scriptstyle \the\numexpr{number_line_size} + 1*\x\relax$')
    copy.append(r'};')
    if symbol == '>':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length}, 0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=white, thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '>=':
        out.append(
            fr'\draw[->,very thick,red,-latex] ({(-1 * number_line_size) + line_length},0) -- (7,0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    elif symbol == '<=':
        out.append(
            fr'\draw[<-,very thick,red,latex-] (0,0) -- ({(-1 * number_line_size) + line_length},0);')
        out.append(
            fr'\draw[red, fill=red, very thick] ({(-1 * number_line_size) + line_length},0) circle (-2pt);')

    out.append(r'\end{tikzpicture}')
    copy.append(r'\end{tikzpicture}')
    return(''.join(out), ''.join(copy))


def else_situation(sym_1):
    if sym_1 == '<':
        sym_1 = '>'
        return(sym_1)
    elif sym_1 == '>':
        sym_1 = '<'
        return(sym_1)
    elif sym_1 == '>=':
        sym_1 = '<='
        return(sym_1)
    elif sym_1 == '<=':
        sym_1 = '>='
        return(sym_1)


def hard_diff():
    first = ""
    second = ""
    if random.randint(1, 2) == 1:
        checker = ""
        variable = random.choice(
            ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

        number_one = random.randint(1, 30)
        number_two = random.randint(1, 30)
        number_three = random.randint(1, 30)

        sym_1 = random.choice(["+", "-"])
        negative = ["", "-"]
        inequality_sign = random.choice([">", "<", ">=", "<="])
        x = sympy.Symbol(str(variable))

        problem = ""
        answer = ""
#problem = fr"({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} {str(inequality_sign)} {str(number_two)}"

        if random.randint(1, 2) == 1:  # division
            if random.randint(1, 2) == 1:
                problem = fr"{str(variable)} / {str(number_three)} {str(sym_1)} {str(number_one)} {str(inequality_sign)} {str(number_two)}"
            else:
                problem = fr"{str(number_two)} {str(inequality_sign)} {str(variable)} / {str(number_three)} {str(sym_1)} {str(number_one)}"
            #print("problem", problem)
            answer = sympy.solvers.inequalities.reduce_rational_inequalities(
                [[sympy.sympify(problem)]], x)
        else:  # multiplication
            if random.randint(1, 2) == 1:
                problem = fr"{str(random.choice(negative))} {str(number_one)} * {str(variable)} {str(sym_1)} {str(number_three)} {str(inequality_sign)} {str(number_two)}"
            else:
                problem = fr"{str(number_two)} {str(inequality_sign)} {str(random.choice(negative))} {str(number_one)} * {str(variable)} {str(sym_1)} {str(number_three)}"
            #print("problem", problem)
            answer = sympy.solvers.inequalities.reduce_rational_inequalities(
                [[sympy.sympify(problem)]], x)

        answer = str(answer)
        if str(answer).find("oo") <= 10:
            # print(answer[str(answer).find("&") + 3:-1]) #print(answer[str(answer).find("&") + 3:-1])
            checker = answer[str(answer).find("&") + 3:-1]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
        else:
            # print("else")
            # print("HERERE--------------------")
            #print(answer[1:str(answer).find("&") - 2])
            checker = answer[1:str(answer).find("&") - 2]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
            else:
                if str(float(Fraction(checker[0])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[0]), else_situation(checker[1]))
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[0])), else_situation(checker[1]))
        #print(problem, answer)
        if random.randint(1, 2) == 1:
            return(sympy.latex(sympy.sympify(problem, evaluate=False), fold_short_frac=False, mode="inline"), first, second)
        else:
            return(sympy.latex(sympy.sympify(problem), fold_short_frac=False, mode="inline"), first, second)
    else:
        checker = ""
        variable = random.choice(
            ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

        number_one = random.randint(1, 30)
        number_two = random.randint(1, 30)
        number_three = random.randint(1, 30)

        sym_1 = random.choice(["+", "-"])
        negative = ["", "-"]
        inequality_sign = random.choice([">", "<", ">=", "<="])
        x = sympy.Symbol(str(variable))

        problem = ""
        answer = ""
        if random.randint(1, 2) == 1:
            problem = fr"{str(random.choice(negative))} ({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} {str(inequality_sign)} {str(number_two)}"
        else:
            problem = fr"{str(number_two)} {str(inequality_sign)} {str(random.choice(negative))} ({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} "
        answer = sympy.solvers.inequalities.reduce_rational_inequalities(
            [[sympy.sympify(problem)]], x)

        answer = str(answer)
        if str(answer).find("oo") <= 10:
            # print(answer[str(answer).find("&") + 3:-1]) #print(answer[str(answer).find("&") + 3:-1])
            checker = answer[str(answer).find("&") + 3:-1]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
        else:
            # print("else")
            # print("HERERE--------------------")
            #print(answer[1:str(answer).find("&") - 2])
            checker = answer[1:str(answer).find("&") - 2]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
            else:
                if str(float(Fraction(checker[0])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[0]), else_situation(checker[1]))
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[0])), else_situation(checker[1]))
        #print(problem, answer)
        return(sympy.latex(sympy.sympify(problem, evaluate=False), fold_short_frac=False, mode="inline"), first, second)


def Solving_Two_Step_Inequalities(option_difficulty='easy', expr='latex'):
    first = ""
    second = ""
    if option_difficulty == "easy":
        checker = ""
        variable = random.choice(
            ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

        number_one = random.randint(1, 10)
        number_two = random.randint(1, 10)
        number_three = random.randint(1, 10)

        sym_1 = random.choice(["+", "-"])
        negative = ["", "-"]
        inequality_sign = random.choice([">", "<", ">=", "<="])
        x = sympy.Symbol(str(variable))

        problem = ""
        answer = ""
#problem = fr"({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} {str(inequality_sign)} {str(number_two)}"

        if random.randint(1, 2) == 1:  # division
            if random.randint(1, 2) == 1:
                problem = fr"{str(variable)} / {str(number_three)} {str(sym_1)} {str(number_one)} {str(inequality_sign)} {str(number_two)}"
            else:
                problem = fr"{str(number_two)} {str(inequality_sign)} {str(variable)} / {str(number_three)} {str(sym_1)} {str(number_one)}"
            #print("problem", problem)
            answer = sympy.solvers.inequalities.reduce_rational_inequalities(
                [[sympy.sympify(problem)]], x)
        else:  # multiplication
            if random.randint(1, 2) == 1:
                problem = fr"{str(random.choice(negative))} {str(number_one)} * {str(variable)} {str(sym_1)} {str(number_three)} {str(inequality_sign)} {str(number_two)}"
            else:
                problem = fr"{str(number_two)} {str(inequality_sign)} {str(random.choice(negative))} {str(number_one)} * {str(variable)} {str(sym_1)} {str(number_three)}"
            #print("problem", problem)
            answer = sympy.solvers.inequalities.reduce_rational_inequalities(
                [[sympy.sympify(problem)]], x)

        answer = str(answer)
        if str(answer).find("oo") <= 10:
            # print(answer[str(answer).find("&") + 3:-1]) #print(answer[str(answer).find("&") + 3:-1])
            checker = answer[str(answer).find("&") + 3:-1]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
        else:
            # print("else")
            # print("HERERE--------------------")
            #print(answer[1:str(answer).find("&") - 2])
            checker = answer[1:str(answer).find("&") - 2]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
            else:
                if str(float(Fraction(checker[0])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[0]), else_situation(checker[1]))
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[0])), else_situation(checker[1]))
        #print(problem, answer)
        if random.randint(1, 2) == 1:
            return(sympy.latex(sympy.sympify(problem, evaluate=False), fold_short_frac=False, mode="inline"), first, second)
        else:
            return(sympy.latex(sympy.sympify(problem), fold_short_frac=False, mode="inline"), first, second)

    elif option_difficulty == "medium":
        checker = ""
        variable = random.choice(
            ['x', 'y', 'a', 'b', 'z', 'p', 't', 'q', 'k', 'u', 'r', 'd', 'w', 's', 'h', 'v'])

        number_one = random.randint(1, 10)
        number_two = random.randint(1, 10)
        number_three = random.randint(1, 10)

        sym_1 = random.choice(["+", "-"])
        negative = ["", "-"]
        inequality_sign = random.choice([">", "<", ">=", "<="])
        x = sympy.Symbol(str(variable))

        problem = ""
        answer = ""
        if random.randint(1, 2) == 1:
            problem = fr"{str(random.choice(negative))} ({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} {str(inequality_sign)} {str(number_two)}"
        else:
            problem = fr"{str(number_two)} {str(inequality_sign)} {str(random.choice(negative))} ({str(variable)} {str(sym_1)} {str(number_one)}) / {str(number_three)} "
        answer = sympy.solvers.inequalities.reduce_rational_inequalities(
            [[sympy.sympify(problem)]], x)

        answer = str(answer)
        if str(answer).find("oo") <= 10:
            # print(answer[str(answer).find("&") + 3:-1]) #print(answer[str(answer).find("&") + 3:-1])
            checker = answer[str(answer).find("&") + 3:-1]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
        else:
            # print("else")
            # print("HERERE--------------------")
            #print(answer[1:str(answer).find("&") - 2])
            checker = answer[1:str(answer).find("&") - 2]
            #print(checker, "checker")
            list(checker)
            checker = checker.split()
            # print(checker)
            if str(checker[0]) == str(variable):
                # print("noraml")
                #print(checker[2:3], "inequal")
                #print(checker[3:], "numba")
                # print(float(Fraction(checker[3:])))
                if str(float(Fraction(checker[2])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[2]), checker[1])
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[2])), checker[1])
            else:
                if str(float(Fraction(checker[0])))[-2:] == ".0":
                    first, second = Whole_Inequality_Graph_Template(
                        float(checker[0]), else_situation(checker[1]))
                else:
                    first, second = Decimal_Inequality_Graph_Template(
                        float(Fraction(checker[0])), else_situation(checker[1]))
        #print(problem, answer)
        return(sympy.latex(sympy.sympify(problem, evaluate=False), fold_short_frac=False, mode="inline"), first, second)
    elif option_difficulty == "hard":
        return(hard_diff())


for i in range(5):
    a, b, c = Solving_Two_Step_Inequalities("easy", 'latex')
    print(a, r'\\', '\n', b, r'\\', '\n', c)
    print(r'\\')
for i in range(5):
    a, b, c = Solving_Two_Step_Inequalities("medium", 'latex')
    print(a, r'\\', '\n', b, r'\\', '\n', c)
    print(r'\\')
for i in range(5):
    a, b, c = Solving_Two_Step_Inequalities("hard", 'latex')
    print(a, r'\\', '\n', b, r'\\', '\n', c)
    print(r'\\')

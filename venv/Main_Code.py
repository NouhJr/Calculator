from Classes import Mathematics_Class,Trigonometric_Class,Statistics_Class # import Mathematics_Class,Trigonometric_Class and Statistics_Class from package(Classes)
import math
import numpy as np

while True:  # Creating while loop to let user control when to close the program.
    print("*************** W E L C O M E  T O  C A L C U L A T O R ***************")
    print("                ***************************************")
    print(" ____________________________________________")
    print("| Choose System:                             |\n")
    print("| 1 - Basic Mathematical Operations.         |\n")
    print("| 2 - Basic Statistics Operations.           |\n")  # Menu_1 to let the user choose the system.
    print("| 3 - Basic Trigonometric Functions.         |\n")
    print("| <<Please Choose Valid number from 1 to 3>> |")
    print(" ____________________________________________ \n")

    Choice0 = input()  # Scanning Choice from User using input() function
    c0 = int(Choice0)  # Casting input from string to integer using int() function

    if (c0 < 1) or (c0 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_1).
        print("Error: Invalid Input!")

    elif (c0 == 1): # when user choose the first choice from (Menu_1).
        print(" ____________________________________________")
        print("| Choose System:                             |\n")
        print("| 1 - Two Numbers.                           |\n")
        print("| 2 - Two Vectors.                           |\n")  # Menu_2 to let the user choose more specific system.
        print("| <<Please Choose Valid number (1) OR (2)>>      |")
        print(" ____________________________________________ \n")

        Choice1 = input()  # Scanning Choice from User using input() function
        c1 = int(Choice1)  # Casting input from string to integer using int() function

        if (c1 < 1) or (c1 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_2).
            print("Error: Invalid Input!")

        elif (c1 == 1): # when user choose the first choice from (Menu_2).
            print(" ____________________________________________")
            print("| Chose Operation:                           |\n")
            print("| 1 - Add.                                   |\n")
            print("| 2 - Subtract.                              |\n")
            print("| 3 - Multiply.                              |\n")  # Menu_3 to let the user choose specific operation from system_1.
            print("| 4 - Division.                              |\n")
            print("| <<Please Choose Valid number from 1 to 4>> |")
            print(" ____________________________________________ \n")

            Choice2 = input()  # Scanning Choice from User using input() function
            c2 = int(Choice2)  # Casting input from string to integer using int() function

            if (c2 < 1) or (c2 > 4):  # if condition to make sure that user has chosen valid choice from (Menu_3).
                print("Error: Invalid Input!")

            elif (c2 == 1):  # when user choose the first choice from (Menu_3).

                num1 = input("Enter first Number:\n")  # Scanning Numbers from User using input() function
                Num1 = float(num1)  # Casting input from string to float using float() function

                num2 = input("Enter second Number:\n")  # Scanning Numbers from User using input() function
                Num2 = float(num2)  # Casting input from string to float using float() function

                Operation = Mathematics_Class.Numbers()  # Creating Object(Operation) from Class(Mathematics)
                print("Result:\n")
                print(Num1, "+", Num2, "=", Operation.add(Num1, Num2))  # Accesing Method(add) from Class(Mathematics)

            elif (c2 == 2):  # when user choose the second choice from (Menu_3).
                num1 = input("Enter first Number:\n")  # Scanning Numbers from User using input() function
                Num1 = float(num1)  # Casting input from string to float using float() function

                num2 = input("Enter second Number:\n")  # Scanning Numbers from User using input() function
                Num2 = float(num2)  # Casting input from string to float using float() function

                Operation = Mathematics_Class.Numbers()  # Creating Object(Operation) from Class(Mathematics)
                print("Result:\n")
                print(Num1, "-", Num2, "=",
                      Operation.subtract(Num1, Num2))  # Accesing Method(add) from Class(Mathematics)

            elif (c2 == 3):  # when user choose the third choice from (Menu_3).
                num1 = input("Enter first Number:\n")  # Scanning Numbers from User using input() function
                Num1 = float(num1)  # Casting input from string to float using float() function

                num2 = input("Enter second Number:\n")  # Scanning Numbers from User using input() function
                Num2 = float(num2)  # Casting input from string to float using float() function

                Operation = Mathematics_Class.Numbers()  # Creating Object(Operation) from Class(Mathematics)
                print("Result:\n")
                print(Num1, "*", Num2, "=",
                      Operation.multiply(Num1, Num2))  # Accesing Method(add) from Class(Mathematics)

            elif (c2 == 4):  # when user choose the fourth choice from (Menu_3).
                num1 = input("Enter first Number:\n")  # Scanning Numbers from User using input() function
                Num1 = float(num1)  # Casting input from string to float using float() function

                num2 = input("Enter second Number:\n")  # Scanning Numbers from User using input() function
                Num2 = float(num2)  # Casting input from string to float using float() function

                Operation = Mathematics_Class.Numbers()  # Creating Object(Operation) from Class(Mathematics)
                print("Result:\n")
                print(Num1, "/", Num2, "=",
                      Operation.division(Num1, Num2))  # Accesing Method(add) from Class(Mathematics)


        elif (c1 == 2):  # when user choose the second choice from (Menu_2).
            print(" ____________________________________________")
            print("| Chose Operation:                           |\n")
            print("| 1 - Add.                                   |\n")
            print("| 2 - Subtract.                              |\n")
            print("| 3 - Multiply.                              |\n")  # Menu_3 to let the user choose specific operation from system_1.
            print("| 4 - Division.                              |\n")
            print("| <<Please Choose Valid number from 1 to 4>> |")
            print(" ____________________________________________ \n")

            Choice3 = input()  # Scanning Choice from User using input() function
            c3 = int(Choice3)  # Casting input from string to integer using int() function

            if (c3 < 1) or (c3 > 5):
                print("Error: Invalid Input!")

            elif (c3 == 1):  # when user choose the first choice from (Menu_3).

                vector1_str = input("Enter first vector's elements Seprated by comma:\n")  # Scanning first vector from user.
                vector1_split = vector1_str.split(",")  # Separate elements of the vector.
                vector1 = [float(element) for element in vector1_split]  # Casting element of first victor from string to float using float() method.

                vector2_str = input("Enter second vector's elements Seprated by comma:\n<<Must be the same size as first vector>>\n")  # Scanning second vector from user.
                vector2_split = vector2_str.split(",")  # Separate elements of the vector.
                vector2 = [float(element) for element in vector2_split]  # Casting element of second victor from string to float using float() method.

                size = len(vector1)  # Determine the size of one of the vectors to create for loop.

                operation = Mathematics_Class.Vectors()  # Creating object from class Vectors in package Classes.
                operation.add(vector1, vector2, size)  # Accesing method(add) from class(vectors).


            elif (c3 == 2):  # when user choose the second choice from (Menu_3).

                vector1_str = input("Enter first vector's elements Seprated by comma:\n")  # Scanning first vector from user.
                vector1_split = vector1_str.split(",")  # Separate elements of the vector.
                vector1 = [float(element) for element in vector1_split]  # Casting element of first victor from string to float using float() method.

                vector2_str = input("Enter second vector's elements Seprated by comma:\n<<Must be the same size as first vector>>\n")  # Scanning second vector from user.
                vector2_split = vector2_str.split(",")  # Separate elements of the vector.
                vector2 = [float(element) for element in vector2_split]  # Casting element of second victor from string to float using float() method.

                size = len(vector1)  # Determine the size of one of the vectors to create for loop.

                operation = Mathematics_Class.Vectors()  # Creating object from class Vectors in package Classes.
                operation.subtract(vector1, vector2, size)  # Accesing method(subtract) from class(vectors).


            elif (c3 == 3):  # when user choose the third choice from (Menu_3).

                vector1_str = input("Enter first vector's elements Seprated by comma:\n")  # Scanning first vector from user.
                vector1_split = vector1_str.split(",")  # Separate elements of the vector.
                vector1 = [float(element) for element in vector1_split]  # Casting element of first victor from string to float using float() method.

                vector2_str = input("Enter second vector's elements Seprated by comma:\n<<Must be the same size as first vector>>\n")  # Scanning second vector from user.
                vector2_split = vector2_str.split(",")  # Separate elements of the vector.
                vector2 = [float(element) for element in vector2_split]  # Casting element of second victor from string to float using float() method.

                size = len(vector1)  # Determine the size of one of the vectors to create for loop.

                operation = Mathematics_Class.Vectors()  # Creating object from class Vectors in package Classes.
                operation.multiply(vector1, vector2, size)  # Accesing method(multiply) from class(vectors).

            elif (c3 == 4):  # when user choose the fourth choice from (Menu_3).

                vector1_str = input("Enter first vector's elements Seprated by comma:\n")  # Scanning first vector from user.
                vector1_split = vector1_str.split(",")  # Separate elements of the vector.
                vector1 = [float(element) for element in vector1_split]  # Casting element of first victor from string to float using float() method.

                vector2_str = input("Enter second vector's elements Seprated by comma:\n<<Must be the same size as first vector>>\n")  # Scanning second vector from user.
                vector2_split = vector2_str.split(",")  # Separate elements of the vector.
                vector2 = [float(element) for element in vector2_split]  # Casting element of second victor from string to float using float() method.

                size = len(vector1)  # Determine the size of one of the vectors to create for loop.

                operation = Mathematics_Class.Vectors()  # Creating object from class Vectors in package Classes.
                operation.division(vector1, vector2, size)  # Accesing method(division) from class(vectors).



    elif (c0 == 2):
        data_str = input("Enter your data set Seprated by comma:\n")  # Scanning data set from user.
        data_split = data_str.split(",")  # Separate elements of the data set.
        data = [float(element) for element in data_split]  # Casting element of data set from string to float using float() method.

        print(" ____________________________________________")
        print("| Chose Operation:                           |\n")
        print("| 1 - Mean.                                  |\n")
        print("| 2 - Median.                                |\n")
        print("| 3 - Mod.                                   |\n")  # Menu_7 to let the user choose specific operation from system_2.
        print("| 4 - variance.                              |\n")
        print("| 5 - Standard Deviation.                    |\n")
        print("| <<Please Choose Valid number from 1 to 5>> |")
        print(" ____________________________________________ \n")

        Choice9 = input()  # Scanning Choice from User using input() function
        c9 = int(Choice9)  # Casting input from string to integer using int() function

        if (c9 < 1) or (c9 > 5):  # if condition to make sure that user has chosen valid choice from (Menu_1).
            print("Error: Invalid Input!")


        elif (c9 == 1):  # When user choose the first choice form Menu_7
            Stat = Statistics_Class.Statistics()  # Creating Object(Stat) from Class(Statistics)
            print("Mean =",Stat.Mean(data))

        elif (c9 == 2):  # When user choose the second choice form Menu_7
            Stat = Statistics_Class.Statistics()  # Creating Object(Stat) from Class(Statistics)
            print("Median =",Stat.Median(data))

        elif (c9 == 3):  # When user choose the third choice form Menu_7
            Stat = Statistics_Class.Statistics()  # Creating Object(Stat) from Class(Statistics)
            print("Mod =",Stat.Mod(data))

        elif (c9 == 4):  # When user choose the fourth choice form Menu_7
            Stat = Statistics_Class.Statistics()  # Creating Object(Stat) from Class(Statistics)
            print("Variance =",Stat.Variance(data))

        elif (c9 == 5):  # When user choose the fifth choice form Menu_7
            Stat = Statistics_Class.Statistics()  # Creating Object(Stat) from Class(Statistics)
            print("Standard_Deviation =",Stat.Standard_Deviation(data))



# Note : all values in this phase has been calculated by trigonometric functions that comes from 'math' module,
# so it would be a little different from the real values.
    elif (c0 == 3):  # when user choose the third choice from (Menu_1).
        print(" ____________________________________________")
        print("| Choose Operation:                          |\n")
        print("| 1 - Values.                                |\n")
        print("| 2 - Graphs.                                |\n")  # Menu_4 to let the user choose more specific system..
        print("| <<Please Choose Valid number (1) OR (2)>>  |")
        print(" ____________________________________________ \n")

        Choice4 = input()  # Scanning Choice from User using input() function
        c4 = int(Choice4)  # Casting input from string to integer using int() function

        if (c4 < 1) or (c4 > 2):  # if condition to make sure that user has chosen valid choice from (Menu_4).
            print("Error: Invalid Input!")

        elif (c4 == 1):
            print(" ____________________________________________")
            print("| Choose Angle:                              |\n")
            print("| 1  - Zero                                  |\n")
            print("| 2  - π/6   ...   (30 dgree)                |\n")
            print("| 3  - π/4   ...   (45 dgree)                |\n")
            print("| 4  - π/3   ...   (60 dgree)                |\n")
            print("| 5  - π/2   ...   (90 dgree)                |\n")
            print("| 6  - 2π/3  ...   (120 dgree)               |\n")
            print("| 7  - 5π/6  ...   (150 dgree)               |\n")  # Menu_5 to let the user choose the angle.
            print("| 8  - π     ...   (180 dgree)               |\n")
            print("| 9  - 5π/4  ...   (225 dgree)               |\n")
            print("| 10 - 3π/2  ...   (270 dgree)               |\n")
            print("| 11 - 5π/3  ...   (300 dgree)               |\n")
            print("| 12 - 11π/6 ...   (330 dgree)               |\n")
            print("| 13 - 2π    ...   (360 dgree)               |\n")
            print("| <<Please Choose Valid number from 1 to 13>>|")
            print(" ____________________________________________ \n")

            Choice5 = input()  # Scanning Choice from User using input() function
            c5 = int(Choice5)  # Casting input from string to integer using int() function

            if (c5 < 1) or (c5 > 13):  # if condition to make sure that user has chosen valid choice from (Menu_5).
                print("Error: Invalid Input!")

            elif (c5 == 1):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(Zero):")
                    print(Operation.Sin_value(0))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(Zero):")
                    print(Operation.Cos_value(0))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(Zero):")
                    print(Operation.Tan_value(0))  # Accessing (Tan_Value) function.


            elif (c5 == 2):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(π/6):")
                    print(Operation.Sin_value(math.pi/6))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(π/6):")
                    print(Operation.Cos_value(math.pi/6))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(π/6):")
                    print(Operation.Tan_value(math.pi/6))  # Accessing (Tan_Value) function.

            elif (c5 == 3):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(π/4):")
                    print(Operation.Sin_value(math.pi/4))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(π/4):")
                    print(Operation.Cos_value(math.pi/4))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(π/4):")
                    print(Operation.Tan_value(math.pi/4))  # Accessing (Tan_Value) function.

            elif (c5 == 4):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(π/3):")
                    print(Operation.Sin_value(math.pi/3))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(π/3):")
                    print(Operation.Cos_value(math.pi/3))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(π/3):")
                    print(Operation.Tan_value(math.pi/3))  # Accessing (Tan_Value) function.

            elif (c5 == 5):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(π/2):")
                    print(Operation.Sin_value(math.pi/2))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(π/2):")
                    print(Operation.Cos_value(math.pi/2))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(π/2):")
                    print(Operation.Tan_value(math.pi/2))  # Accessing (Tan_Value) function.

            elif (c5 == 6):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(2π/3):")
                    print(Operation.Sin_value(math.pi*2/3))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(2π/3):")
                    print(Operation.Cos_value(math.pi*2/3))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(2π/3):")
                    print(Operation.Tan_value(math.pi*2/3))  # Accessing (Tan_Value) function.

            elif (c5 == 7):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(5π/6):")
                    print(Operation.Sin_value(math.pi*5/6))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(5π/6):")
                    print(Operation.Cos_value(math.pi*5/6))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(5π/6):")
                    print(Operation.Tan_value(math.pi*5/6))  # Accessing (Tan_Value) function.

            elif (c5 == 8):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(π):")
                    print(Operation.Sin_value(math.pi))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(π):")
                    print(Operation.Cos_value(math.pi))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(π):")
                    print(Operation.Tan_value(math.pi))  # Accessing (Tan_Value) function.

            elif (c5 == 9):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(5π/4):")
                    print(Operation.Sin_value(math.pi*5/4))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(5π/4):")
                    print(Operation.Cos_value(math.pi*5/4))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(5π/4):")
                    print(Operation.Tan_value(math.pi*5/4))  # Accessing (Tan_Value) function.

            elif (c5 == 10):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(3π/2):")
                    print(Operation.Sin_value(math.pi*3/2))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(3π/2):")
                    print(Operation.Cos_value(math.pi*3/2))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(3π/2):")
                    print(Operation.Tan_value(math.pi*3/2))  # Accessing (Tan_Value) function.

            elif (c5 == 11):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(5π/3):")
                    print(Operation.Sin_value(math.pi*5/3))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(5π/3):")
                    print(Operation.Cos_value(math.pi*5/3))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(5π/3):")
                    print(Operation.Tan_value(math.pi*5/3))  # Accessing (Tan_Value) function.

            elif (c5 == 12):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(11π/6):")
                    print(Operation.Sin_value(math.pi*11/6))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(11π/6):")
                    print(Operation.Cos_value(math.pi*11/6))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(11π/6):")
                    print(Operation.Tan_value(math.pi*11/6))  # Accessing (Tan_Value) function.

            elif (c5 == 13):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| 3  - Tan                                   |\n")
                print("| <<Please Choose Valid number from 1 to 3>> |  ")
                print(" ____________________________________________ \n")

                Choice6 = input()  # Scanning Choice from User using input() function
                c6 = int(Choice6)  # Casting input from string to integer using int() function

                if (c6 < 1) or (c6 > 3):  # if condition to make sure that user has chosen valid choice from (Menu_6).
                    print("Error: Invalid Input!")

                elif (c6 == 1):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Sin(2π):")
                    print(Operation.Sin_value(math.pi*2))  # Accessing (Sin_Value) function.

                elif (c6 == 2):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Cos(2π):")
                    print(Operation.Cos_value(math.pi*2))  # Accessing (Cos_Value) function.

                elif (c6 == 3):
                    Operation = Trigonometric_Class.Trigonometric()  # Creating object(Operation) from (Trigonometric Class).
                    print("Tan(2π):")
                    print(Operation.Tan_value(math.pi*2))  # Accessing (Tan_Value) function.


        elif (c4 == 2):
            print(" ____________________________________________")
            print("| Choose Angle:                              |\n")
            print("| 1  - π/6   ...   (30 dgree)                |\n")
            print("| 2  - π/4   ...   (45 dgree)                |\n")
            print("| 3  - π/3   ...   (60 dgree)                |\n")
            print("| 4  - π/2   ...   (90 dgree)                |\n")
            print("| 5  - 2π/3  ...   (120 dgree)               |\n")
            print("| 6  - 5π/6  ...   (150 dgree)               |\n")
            print("| 7  - π     ...   (180 dgree)               |\n")   # Menu_7 to let the user choose the angle(extended).
            print("| 8  - 5π/4  ...   (225 dgree)               |\n")
            print("| 9 - 3π/2   ...   (270 dgree)               |\n")
            print("| 10 - 5π/3  ...   (300 dgree)               |\n")
            print("| 11 - 11π/6 ...   (330 dgree)               |\n")
            print("| 12 - 2π    ...   (360 dgree)               |\n")
            print("| 13 - General graph for Sine                |\n")
            print("| 14 - General graph for Cosine              |\n")
            print("| 15 - General graph for Tan                 |\n")
            print("| <<Please Choose Valid number from 1 to 15>>|")
            print(" ____________________________________________ \n")

            Choice7 = input()  # Scanning Choice from User using input() function
            c7 = int(Choice7)  # Casting input from string to integer using int() function

            if (c7 < 1) or (c7 > 15):  # if condition to make sure that user has chosen valid choice from {Menu_7(extended)}.
                print("Error: Invalid Input!")
                
            elif (c7 == 1):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")
                
                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi/6, "π/6")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi/6, "π/6")


            elif (c7 == 2):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi/4, "π/4")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi/4, "π/4")


            elif (c7 == 3):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi/3, "π/3")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi/3, "π/3")


            elif (c7 == 4):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi/2, "π/2")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi/2, "π/2")


            elif (c7 == 5):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi*2/3, "2π/3")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi*2/3, "2π/3")


            elif (c7 == 6):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi*5/6, "5π/6")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi*5/6, "5π/6")


            elif (c7 == 7):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi, "π")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi, "π")


            elif (c7 == 8):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi*5/4, "5π/4")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi*5/4, "5π/4")


            elif (c7 == 9):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi*3/2, "3π/2")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi*3/2, "3π/2")


            elif (c7 == 10):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi*5/3, "5π/3")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi*5/3, "5π/3")


            elif (c7 == 11):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi*11/6, "11π/6")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi*11/6, "11π/6")


            elif (c7 == 12):
                print(" ____________________________________________   ")
                print("| Choose Function:                           |\n")
                print("| 1  - Sine                                  |\n")
                print("| 2  - Cosine                                |\n")  # Menu_6 to let the user choose the Function.
                print("| <<Please Choose Valid number (1) OR (2)>>  |  ")
                print(" ____________________________________________ \n")

                Choice8 = input()  # Scanning Choice from User using input() function
                c8 = int(Choice8)  # Casting input from string to integer using int() function

                if (c8 < 1) or (c8 > 2):  # if condition to make sure that user has chosen valid choice from {Menu_6}.
                    print("Error: Invalid Input!")

                elif (c8 == 1):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Sine_Graph(np.pi*2, "2π")

                elif (c8 == 2):
                    Graph = Trigonometric_Class.Graphs()
                    Graph.Cosine_Graph(np.pi*2, "2π")


            elif (c7 == 13):
                Graph = Trigonometric_Class.Graphs()
                Graph.Sine_Graph(np.pi*4, "")

            elif (c7 == 14):
                Graph = Trigonometric_Class.Graphs()
                Graph.Cosine_Graph(np.pi*4, "")

            elif (c7 == 15):
                Graph = Trigonometric_Class.Graphs()
                Graph.Tan_Graph()


    decision = input("\nDo You Want to Continue?\n<<press 'y' for Yes>>\n")  # Scanning choice from user to cheack if he want to keep the program running or no.
    if (decision != 'y'):  # if condition to close the program if user didn't choose to keep it running.
        print("<<Developed By 'Omar Nouh'>>\n****************************")  # Developer's Signature.
        break
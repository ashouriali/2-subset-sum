def read_input():
    ##############################
    #
    # this function reads the input
    #
    ##############################
    
    inp_numbers = input('enter the numbers(split them by space):')
    inp_numbers = inp_numbers.split(' ')
    summation = input('enter any int number as an arbitary summation:')
    
    return inp_numbers,summation

def strlist_to_intlist(inp_list):
    ####################################
    #
    # this function changes the type of 
    # the list of string numbers to a list
    # of integer numbers
    #
    ####################################
    
    input_numbers = list(map(int,inp_list))
    
    return input_numbers

def find_conjugate_numbers(str_numbers , summation):
    ###################################
    #
    # this function finds in given list
    # two numbers whose sum are 
    # equal to summation(given)
    #
    ###################################
    
    summation = int(summation)
    int_numbers = strlist_to_intlist(str_numbers)

    
    numbers_dict = dict(zip(str_numbers,int_numbers))
    
    
    conjugate_numbers = []

    #special case for even summation
    if summation%2==0:
        if int_numbers.count(summation//2)== 1 :
            del numbers_dict[str(summation//2)]
        elif int_numbers.count(summation//2) > 1:
            conjugate_numbers.append((summation//2,summation//2))
            del numbers_dict[str(summation//2)]
    
    for num in numbers_dict:
        if numbers_dict[num]<= summation:
            suggested_num = summation-numbers_dict[num]
            suggested_num = str(suggested_num)
            if numbers_dict.get(suggested_num,None) is not None:
                conjugate_numbers.append((num,suggested_num))

    return conjugate_numbers

def print_numbers(conj_numbers):
    ###################################
    #
    # this function print the conjugate 
    # numbers
    #
    ###################################
    
    for num in conj_numbers:
        print(num[0],'+',num[1],'=' , int(num[0])+int(num[1]))
    
def main():
    #############################
    #
    # the program starts from this
    # function
    #
    #############################
    
    inp_numbers,summation = read_input()
    conj_numbers = find_conjugate_numbers(inp_numbers , summation)
    print_numbers(conj_numbers)
    
# by calling main() the program starts
main()


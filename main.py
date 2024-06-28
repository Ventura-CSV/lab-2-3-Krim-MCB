def main():
    val1=int(input("Enter Val1:"))
    val2=int(input("Enter Val2:"))
    val3=int(input("Enter Val1:"))
    total=val1+val2+val3
    average = total/3 
    print(f'Total: {total}')
    print(f'Average:{average:.2f}')
    total_result=total 
    average_result=average
    ##################################################
    # Comlete your code here
    ##################################################
    """
    Use following variables to save your result
    total 
    average
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return total_result, average_result

if __name__ == '__main__':
    main()

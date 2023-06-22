def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    nomales = int(input('Enter the amount of males registered in the class: '))
    nofemales =int(input('Enter the amount of females registed in the class: '))
    total = nomales + nofemales
    m_perc = (nomales/total)*100
    f_perc = (nofemales/total)*100
    print('Total number of students: ', total)
    print('Total number of males and females: ', nomales, "\t", nofemales)
    print('The percentage of males and females', m_perc, "% \t", f_perc, "%")
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()

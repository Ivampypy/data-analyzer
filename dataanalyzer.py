
import numpy as np


def create_array(l,low_b,high_b):
    if low_b>=high_b:
        raise ValueError('Low border must be smaller than high border!')
    if l<=0:
        raise ValueError('Length must be >0!')
    if high_b-low_b<l:
        raise ValueError('Array can not be filled, not enough values!')
    
    
    rng=np.random.default_rng()
    arr=rng.integers(low_b,high_b,l)
    return arr



def show_info():
    print('====================================')
    print('')
    print('           DATA ANALYZER            ')
    print('')
    print('====================================')
    print('')
    print('             OPTIONS                 ')
    print('')
    print('1. Find minimum')
    print('2. Find maximum')
    print('3. Find average')
    print('4. Find median')
    print('5. Find mode')
    print('6. Find variance')
    print('7. Find standard deviation')
    print('8. Find the Q1')
    print('9. Find the Q3')
    print('10. Find the IQR')
    print('11. Show array')
    print('0. Back')


def find_min(array):
    return np.min(array)

def find_max(array):
    return np.max(array)

def find_average(array):
    return round(np.mean(array),2)

def find_mode(array):
    values, frequency = np.unique(array, return_counts=True)
    max_frequency = np.max(frequency)

    if max_frequency == 1:
        return 'This array does not have a mode!'

    mode = values[frequency == max_frequency]

    return mode
    
    
def find_median(array):
    return np.median(array)

def find_variance(array):
    return round(np.var(array),2)

def find_stdev(array):
    return round(np.std(array),2)


def find_q1(array):
    array=np.sort(array)
    if len(array)%2==0:
        first_half=array[:(len(array)//2)]
        return round(np.median(first_half),2)
    else:
        ind=len(array)//2
        first_half=array[:ind]
        return round(np.median(first_half),2)

def find_q3(array):
    array=np.sort(array)
    if len(array)%2==0:
        second_half=array[(len(array)//2):]
        return round(np.median(second_half),2)
    else:
        ind=len(array)//2
        second_half=array[ind+1:]
        return round(np.median(second_half),2)

def find_iqr(array):
    return round(find_q3(array)-find_q1(array),2)



def outputting_res(result):
    print('===============================================================')
    print('===============================================================')
    print('')
    print('                           YOUR RESULT:                         ')
    print('')
    print(f'                            {result}                           ')
    print('')
    print('===============================================================')
    print('===============================================================')

def bye():
    print('--------------------------------------------------')
    print(' Bye-Bye! Catch you later then! Thanks for using!')
    print('        I hope it was useful for you!                ')
    print('---------------------------------------------------')

    

def main():
    print('')
    print('')
    print('HI!')
    length=int(input(('To get started, please input the length of your array:')))
    print('')
    low_border,high_border=map(int,input('Input low border and high border of values in array: ').split())
    data=create_array(length,low_border,high_border)
    if data is None:
        return
    print('')
    show_info()
    while True:
        print('')
        operation=input(' Input the number of action: ')
        if not(operation.isdigit()):
            print('Try again and input only digits!')
            continue
        operation=int(operation)
        if operation>11:
            print('Try again and input only values<=11!')
            continue


        match operation:
            case 1:
                outputting_res(find_min(data))
            case 2:
                outputting_res(find_max(data))
            case 3:
                outputting_res(find_average(data))
            case 4:
                outputting_res(find_median(data))
            case 5:
                outputting_res(find_mode(data))
            case 6:
                outputting_res(find_variance(data))
            case 7:
                outputting_res(find_stdev(data))
            case 8:
                outputting_res(find_q1(data))
            case 9:
                outputting_res(find_q3(data))
            case 10:
                outputting_res(find_iqr(data))
            case 11:
                outputting_res(data)
            case 0:
                bye()
                break
                


        

if __name__=='__main__':
    main()

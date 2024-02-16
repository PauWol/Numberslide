import math , time

def multiply_digits(n):
    r = 1
    num_str = str(n)
    for i in range(int(math.log10(n)) + 1):
        r = r * int(num_str[i])
    return r

def calc(range):
    result = []
    for i in range:
        x = multiply_digits(i)
        while x > 10:
            x  = multiply_digits(x)
        if x % 2 != 0:
            result.append({'number': i, 'product of digits': x})
    return result

def format_result(val_array,output_delay_s):
    for i in val_array:
        print('Start: '+str(i.get('number')),'Result: '+str(i.get('product of digits')))
        time.sleep(output_delay_s)


def inp():
    inp_tup = input('Enter a Numberrange like (1,100): ')
    inp_tup = inp_tup.split(',')
    if len(inp_tup) != 2:
        print('Please enter a correct numberrange')
        inp()
    return range(int(inp_tup[0]), int(inp_tup[1]))

def main():
    format_result(calc(inp()),0)

if __name__ == '__main__':
    start = time.process_time()
    main()
    elapsed = (time.process_time() - start)
    print(f"Execution time: {elapsed} seconds")
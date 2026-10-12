def swap_case(s):
    nl=list(s)
    for i in range(len(nl)):
        if nl[i].isupper():
            nl[i]=nl[i].lower()
        elif nl[i].islower():
            nl[i]=nl[i].upper()
    
    return "".join(nl)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
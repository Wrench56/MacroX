def parse_char(string) -> int:
    ret_lst = []
    chr_ord = None
    for i, char in enumerate(string):
        if skip_count > 0:
            skip_count -= 1
            continue
        if char == '#':
            if len(string)-1 >= i+3:
                if string[i+1] == 'E' and string[i+2] == 'S' and string[i+3] == 'C':
                    chr_ord = 27
                    skip_count = 3

        else:
            chr_ord = ord(char)
        ret_lst.append(chr_ord)
    
    return ret_lst
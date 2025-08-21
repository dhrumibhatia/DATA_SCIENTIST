def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string


#sol2
string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
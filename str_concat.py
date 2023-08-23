def str_concat (*str ) : 
    result = ""
    for i in str : 
        result = result + i + " "
    return result


print(str_concat("Hello","World"))
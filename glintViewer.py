import os, sys

def prettyPrint(json, headers, colum_sizes):
    print_line = line(colum_sizes)
    print print_line
    print header(headers, colum_sizes)
    print print_line
    content = body(json, headers, colum_sizes)
    for content_line in content:
        print content_line
    print print_line

def line(colum_sizes):
    rtn_line = '+'
    for colum in colum_sizes:
        rtn_line += '-'*(colum+2)
        rtn_line += '+'
    return rtn_line


def header(headers, colum_sizes):
    rtn_header = '|'
    for header, colum in zip(headers, colum_sizes):
        rtn_header += ' ' + header['header']
        rtn_header += ' '*(colum-len(header['header'])+1)
        rtn_header += '|'
    return rtn_header


def body(json, headers, colum_sizes):
    rtn_lines = []
    for item in json:
        tmp_line = '|'
        for header, colum in zip(headers, colum_sizes):
            tmp_line += ' '
            tmp_line += item[header['key']]
            tmp_line += ' '*(colum-len(item[header['key']])-1)
            tmp_line += ' |'
        rtn_lines.append(tmp_line)
    return rtn_lines
          

def main():
    json = [{u'Result':u'Successful Delete', u'Item':u'Image1'}, {u'Result':u'Unsuccessful Delete', u'Item':u'Image2'}]
    headers = [{'header':'Result', 'key':'Result'}, {'header':'Item', 'key':'Item'}]
    colum_sizes = [19,6]

    prettyPrint(json, headers, colum_sizes)


if __name__=="__main__":
    main()
        
    

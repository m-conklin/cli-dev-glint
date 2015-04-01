import os, sys

import cli_factory_utils as fact_utils

def cli_view(json,cmd):
    print "View the Json %s with command %s"%(json,cmd)
    #get titles
    headers = fact_utils.get_titles(cmd)
    #print headers
    if "%s"%cmd in "get-images":
        col_sizes = fact_utils.get_image_max_column_sizes(json,headers)
    else:
        col_sizes = fact_utils.get_max_column_sizes(json,headers)
    print headers
    print col_sizes

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
            tmp_line += ' ' + str(item[header['key']])
            tmp_line += ' '*(colum-len(str(item[header['key']]))+1)
            tmp_line += '|'
        rtn_lines.append(tmp_line)
    return rtn_lines
          

       
    

import os, sys

def prettyPrint(json, headers, colum_sizes):


def line(colum_sizes):
    rtn_line = '+'
    for colum in colum_sizes:
        rtn_line += '-'*(colum+2)
        rtn_line += '+'
    return rtn_line


def header(headers, colum_sizes):
    rtn_header = '| '
    for header, colum in zip(headers, colum_sizes):
        rtn_header += header
        rtn_header += ' '*(colum-len(header)-1)
        rtn_header += '| '
    return rtn_header
        
    

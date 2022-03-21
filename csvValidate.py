# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 11:09:52 2022

This tool will compare the schema of a csv with the header of a csv to identify any issues.

@author: Alec_2
"""

def accessData():
    with open("schema.csv", "r") as f:
        schema = f.read().split(',')
        
    with open("file.csv", "r") as g:
        file = g.readline().split(',')
    
    return schema, file
    
def fileValidate(schema, file):
    if len(schema) != len(file):
        print('File format does not match schema.')
        print('Expected ', str(len(schema)), 'columns. Received ', str(len(file)), 'columns.\n')
    
    errors = []
    index = 0
    for e in range(len(schema)):
        if schema[e].strip('\n') != file[e].strip('\n'):
            errors.append((schema[e], file[e]))
        index+=1
    if len(errors)>0:
        print('Schema Violations Found: (Schema Format , CSV Format)\n')
        for error in errors:
            print(error)
    else:
        print('File schema is valid')
    
    stop = input('--- Enter any key to quit ---\n')
    
    if stop == True:
        quit()
    
def main():
    schema, file = accessData()
    fileValidate(schema, file)
    
main() 
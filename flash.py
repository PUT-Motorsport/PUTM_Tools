#!/usr/bin/python3
import os
import argparse

parser = argparse.ArgumentParser(description='PUTM tools to flash STM32 chips.')
parser.add_argument('-b', '--board', choices=['f1', 'f4', 'l4'], required=True, help='Chip\'s family')
parser.add_argument('-f', '--file', required=True, help='Binary file to flash to STM in elf format')

args = parser.parse_args()

cfg_file = ''
if args.board == 'f1':
    cfg_file = 'st_nucleo_f1.cfg'
elif args.board == 'f3':
    cfg_file = 'st_nucleo_f3.cfg'
elif args.board == 'f4':
    cfg_file = 'st_nucleo_f4.cfg'
elif args.board == 'l4':
    cfg_file = 'st_nucleo_l4.cfg'
    
if os.path.isfile(args.file):
    print('file exists')
else:
    print('No such file: ', args.file)
    exit(-1)

command = 'openocd '

command += '-f '
command += cfg_file
command += ' '

command += '-c "program '
command += args.file
command += ' verify reset exit"'

print(command)
os.system(command)



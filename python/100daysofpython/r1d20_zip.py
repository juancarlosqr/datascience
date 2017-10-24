#!/usr/bin/env python3

import os
import glob
import time
import zipfile

def run_backup1():
    ''''''
    print('\nrunning backup v1')
    source_dir = ['/Users/juancarlosqr/code/empty/files']
    target_dir = '/Users/juancarlosqr/code/empty/backup'
    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
    #create target dir, if not exists
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    zip_command = f'zip -r {target} {" ".join(source_dir)}'
    print('zip command is:', zip_command)
    print('Running command')
    if os.system(zip_command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup failed')

def run_backup2():
    ''''''
    print('\nrunning backup v2')
    source_dir = ['/Users/juancarlosqr/code/empty/files']
    target_dir = '/Users/juancarlosqr/code/empty/backup'
    #create target dir, if not exists
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    today = target_dir + os.sep + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    target = today + os.sep + now + '.zip'
    if not os.path.exists(today):
        os.mkdir(today)
        print('directory created', today)
    zip_command = f'zip -r {target} {" ".join(source_dir)}'
    print('zip command is:', zip_command)
    print('Running command')
    if os.system(zip_command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup failed')

def run_backup3():
    ''''''
    print('\nrunning backup v3')
    source_dir = ['/Users/juancarlosqr/code/empty/files']
    target_dir = '/Users/juancarlosqr/code/empty/backup'
    #create target dir, if not exists
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    today = target_dir + os.sep + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    comment = input('Enter a comment: ')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + \
                 '_' + comment.replace(' ', '_') + '.zip'
    if not os.path.exists(today):
        os.mkdir(today)
        print('directory created', today)
    zip_command = f'zip -r {target} {" ".join(source_dir)}'
    print('zip command is:', zip_command)
    print('Running command')
    if os.system(zip_command) == 0:
        print('Successful backup to', target)
    else:
        print('Backup failed')

def run_backup4():
    ''''''
    print('\nrunning backup v4')
    source_dir = [
        '/Users/juancarlosqr/code/empty/files',
        '/Users/juancarlosqr/code/empty/copy'
    ]
    files = [file for source in source_dir for file in glob.glob(source + os.sep + '*')]
    target_dir = '/Users/juancarlosqr/code/empty/backup'
    # create target dir, if not exists
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    # date as folder name
    today = target_dir + os.sep + time.strftime('%Y%m%d')
    # time as zip file name
    now = time.strftime('%H%M%S')
    comment = input('enter a comment: ')
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + \
                 '_' + comment.replace(' ', '_') + '.zip'
    # create today dir, if not exists
    if not os.path.exists(today):
        os.mkdir(today)
        print('directory created', today)
    # create zip file
    print('creating zip')
    with zipfile.ZipFile(target, 'w') as zip:
        for file in files:
            print('adding to zip:', file)
            zip.write(file)
        print('successful backup to', target)

if __name__ == '__main__':
    # run_backup1()
    # run_backup2()
    # run_backup3()
    run_backup4()

'''
output:

running backup v4
enter a comment: dummy
creating zip
adding to zip: /Users/juancarlosqr/code/empty/files/file1.txt
adding to zip: /Users/juancarlosqr/code/empty/files/file2.txt
adding to zip: /Users/juancarlosqr/code/empty/files/file3.txt
adding to zip: /Users/juancarlosqr/code/empty/copy/file1.txt
adding to zip: /Users/juancarlosqr/code/empty/copy/file2.txt
adding to zip: /Users/juancarlosqr/code/empty/copy/file3.txt
successful backup to /Users/juancarlosqr/code/empty/backup/20171024/081956_dummy.zip
'''

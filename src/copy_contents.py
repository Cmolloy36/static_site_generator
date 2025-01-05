import os
import shutil

public_fpth = ''
static_fpth = ''


def copy_contents(source,dest,fpth_list=[]):
    '''Copies contents from source to specified directory.
    Source: a directory
    Dest: a directory'''
    cwd = os.getcwd()
    dest_pth = os.path.join(cwd,dest)
    if os.path.exists(dest_pth):
        # remove directory contents
        shutil.rmtree(dest_pth)

    # make new directory
    os.mkdir(dest_pth)

    source_fpth = os.path.join(cwd,source)
    
    if os.path.exists(source_fpth):
        for file in os.listdir(source_fpth):
            source_fpth_fnm = os.path.join(source_fpth,file)
            if os.path.isfile(source_fpth_fnm): # if this file is a leaf
                print(f'{source_fpth_fnm} is a leaf')
                shutil.copy2(source_fpth_fnm,dest)
                fpth_list.append(source_fpth_fnm)
            else:
                dest_fnm = os.path.join(dest,file)
                copy_contents(source_fpth_fnm,dest_fnm) # in a different world, we would use the shutil.copytree()
    return fpth_list
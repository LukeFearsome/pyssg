import os
import shutil

def copy_static(dest):
    public = dest
    static = "./static/"

    shutil.rmtree(public)
    os.mkdir(public)

    copy_dir(static,public)
    
def copy_dir(src,dst):
    if not os.path.exists(dst):
        print(f"Creating directory: {dst}")
        os.mkdir(dst)

    for item in os.listdir(src):
        if os.path.isfile(os.path.join(src,item)):
            print("Copying: " + os.path.join(src,item) + " -> " + os.path.join(dst,item))
            shutil.copy(os.path.join(src,item),os.path.join(dst,item))
        elif os.path.isdir(os.path.join(src,item)):
            copy_dir(os.path.join(src,item),os.path.join(dst,item))
        else:
            raise Exception("Unexpected item in copied folder.")

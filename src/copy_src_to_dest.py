import os
import shutil

def main():
    copy_src_to_dest()

def delete_all_in_dest(destination):
    print('checking if public directory exists')
    if os.path.exists(destination):
        print('Deleting Public')
        shutil.rmtree(destination)
    else:
        print('no public directory found')
    print('creating public folder')
    # os.mkdir(destination)

def copy_from_src_to_dest(origin,dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for filename in os.listdir(origin):
        from_path = os.path.join(origin, filename)
        dest_path = os.path.join(dest, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_from_src_to_dest(from_path, dest_path)    


def copy_src_to_dest():
    DEST_FOLDER = './public/'
    SOURCE_STATIC_FOLDER = './static/'
    delete_all_in_dest(DEST_FOLDER)
    copy_from_src_to_dest(SOURCE_STATIC_FOLDER,DEST_FOLDER)


if __name__ == '__main__':
    main()


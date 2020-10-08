import os
import shutil


def main_function(dir_path):
    """The main function executing all of the functions"""
    gen_walk_obj_1 = os.walk(dir_path)
    folder_creator(gen_walk_obj_1)
    gen_walk_obj_2 = os.walk(dir_path)
    file_mover(gen_walk_obj_2)


def folder_creator(generator_object):
    """Takes in the first generator object and creates folders according to the extensions"""    
    for path, folders, files in generator_object:

        folder_extensions = []
        file_extensions = []
        path_check = (path.split("\\"))[-1]

        if "AO-" not in path_check:
            if files:
                for file in files:
                    ext_slicer = (file[-9:].split("."))[-1]
                    file_extensions.append(ext_slicer)

                for folder in folders:
                    if "AO-" in folder:
                        ext_slicer = (folder.split("-"))[-1].lower()
                        folder_extensions.append(ext_slicer)

                    else:
                        pass

                for file_ext in set(file_extensions):
                    if file_ext not in folder_extensions:
                        updated_path = os.path.join(path, ("AO-"+file_ext.upper()))
                        os.mkdir(updated_path)

                    else:
                        pass

            else:
                # print(f"There are no files in this directory : {path}")
                pass

        else:
            # print(f"This directory has already been sorted : {path}")
            pass


def file_mover(generator_object):
    """Takes in the updated generator object and moves the files according to the extensions"""
    for path, folders, files in generator_object:
        if files:
            for file in files:
                ext_det = ((file[-9:].split("."))[-1]).upper()
                for folder in folders:
                    if ((folder.split("-"))[-1]).upper() == ext_det:
                        source = os.path.join(path, file)
                        dest_setter = folder + "\\" + file
                        destination = os.path.join(path, dest_setter)
                        shutil.move(source, destination)

                    else:
                        pass

        else:
            pass
            
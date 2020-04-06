"""zip module"""
import zipfile as zf
import os
import io
import json
from jsonpath_rw_ext import match


def zip_files(zip_file_name, files_to_zip):
    """
        Zips the specified files.

        Args:
            zip_file_name: The zip file name.
            files_to_zip: A list of files to zip.
    """
    with zf.ZipFile(zip_file_name, mode='w', allowZip64=True, compression=zf.ZIP_DEFLATED) \
            as zip_file:
        for file in files_to_zip:
            zip_file.write(file, arcname=os.path.basename(file))


def zip_camtasia_project_files(target_folder, project_file_name):
    """
        Zips the files contained in a Camtasia 2019 project file.

        Args:
            target_folder: The folder in which to write the zip file.
            project_file_name: The Camtasia project file name.
    """
    zip_file_name = os.path.basename(os.path.splitext(project_file_name)[0]) + ".zip"

    with io.open(project_file_name, "r", encoding="utf8") as project_file:
        json_file = json.load(project_file)
        project_files = match("$.sourceBin[*].src", json_file)
        project_file.append(project_file_name)
        zip_files(os.path.join(target_folder, zip_file_name), project_files)

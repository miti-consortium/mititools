import os
from os import mkdir
from os import listdir
from os.path import join
from os.path import exists

import pandas as pd

from ..default_values import cv_path
from ..name_manipulation import create_auxiliary_table_filename


def load_cv():
    cv_table_filenames = listdir(cv_path)
    strip = lambda x : re.sub('\.tsv$', '', x)
    cv_tables = {
        strip(basename(filename)) : pd.read_csv(join(cv_path, filename), sep='\t').fillna('')
        for filename in cv_table_filenames
    }
    return cv_tables


def write_cv(cv_tables):
    if not exists(cv_path):
        mkdir(cv_path)

    for tablename, df in cv_tables.items():
        filename = create_auxiliary_table_filename(tablename)
        df.to_csv(join(cv_path, filename), sep='\t', index=False)

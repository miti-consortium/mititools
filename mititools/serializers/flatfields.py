import os
from os import mkdir
from os.path import join
from os.path import exists
from os.path import basename
import re

import pandas as pd

from ..default_values import fields_filename
from ..default_values import tables_filename
from ..default_values import flatfields_path

from ..name_manipulation import create_table_filename
from ..name_manipulation import create_auxiliary_table_filename


def load_flatfields():
    fields_table = pd.read_csv(join(flatfields_path, fields_filename), sep='\t')
    tables_table = pd.read_csv(join(flatfields_path, tables_filename), sep='\t')
    fields_table.fillna('', inplace=True)
    tables_table.fillna('', inplace=True)
    return [fields_table, tables_table]


def write_flatfields(fields_table, tables_table):
    if not exists(flatfields_path):
        mkdir(flatfields_path)

    fields_table.to_csv(join(flatfields_path, fields_filename), sep='\t', index=False)
    tables_table.to_csv(join(flatfields_path, tables_filename), sep='\t', index=False)

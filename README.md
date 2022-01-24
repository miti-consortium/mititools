These tools convert the [MITI schema](https://github.com/miti-consortium/MITI) between 3 different formats:

1. `yaml`. The reference YAML specification, designed to be validated with [Cerberus](https://docs.python-cerberus.org/en/stable/).
2. `flatfields`. A specification based on a flat table of fields.
3. `frictionless`. A [Frictionless Data](https://frictionlessdata.io/standards/#standards-toolkit) [data package](https://specs.frictionlessdata.io/data-package/) schema.

The translation is not perfect, as the schema languages are not equivalent.

# Installation
The top level of this repository comprises a Python package, which is the standard structure for a Python source repository. To install from source, after `git clone` and `cd mititools`:
```sh
pip install .
```

# Generate alternative schema
```sh
mititools generate --source-dir path-to-yaml/
```

This creates:

1. `flatfields/fields.tsv`
2. `flatfields/tables.tsv`
3. `frictionless/datapackage.json`
4. `cv/*` controlled vocabulary tables
5. `example_fd_package/`

A snapshot of the most recently generated version of artifacts 1-4 are committed as part of this repository. Item 5 is not.


# Validation with FD
Frictionless Data (FD) is an extensive and modular system of high-level data management tools, with consistent bindings in Python, JavaScript, and the bash command-line.

```sh
frictionless validate example_fd_package/datapackage.json
```

Output:

```
# -----
# valid: biospecimen.tsv
# -----
# -----
# valid: cell.tsv
# -----

...
```

# Description with FD
```sh
frictionless describe example_fd_package/cell.tsv
```

Output:

```yaml
# --------
# metadata: example_fd_package/cell.tsv
# --------

dialect:
  delimiter: "\t"
encoding: utf-8
format: tsv
hashing: md5
name: cell
path: example_fd_package/cell.tsv
profile: tabular-data-resource
schema:
  fields:
    - name: data_file_id
      type: any
    - name: filename
      type: any
    - name: file_format
      type: any
    - name: parent_id
      type: any
    - name: software_and_version
      type: any
    - name: commit_sha
      type: any
    - name: comment
      type: any
    - name: header_size
      type: any
    - name: object_classes_included
      type: any
    - name: object_classes_description
      type: any
    - name: fov_size_x
      type: any
    - name: fov_size_y
      type: any
    - name: pyramid
      type: any
    - name: z_stack
      type: any
    - name: t_series
      type: any
    - name: type
      type: any
    - name: physical_size_x
      type: any
    - name: physical_size_xunit
      type: any
    - name: physical_size_y
      type: any
    - name: physical_size_yunit
      type: any
    - name: physical_size_z
      type: any
    - name: physical_size_zunit
      type: any
    - name: cell_state_level
      type: any
scheme: file
```


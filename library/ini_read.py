#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os, configparser

DOCUMENTATION = r'''
---
module: ini_read

short_description: Read a section from an .ini file.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Read a section from an .ini file.

options:
    path:
        description: Path to .ini file
        required: true
        type: str
    section:
        description: Name of section
        required: true
        type: str

author:
    - Steve Brasier (steveb@stackhpc.com)
'''

EXAMPLES = r'''
TODO
'''

RETURN = r'''
config: dict, keys/values from specified section
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    
    module_args = dict(
        path=dict(type='str', required=True),
        section=dict(type='str', required=True),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    path = module.params['path']
    section = module.params['section']
    
    result = dict(changed=False)
    
    if module.check_mode:
        module.exit_json(**result)
    if not os.path.exists(path):
        module.fail_json(msg='file {} not found'.format(path), **result)

    config = configparser.ConfigParser()
    config.read(path)
    result['config'] = dict((k, v) for k, v in config[section].items())
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
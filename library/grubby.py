#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

DOCUMENTATION = r'''
---
module: grubby

short_description: Set default kernel for boot.

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Set default kernel for boot.

options:
    version:
        description: A fully-specified kernel version string, e.g. '4.18.0-80.11.2.el8_0.x86_64'
        required: true
        type: str

author:
    - Steve Brasier (steveb@stackhpc.com)
'''

EXAMPLES = r'''
TODO
'''

RETURN = r'''
old_kernel_file: str, path of kernel file before this module ran
new_kernel_file: str, path of kernel file after this module ran

Note that if grubby fails to change the kernel, `new_kernel_file` specifies what it was trying to change it to.
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    
    module_args = dict(
        version=dict(type='str', required=True),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    kernel_version = module.params['version']
    result = dict(changed=False)
    

    if module.check_mode:
        module.exit_json(**result)

    # check required kernel is installed:
    kernel_file = os.path.join('/boot/vmlinuz-{}'.format(kernel_version))
    if not os.path.exists(kernel_file):
        module.fail_json(msg='File {} not found - is kernel {} installed?'.format(kernel_file, kernel_version), **result)

    # check existing boot default:
    _, current_default_stdout, _ = module.run_command('grubby --default-kernel', check_rc=True)
    result['old_kernel_file'] = current_default_stdout.strip()
    result['new_kernel_file'] = kernel_file
    if result['old_kernel_file'] == result['new_kernel_file']:
        module.exit_json(**result)
    
    # set new boot default:
    _, new_default_stdout, _ = module.run_command(['grubby', '--set-default', kernel_file], check_rc=True)
    result['changed'] = True
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
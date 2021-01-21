Role Name
=========

Manage `kernel` and `kernel-*` packages which depend on kernel version.

There are two problems which mean that it can be hard to install packages like `kernel-headers` properly: Firstly the kernel can change unexpectedly on reboot as (by default) CentOS installs updated `kernel` packages when available. Secondly the main CentOS repos only contain the latest versions of packages, which means `yum`/`dnf` may not be able to find `kernel-*` packages which match the running kernel.

This role fixes this by:
- Ensuring the selected kernel version is installed, running and set as the default on boot.
- Disabling updates to `kernel*` packages.
- Installing `kernel-*` packages matching the selected kernel from either the normal or CentOS Vault (archive) repos as necessary.

Note that outdated kernels and other packages may have security issues or contain bugs. However some applications such as lustre servers may require specific kernel versions.

Requirements
------------
A CentOS 7.8 - 8.3 (inclusive) x86_84 system. This role must be run with `become` and `gather_facts`.

Role Variables
--------------
- `kernel_version`: Optional. Either a specific, full kernel version as listed below or `{{ ansible_kernel }}` (default) to use the currently-running kernel.
   **NB:** In the default case the running kernel must still be in the list below.
- `kernel_pkgs`: Optional. A list of packages depending on a specific kernel version. Default is empty list.
- `kernel_pkgs_state`: Optional. Either `present` (default) or `absent` to control `kernel_pkgs` install state.

Kernel Versions
---------------
The following kernel versions may be used for `kernel_version`, depending on the running CentOS release:
- CentOS 8.3 (2011):
  - 4.18.0-240.1.1.el8_3.x86_64 (used by cloud image `CentOS-8-GenericCloud-8.3.2011-20201204.2.x86_64.qcow2`)
  - 4.18.0-240.10.1.el8_3.x86_64
  - 4.18.0-240.el8.x86_64
  - Any later kernels provided in the main CentOS repos.

- Centos 8.2 (2004):
  - 4.18.0-193.1.2.el8_2.x86_64
  - 4.18.0-193.6.3.el8_2.x86_64 (used by cloud image `CentOS-8-GenericCloud-8.2.2004-20200611.2.x86_64.qcow2`)
  - 4.18.0-193.14.2.el8_2.x86_64
  - 4.18.0-193.19.1.el8_2.x86_64
  - 4.18.0-193.28.1.el8_2.x86_64

- Centos 8.1 (1911):
  - 4.18.0-147.0.3.el8_1.x86_64
  - 4.18.0-147.3.1.el8_1.x86_64 (used by cloud image `CentOS-8-GenericCloud-8.1.1911-20200113.3.x86_64.qcow2`)
  - 4.18.0-147.5.1.el8_1.x86_64
  - 4.18.0-147.8.1.el8_1.x86_64
  - 4.18.0-147.el8.x86_64

- Centos 8.0 (1905):
  - 4.18.0-80.1.2.el8_0.x86_64
  - 4.18.0-80.4.2.el8_0.x86_64
  - 4.18.0-80.7.1.el8_0.x86_64
  - 4.18.0-80.7.2.el8_0.x86_64
  - 4.18.0-80.11.1.el8_0.x86_64
  - 4.18.0-80.11.2.el8_0.x86_64
  - 4.18.0-80.el8.x86_64

- Centos 7.9 (2009):
  - 3.10.0-1160.el7.x86_64 (used by cloud image CentOS-7-x86_64-GenericCloud-2009.qcow2)
  - Any later kernels provided in the main CentOS repos.

- Centos 7.8 (2003):
  - 3.10.0-1127.el7.x86_64 (used by cloud image CentOS-7-x86_64-GenericCloud-2003.qcow2)

Dependencies
------------

None.

Example Playbook
----------------

To install a `4.18.0-147.0.3` (for CentOS 8.1) kernel plus matching `kernel-headers` and `kernel-devel` packages:

    - hosts: servers
      become: yes
      tasks:
        - import_role:
            name: kernel_packages
            vars:
              kernel_version: "4.18.0-147.0.3.el8_1.x86_64"
              kernel_pkgs:
                - kernel-headers
                - kernel-devel


License
-------

Apache 2.0

Author Information
------------------

Steve Brasier steveb@stackhpc.com

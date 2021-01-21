Role Name
=========

Manage `kernel` and `kernel-*` packages which depend on kernel version.

There are two problems which mean that it can be hard to install packages like `kernel-headers` properly: Firstly by default the kernel can change unexpectedly on reboot as CentOS installs updated `kernel` packages when available. Secondly the main CentOS repos only contain the latest versions of packages, which means `yum`/`dnf` may not be able to find `kernel-*` packages which match the installed kernel.

This role fixes this by:
- Ensuring the selected kernel version is installed, running and set as the default on boot.
- Disabling kernel updates.
- Installing `kernel-*` packages matching the selected kernel from either the normal or CentOS Vault (archive) repos if necessary.

Note that outdated kernels and other packages may have security issues or contain bugs. However some applications such as lustre servers may require specific kernel versions.

Requirements
------------
A CentOS 7.8 - 8.3 (inclusive) system. This role must be run with `become` and `gather_facts`.

Role Variables
--------------
- `kernel_version`: Optional. Either a specific, full kernel version (e.g. `4.18.0-80.11.2.el8_0.x86_64`) or `pinned` (default) to use the currently-running kernel. Note that kernel versions
  must be appropriate for the running `major.minor` CentOS release.
- `kernel_pkgs`: Optional. A list of packages depending on a specific kernel version. Default `['kernel-headers']`.
- `kernel_pkgs_state`: Optional. Either `present` (default) or `absent` to control `kernel_pkgs` install state.

**NB:** The kernel version must be valid for the running CentOS release.

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

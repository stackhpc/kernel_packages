
Molecule tests using the OpenStack driver.

Note this role can't be tested using Docker as it requires specific/changing kernels.

# Installation

```shell
sudo yum install -y gcc python3-pip python3-devel openssl-devel python3-libselinux
cd <role>
python3 -m venv venv-mol
. venv-mol/bin/activate
pip install -U pip
pip install -r molecule/requirements.txt
```

# Configuration

Download an openstack .rc file to the role directory and source it.

Find generic CentOS images, flavors and an external network:

```shell
alaska openstack image list | grep -i centos
alaska openstack flavor list
alaska openstack network list
```

Using the above, copy `molecule/alaska-config.yml` and create a config file for your specific cloud. Now source that.

**NB: At present only testing of CentOS 8.2 images is configured** TODO: FIXME:

# Tests

The following tests are defined:
- `default`: Checks role defaults work, i.e. don't change kernel version (just pin etc), no other packages installed
- `change`: Change kernel version and install a matching package
- `nochange`: Don't change kernel version but install a matching package

Run tests using:

```shell
molecule --env-file molecule/alaska-config.yml test --all
```

replacing the env-file path with whatever your cloud config file is.
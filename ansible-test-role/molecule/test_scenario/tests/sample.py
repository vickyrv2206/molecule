import os
# import sys
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def check_info(host):
    f = host.file('/etc/hosts')
    assert f.exists


def sample(host):
    f = host.file('/etc/')
    assert f.exists
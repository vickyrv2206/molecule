import os
import os.path

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    print(host)
    f = host.file('/etc/hosts')
    assert host.file('/etc/hosts').exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_os_type(host):
    os.path.exists('/etc/hosts')

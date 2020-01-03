import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')
var_file_path = './../../../../vars/temp/main.yml'
with open(var_file_path) as f:
    var_file = yaml.safe_load(f)
# list = var_file['package']


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def check_package(host):
    f = host.package(var_file['package'])
    assert f.is_installed

import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')
var_file_path = './../../vars/main.yml'
with open(var_file_path) as f:
    var_file = yaml.safe_load(f)


def test_hosts_file(host):
    package = host.package(var_file['package'])  # var_file['package']
    assert package.is_installed

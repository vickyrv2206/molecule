import os
import subprocess
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    files_list = subprocess.check_output(['whoami'])
    print(files_list)
    f = host.package("php")
    # f = "sample"
    assert f.is_installed

import os

import subprocess
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/home/ubuntu/testing/adada')
    files_list = subprocess.check_output(['whoami'])
    print(files_list)
    path1 = "/home/ubuntu/testing/adada"
    print(path1)
    out = os.path.exists(path1)
    print(out)
    # assert out
    assert f.exists
    assert f.user == "ubuntu"

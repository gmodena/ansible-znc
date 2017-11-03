import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_enabled(Service):
    service = Service('znc')
    assert service.is_enabled


def test_service_running(Service):
    service = Service('znc')
    assert service.is_running


def test_socket_listening_ipv4(Socket):
    socket = Socket('tcp://0.0.0.0:6666')
    assert socket.is_listening


def test_socket_listening_ipv6(Socket):
    socket = Socket('tcp://:::6666')
    assert not socket.is_listening

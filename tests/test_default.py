import pytest
import testinfra


def test_os_release_file(host):
    f = host.file('/etc/os-release')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_os_release_fedora(host):
    assert host.file("/etc/os-release").contains("Fedora")


def test_customos_group_exists(host):
    assert host.group("customos").exists
    assert host.group("customos").gid == 3000


def test_customos_user_exists(host):
    assert host.user("customos").exists
    assert host.user("customos").uid == 3000


@pytest.mark.parametrize("package", [
    "openssh-server",
    "zabbix-agent",
    "clamav-server",
    "clamav-data",
    "clamav-update",
    "clamav-filesystem",
    "clamav",
    "clamav-scanner-systemd",
    "clamav-devel",
    "clamav-lib",
    "clamav-server-systemd",
])
def test_agent_packages_are_installed(host, package):
    host.package(package).is_installed


def test_sshd_service_is_active_and_enabled(host):
    assert host.service("sshd").is_running
    assert host.service("sshd").is_enabled


def test_firewalld_service_is_active_and_enabled(host):
    assert host.service("firewalld").is_running
    assert host.service("firewalld").is_enabled


@pytest.mark.parametrize("service", [
    "clam-freshclam",
    "clamd@scan",
])
def test_clamav_services_are_stopped_and_disabled(host, service):
    assert host.service(service).is_running is False
    assert host.service(service).is_enabled is False


def test_zabbix_service_is_stopped_and_disabled(host):
    assert host.service("zabbix-agent").is_running is False
    assert host.service("zabbix-agent").is_enabled is False

# file lib/ansible/module_utils/facts/system/distribution.py:470-509
# lines [470, 471, 480, 484, 487, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 505, 506, 507, 508]
# branches ['506->507', '506->510', '507->506', '507->508']

import pytest
from ansible.module_utils.facts.system.distribution import Distribution

def test_distribution_os_family_map():
    # Ensure that the OS_FAMILY_MAP is correctly populated
    assert 'RedHat' in Distribution.OS_FAMILY_MAP
    assert 'Debian' in Distribution.OS_FAMILY_MAP
    assert 'Suse' in Distribution.OS_FAMILY_MAP
    assert 'Archlinux' in Distribution.OS_FAMILY_MAP
    assert 'Mandrake' in Distribution.OS_FAMILY_MAP
    assert 'Solaris' in Distribution.OS_FAMILY_MAP
    assert 'Slackware' in Distribution.OS_FAMILY_MAP
    assert 'Altlinux' in Distribution.OS_FAMILY_MAP
    assert 'SGML' in Distribution.OS_FAMILY_MAP
    assert 'Gentoo' in Distribution.OS_FAMILY_MAP
    assert 'Alpine' in Distribution.OS_FAMILY_MAP
    assert 'AIX' in Distribution.OS_FAMILY_MAP
    assert 'HP-UX' in Distribution.OS_FAMILY_MAP
    assert 'Darwin' in Distribution.OS_FAMILY_MAP
    assert 'FreeBSD' in Distribution.OS_FAMILY_MAP
    assert 'ClearLinux' in Distribution.OS_FAMILY_MAP
    assert 'DragonFly' in Distribution.OS_FAMILY_MAP
    assert 'NetBSD' in Distribution.OS_FAMILY_MAP

def test_distribution_os_family():
    # Ensure that the OS_FAMILY is correctly populated
    assert Distribution.OS_FAMILY['RedHat'] == 'RedHat'
    assert Distribution.OS_FAMILY['Fedora'] == 'RedHat'
    assert Distribution.OS_FAMILY['CentOS'] == 'RedHat'
    assert Distribution.OS_FAMILY['Debian'] == 'Debian'
    assert Distribution.OS_FAMILY['Ubuntu'] == 'Debian'
    assert Distribution.OS_FAMILY['SuSE'] == 'Suse'
    assert Distribution.OS_FAMILY['Archlinux'] == 'Archlinux'
    assert Distribution.OS_FAMILY['Mandrake'] == 'Mandrake'
    assert Distribution.OS_FAMILY['Solaris'] == 'Solaris'
    assert Distribution.OS_FAMILY['Slackware'] == 'Slackware'
    assert Distribution.OS_FAMILY['Altlinux'] == 'Altlinux'
    assert Distribution.OS_FAMILY['SGML'] == 'SGML'
    assert Distribution.OS_FAMILY['Gentoo'] == 'Gentoo'
    assert Distribution.OS_FAMILY['Alpine'] == 'Alpine'
    assert Distribution.OS_FAMILY['AIX'] == 'AIX'
    assert Distribution.OS_FAMILY['HPUX'] == 'HP-UX'
    assert Distribution.OS_FAMILY['MacOSX'] == 'Darwin'
    assert Distribution.OS_FAMILY['FreeBSD'] == 'FreeBSD'
    assert Distribution.OS_FAMILY['Clear Linux OS'] == 'ClearLinux'
    assert Distribution.OS_FAMILY['DragonflyBSD'] == 'DragonFly'
    assert Distribution.OS_FAMILY['NetBSD'] == 'NetBSD'

#
# (c) 2022, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from unittest import TestCase

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.utils.utils import Version


class TestIosxrUtils(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_VersionOperation(self):
        self.assertEqual(Version("3.0.1") < Version("3.1.0"), True)
        self.assertEqual(Version("0.0.1") < Version("3.1.0"), True)
        self.assertEqual(Version("3.0.1") < Version("3.0.1"), False)
        self.assertEqual(Version("3.0.1") <= Version("3.0.1"), True)
        self.assertEqual(Version("4.0.1") > Version("3.0.1"), True)
        self.assertEqual(Version("4.1.1") > Version("4.1.0"), True)
        self.assertEqual(Version("4.1.1") == Version("4.1.1"), True)

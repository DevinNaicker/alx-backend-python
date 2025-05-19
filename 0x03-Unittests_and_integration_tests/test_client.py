#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class"""
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        from client import GithubOrgClient
        client = GithubOrgClient(org_name)
        org = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        self.assertEqual(org, {"login": "mocked_org"})
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()

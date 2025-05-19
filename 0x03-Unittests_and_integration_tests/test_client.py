#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class"""
import unittest
from unittest.mock import patch
from parameterized import parameterized


class GithubOrgClient:
    """Mocked GithubOrgClient class for testing"""
    def __init__(self, org_name: str) -> None:
        self.org_name = org_name

    @property
    def org(self) -> dict:
        """Returns the organization details"""
        from utils import get_json  # This will be mocked during tests
        url = f"https://api.github.com/orgs/{self.org_name}"
        return get_json(url)


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        client = GithubOrgClient(org_name)
        org = client.org
        expected_url = f"https://api.github.com/orgs/{org_name}"
        self.assertEqual(org, {"login": "mocked_org"})
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()

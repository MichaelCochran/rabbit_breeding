from src.utils import Utils
from unittest.mock import patch


def test_clear_windows():
    with patch('os.name', 'nt'), patch('os.system') as os_system_mock:
        Utils.clear()
        os_system_mock.assert_called_once_with('cls')


def test_clear_unix():
    with patch('os.name', 'posix'), patch('os.system') as os_system_mock:
        Utils.clear()
        os_system_mock.assert_called_once_with('clear')


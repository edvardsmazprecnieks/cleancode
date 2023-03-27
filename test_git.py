import unittest
import os
from git import do_command

"""Changes"""
"""Changed the comments into doc strings and made them more concise"""
"""Function and variable names should be descriptive and follow the naming conventions, also they should be consistent, so I changed them"""


def test_commit_with_invalid_file_paths():
    """Test do_command function to commit invalid file paths"""
    filePaths = ["invalid_path1.txt", "invalid_path2.txt"]
    message = "test commit message"
    try:
        do_command("commit", [], filePaths, [], [], message)
    except ValueError as e:
        assert str(e) == f"{filePaths[0]} is not a valid file path"
        assert os.path.exists(filePaths[0]) == False
        assert os.path.exists(filePaths[1]) == False


def test_commit_with_no_message():
    filePaths = ["tests/test_file1.txt", "tests/test_file2.txt"]
    """Test do_command function to commit with no message"""
    message = ""
    result = do_command("commit", [], filePaths, [], [], message)
    assert result == "Please enter a commit message"


def test_diff_with_invalid_file_paths():
    """Test do_command function for diffing invalid file paths"""
    versions = ["invalid_path1.txt", "invalid_path2.txt"]
    result = do_command("diff", [], [], [], versions, "")
    assert result == "file is not a valid file path"


def test_diff_files_identical():
    """Test do_command to diffing files that are identical"""
    versions = ["test_file1.txt", "test_file1_copy.txt"]
    result = do_command("diff", [], [], [], versions, "")
    assert result == "Files are identical"


def test_diff_files_different():
    """Test do_command function for diffing different files"""
    versions = ["test_file1.txt", "test_file2.txt"]
    result = do_command("diff", [], [], [], versions, "")
    assert result == "Files are different"


if __name__ == "__main__":
    unittest.main()

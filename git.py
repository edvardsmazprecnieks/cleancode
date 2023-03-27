import os
import filecmp

"""Changes"""
"""The names should be descriptive and concise, also they should follow a uniformly conventions"""
"""Bloaters - Instead of using nested if statements, I use guard classes to simplify the code. so I created a set of classes that each have a single responsibility to validate one of the conditions."""
"""Simplified the commit function by using the all function to check if all file paths exist, instead of using a for loop"""


def do_command(command, pathSpecs, filePaths, pathsToShowLogFor, versions, message):
    """
    Executes the specified Git command with the given arguments.

    Args:
        command (str): The Git command to execute.
        pathSpecs (list): A list of file path patterns to include in the command.
        filePaths (list): A list of file paths to include in the command.
        pathsToShowLogFor (list): A list of file paths to show logs for.
        versions (list): A list of versions to compare for the "diff" command.
        message (str): The commit message to use for the "commit" command.

    Returns:
        str: The result of the Git command.

    Raises:
        TypeError: If any of the input arguments are not lists.
        ValueError: If the "diff" command is used with a number of versions other than 2,
                    or if any of the specified file paths do not exist for the "commit" command.
    """
    if not isinstance(pathSpecs, list):
        raise TypeError("pathSpecs should be a list")
    if not isinstance(filePaths, list):
        raise TypeError("filePaths should be a list")
    if not isinstance(pathsToShowLogFor, list):
        raise TypeError("pathsToShowLogFor should be a list")
    if not isinstance(versions, list):
        raise TypeError("versions should be a list")

    if command == "status":
        return status(pathSpecs)
    elif command == "commit":
        return commit(filePaths, message)
    elif command == "log":
        return log(pathsToShowLogFor)
    elif command == "diff":
        if len(versions) != 2:
            raise ValueError("diff command requires exactly 2 versions")
        return diff(versions[0], versions[1])
    else:
        return f"{command} is not supported by git"


def status(file_path_patterns):
    return f"Status for: {', '.join(pathSpecs)}"


def commit(file_paths, message):
    if not message:
        return "Please enter a commit message"
    if not all(os.path.exists(path) for path in file_paths):
        raise ValueError("One or more file paths are not valid")
    return f"Committed: {', '.join(file_paths)}"


def log(pathsToShowLogFor):
    return f"Log for: {', '.join(pathsToShowLogFor)}"


def diff(file1, file2):
    if not os.path.exists(file1):
        return "file is not a valid file path"
    if not os.path.exists(file2):
        return "file is not a valid file path"
    # Compare two files using filecmp
    if filecmp.cmp(file1, file2):
        return "Files are identical"
    else:
        return "Files are different"

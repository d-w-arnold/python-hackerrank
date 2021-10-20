import os
import sys


def generate_packages(sep: str, path: str):
    """
    Recursively create Python packages (dirs and `__init__.py` files in newly created dirs), from a given path.

    Example usage: `python main.py --path InterviewPreparationKit/Miscellaneous`

    Result: (Will create each if they each do not already exist)
    src/InterviewPreparationKit/
    src/InterviewPreparationKit/__init__.py
    src/InterviewPreparationKit/Miscellaneous/
    src/InterviewPreparationKit/Miscellaneous/__init__.py
    tests/InterviewPreparationKit/
    tests/InterviewPreparationKit/__init__.py
    tests/InterviewPreparationKit/Miscellaneous/
    tests/InterviewPreparationKit/Miscellaneous/__init__.py

    :param sep: The separator to break down the path provided.
    :param path: The path to recursively create Python packages for.
    """
    if path.split(sep, maxsplit=1)[0] in ("src", "tests"):
        path = path.split(sep, maxsplit=1)[1]
    packages = path.split(sep)
    if packages[0] == path:
        print(f'Error: --path {path} does not contain --sep "{sep}"')
        sys.exit(1)
    generate_packages_helper(packages, os.path.join(os.getcwd(), "src"))
    generate_packages_helper(packages, os.path.join(os.getcwd(), "tests"))


def generate_packages_helper(packages, tmp_path):
    for i in packages:
        tmp_path = os.path.join(tmp_path, i)
        if not os.path.exists(tmp_path):
            os.makedirs(tmp_path)
            print("New dir:\t", tmp_path)
        tmp_path_init = os.path.join(tmp_path, "__init__.py")
        if not os.path.exists(tmp_path_init):
            open(tmp_path_init, "a")
            print("New file:\t", tmp_path_init)


def main(sep, path):
    generate_packages(sep, path)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Add a module path to both src and tests modules in repo.')
    parser.add_argument('--sep', required=True, help='The separator to break down the path provided.')
    parser.add_argument('--path', required=True, help='The path to recursively create Python packages for.')
    args = parser.parse_args()
    main(sep=args.sep, path=args.path)

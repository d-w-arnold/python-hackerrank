import os


def generate_packages(path: str):
    if path.split("/", maxsplit=1)[0] in ("src", "tests"):
        path = path.split("/", maxsplit=1)[1]
    packages = path.split("/")
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
            print("New file:\t", tmp_path)


def main(path):
    generate_packages(path)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Add a module path to both src and tests modules in repo.')
    parser.add_argument('--path', metavar='path', required=True, help='The module path to add.')
    args = parser.parse_args()
    main(path=args.path)

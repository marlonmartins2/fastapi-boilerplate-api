from io import open

read_version = lambda filename: open(filename, "r", encoding="utf-8").read()

""" It defines the project current version """
__version__ = read_version(".version").strip()

if __name__ == "__main__":
    print(__version__)

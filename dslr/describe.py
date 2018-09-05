from argparse import ArgumentParser
import sys
import pandas as pd


def run(args):
    parser = ArgumentParser()
    parser.add_argument('file_path',
                        type=str,
                        help='path to csv file')
    file_path = parser.parse_args(args).file_path
    data = pd.read_csv(file_path)
    print(data)


if __name__ == '__main__':
    run(sys.argv[1:])

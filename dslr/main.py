import sys
from argparse import ArgumentParser
from .describe import run as describe


class Dispatcher:
    def __init__(self):
        parser = ArgumentParser()
        parser.add_argument('command',
                            choices=['describe',
                                     'histogram',
                                     'scatter_plot',
                                     'pair_plot',
                                     'logreg_train',
                                     'logreg_predict'])
        command = parser.parse_args(sys.argv[1:2]).command
        getattr(self, command)(sys.argv[2:])

    @staticmethod
    def describe(args):
        describe(args)

    @staticmethod
    def histogram(args):
        ...

    @staticmethod
    def scatter_plot(args):
        ...

    @staticmethod
    def pair_plot(args):
        ...

    @staticmethod
    def logreg_train(args):
        ...

    @staticmethod
    def logreg_predict(args):
        ...


def main():
    Dispatcher()


if __name__ == '__main__':
    main()

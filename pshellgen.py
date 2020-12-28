#!/bin/env python3.8
import sys
import argparse

# translate normal text into hex and the into binary as different separated funcitons


class Translator():
    def __init__(self, hexstring: str):
        self.hexstring = hexstring

    def translate(self):
        print(self.hexstring)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", "-p", dest="payload_string", type=str, required=True,
                        help="specify payload in hex for translation")
    parser.add_argument("--out", "-o", dest="payload_string", type=str, required=False,
                        help="specify payload in hex for translation")
    return parser.parse_args()


def main():
    sys.argv[1]


if __name__ == '__main__':
    main()

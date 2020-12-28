#!/bin/env python3.8
import sys
import argparse

# normal string -> hexstring -> bytes
# translate normal text into hex and the into binary as different separated funcitons


class Translator():
    def __init__(self, normal_string, hexstring: str):
        self.normal_string = normal_string
        self.hexstring = hexstring
        self.bytestring = None

    def translate(self):
        self.hexstring


class Outputter():
    def __init__(self, filename: str, hexstring: str):
        self.filename = filename
        self.hexstring = hexstring

    # def print_binary():
        # sys.

    def save_to_file(self):
        with open(self.filename, "wb") as f:
            f.write(self.hexstring)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", "-p", dest="payload_string", type=str, required=True,
                        help="specify payload string in hex for translation")
    parser.add_argument("--out", "-o", dest="outfile", type=str, required=False,
                        help="specify file to save result to")
    return parser.parse_args()


def main():
    args = parse_args()
    print(args.payload_string)




if __name__ == '__main__':
    main()

#!/bin/env python3.8
import sys
import argparse

# normal string -> hexstring -> bytes
# translate normal text into hex and the into binary as different separated funcitons

# 's="string"; x=b"lol"; print(bytes(s,"utf-8"), x); f=open("FILE", "wb");
# f.write(bytes(s, "ascii"));f.close()'


class Translator():
    def __init__(self, normal_string):
        self.normal_string = normal_string
        self.bytestring = None

    def translate(self):
        self.bytestring = bytes(self.normal_string, "utf-8")


class Outputter():
    def __init__(self, outfile: str, bytes: str):
        self.outfile = outfile
        self.bytes = bytes

    def save_to_file(self):
        with open(self.outfile, "wb") as f:
            f.write(self.bytes)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--payload", "-p", dest="payload_string", type=str, required=True,
                        help="specify payload string in hex for translation")
    parser.add_argument("--out", "-o", dest="outfile", type=str, required=False,
                        help="specify file to save result to")
    return parser.parse_args()


def main():
    args = parse_args()
    original_string = args.payload_string
    outfile = args.outfile

    t = Translator(original_string)
    t.translate()
    bytes = t.bytestring

    o = Outputter(outfile, bytes)
    o.save_to_file()


if __name__ == '__main__':
    main()

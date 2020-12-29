#!/bin/env python3.8
import sys
# import argparse

# normal string -> hexstring -> bytes
# translate normal text into hex and the into binary as different separated funcitons

# this works move from this
# python3.8 -c 'buf=("\x90"*184);f=open("payload_diablos", "wb");f.write(bytes(buf, "utf-8"));f.close;'


class Translator:
    def __init__(self, normal_string):
        self._normal_string = normal_string
        self.bytestring = None

    def translate(self):
        self.bytestring = bytes(self._normal_string, "utf-8")


class PayloadGenerator:
    def __init__(self, filename: str, opcode: str, opcode_qty: int):
        self.filename = filename
        self.opcode = bytes(opcode, "utf-8")
        self.opcode_qty = opcode_qty
        self.payload = None

    def generate_payload(self):
        self.payload = self.opcode * self.opcode_qty

    def save_to_file(self):
        f = open(f"{self.filename}.bytes", "wb")
        f.write(self.payload)
        f.close()


# def parse_args():
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--payload", "-p", dest="payload_string", type=str, required=True,
    #                   # help="specify payload string in hex for translation")
    # parser.add_argument("--out", "-o", dest="filename", type=str, required=False,
    #                   # help="specify file to save result to")
    # return parser.parse_args()


def main():
    # args = parse_args()
    # original_string = args.payload_string
    # filename = args.filename

    if len(sys.argv) != 2:
        print("specify string")
        sys.exit(1)

    filename = sys.argv[1]

    p = PayloadGenerator(filename, "\x90", 90)
    p.generate_payload()
    p.save_to_file()


if __name__ == '__main__':
    main()

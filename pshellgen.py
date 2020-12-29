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
        self.opcode = opcode
        self.opcode_qty = opcode_qty
        self.nop_slide = None
        self.payload = None

    def generate_nop_slide(self):
        self.nop_slide = bytes("\x90", "utf-8") * self.opcode_qty

    def save_to_file(self):
        self.generate_nop_slide()
        with open(f"{self.filename}.payload", "wb") as f:
            f.write(self.payload)


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

    if len(sys.argv) != 3:
        print("error in args")
        sys.exit(1)

    filename = sys.argv[1]
    opcode = sys.argv[2]

    p = PayloadGenerator(filename, 90)
    p.save_to_file()


if __name__ == '__main__':
    main()

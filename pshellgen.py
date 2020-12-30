#!/bin/env python3.8
import sys


# this is probably useless
class Translator:
    def __init__(self, normal_string):
        self._normal_string = normal_string
        self.bytestring = None

    def translate(self):
        self.bytestring = bytes(self._normal_string, "utf-8")


class PayloadFileGenerator:
    def __init__(self, filename: str, nop_slide_length: int, payload: str):
        self.filename = filename
        self.nop_slide_length = nop_slide_length
        self.payload = payload
        self.nop_slide = None

    def _generate_nop_slide(self):
        self.nop_slide = b"\x90" * self.nop_slide_length

    def save_to_file(self):
        self._generate_nop_slide()
        with open(f"{self.filename}.payload", "wb") as f:
            f.write(self.nop_slide + bytes(self.payload, "utf-8"))


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

    if len(sys.argv) != 4:
        print("error in args")
        sys.exit(1)

    filename = sys.argv[1]
    length = int(sys.argv[2])
    payload = sys.argv[3]

    fileGen = PayloadFileGenerator(filename, length, payload)
    fileGen.save_to_file()


if __name__ == '__main__':
    main()

#!/bin/env python3.8
import sys
import argparse


class PayloadFileGenerator:
    def __init__(self, filename: str, nop_slide_length: int, payload: str):
        self.filename = filename
        self.nop_slide_length = nop_slide_length
        self.payload = payload
        self.nop_slide = None
        self._generate_nop_slide()

    def _generate_nop_slide(self):
        self.nop_slide = b"\x90" * self.nop_slide_length

    def generate_payload_file(self):
        with open(f"{self.filename}.payload", "wb") as f:
            f.write(self.nop_slide + bytes(self.payload, "utf-8"))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--outfile", "-o", dest="outfile", type=str, required=True,
                        help="file save payload to")
    parser.add_argument("--length", "-l", dest="nop_slide_length", type=int, required=True,
                        help="length of the NOP slide")
    parser.add_argument("--payload", "-p", dest="payload", type=str, required=True,
                        help="your custom payload")
    return parser.parse_args()


def main():
    args = parse_args()

    filename = args.outfile
    length = args.nop_slide_length
    payload = args.payload

    fileGen = PayloadFileGenerator(filename, length, payload)
    fileGen.generate_payload_file()


if __name__ == '__main__':
    main()

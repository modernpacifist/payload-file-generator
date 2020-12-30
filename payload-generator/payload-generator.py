#!/bin/env python3.9

import codecs
from argparse import ArgumentParser


class PayloadGenerator:
    def __init__(self, length: int, payload: str = None, shellcode: str = None, filename: str = None):
        self.length = length
        self.payload = payload
        self.shellcode = shellcode
        self.filename = filename

        self.nop_slide = None
        self.generated_payload = None

        self._generate_payload()

    def _generate_payload(self):
        self.nop_slide = b"\x90" * self.length
        if self.payload:
            self.generated_payload = self.nop_slide + bytes(self.payload, "utf-8")

        if self.shellcode:
            self.generated_payload = self.nop_slide + codecs.decode(self.shellcode.encode(), "hex")

        if not self.filename:
            print(f"{self.generated_payload}")
        else:
            with open(f"{self.filename}.payload", "wb") as f:
                f.write(self.generated_payload)


def get_args():
    parser = ArgumentParser()
    parser.add_argument("-l", '--length', dest="length", type=int, required=True,
                        help='length of the nop slide')
    parser.add_argument("-p", '--payload', dest="payload", type=str, required=False,
                        help='specify payload in plain text')
    parser.add_argument("-s", '--shellcode', dest="shellcode", type=str, required=False,
                        help='specify payload in shellcode')
    parser.add_argument("-f", '--filename', dest="filename", type=str, required=False,
                        help='specify payload in shellcode')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    generator = PayloadGenerator(args.length, args.payload, args.shellcode, args.filename)

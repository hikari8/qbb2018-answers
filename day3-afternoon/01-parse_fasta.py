#!/usr/bin/env python3

"""
Parse all FASTA records from stdin and print id and sequence
"""

import sys

class FASTAReader( object ):

    def __init__( self, file ):
        self.last_ident = None
        self.file = file
        self.eof = False

    def next(self):
        if self.eof:
            return None, None
        if self.last_ident is not None:
            # Not first line
            ident = self.last_ident
        else:
            # First line
            line = self.file.readline()
            if line == "":
                return None, None
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\r\n")

        sequences = []
        while True:
            line = self.file.readline()
            if line == "":
                self.eof = True
                break
            elif not line.startswith(">"):
                sequences.append( line.strip() )
            else:
                self.last_ident = line[1:].rstrip("\r\n")
                break
        
        sequence = "".join( sequences )
        return ident, sequence

## WHAT I WANT!

reader = FASTAReader( sys.stdin )

while True:
    ident, sequence = reader.next() 
    if ident is None:
        break
    print( ident, sequence )
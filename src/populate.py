import logging
import os
import sys
import argparse
from sds.SdsQuery import query_rag

from sds.SdsReader import loadDocumentsInDir
from sds.SdsSpitter import addToChromadb, splitDocuments


def main():
    """ Extract a specified file
    """
    logging.basicConfig(level=logging.DEBUG)
    documents = loadDocumentsInDir("./src/sds/samples")
    chunks = splitDocuments(documents)
    addToChromadb(chunks)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

import argparse

parser = argparse.ArgumentParser()
_ = parser.add_argument('--date')
_ = parser.add_argument('rest', nargs='*')
parser.parse_args(['foo', 'bar', 'baz', '--date', 'wat'])
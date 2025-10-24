import argparse
from . import profiler, cleaner, splitter, encoder
import sys

def main():
    parser = argparse.ArgumentParser(prog='ml_utils', description='ML Utilities CLI')
    sub = parser.add_subparsers(dest='cmd')

    p_prof = sub.add_parser('profiler', help='Profile a CSV dataset')
    p_prof.add_argument('csv', help='Path to CSV file')

    p_clean = sub.add_parser('cleaner', help='Clean a CSV dataset')
    p_clean.add_argument('csv', help='Path to CSV file')
    p_clean.add_argument('--out', help='Output CSV path', default='cleaned.csv')
    p_clean.add_argument('--strategy', choices=['mean','median','mode'], default='median')

    p_split = sub.add_parser('split', help='Stratified train/test split')
    p_split.add_argument('csv', help='Path to CSV file')
    p_split.add_argument('--target', required=True, help='Target column for stratify')
    p_split.add_argument('--train', type=float, default=0.8, help='Train fraction')
    p_split.add_argument('--out-dir', default='splits', help='Output folder')

    p_enc = sub.add_parser('encode', help='Label encode columns')
    p_enc.add_argument('csv', help='Path to CSV file')
    p_enc.add_argument('--cols', help='Comma separated columns to encode', required=True)
    p_enc.add_argument('--out', default='encoded.csv', help='Output CSV path')

    args = parser.parse_args()
    if args.cmd == 'profiler':
        profiler.profile(args.csv)
    elif args.cmd == 'cleaner':
        cleaner.clean(args.csv, args.out, args.strategy)
    elif args.cmd == 'split':
        splitter.split(args.csv, args.target, args.train, args.out_dir)
    elif args.cmd == 'encode':
        encoder.encode(args.csv, args.cols.split(','), args.out)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()

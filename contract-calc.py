from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)

parser.add_argument('price', type=float, help='Phone price')
parser.add_argument('upfront', type=float, default=0, help='Upfront cost')
parser.add_argument('monthly', type=float, help='Monthly cost')
parser.add_argument(
    '-t', '--term', type=float, default=24, help='Contract term'
)

if __name__ == '__main__':
    args = parser.parse_args()
    print('Phone price: %.2f.' % args.price)
    print('Upfront cost: %.2f.' % args.upfront)
    print('Monthly cost: %.2f.' % args.monthly)
    print('Contract term: %.2f months.' % args.term)
    base = (args.monthly * args.term) + args.upfront
    base -= args.price
    base /= args.term
    print('Contract price: %.2f PCM.' % base)

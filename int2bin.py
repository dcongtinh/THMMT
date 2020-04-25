from optparse import OptionParser

parser = OptionParser()

parser.add_option('-n', '--num', type=int, default=2020)
parser.add_option('-l', '--length', type=int, default=8)
(options, args) = parser.parse_args()

n = options.num
l = options.length


bin_str = bin(n)[2:]
while len(bin_str) < l:
    bin_str = '0' + bin_str

print(bin_str)

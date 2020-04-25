from optparse import OptionParser

parser = OptionParser()

parser.add_option('-n', '--num', type=str, default='11111100100')
(options, args) = parser.parse_args()

n_str = options.num
print(int(n_str, 2))

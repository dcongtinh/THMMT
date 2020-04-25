from optparse import OptionParser
from prettytable import PrettyTable

parser = OptionParser()

parser.add_option('-a', '--IP', type=str, default='10.0.0.0')
parser.add_option('-n', '--network', type=int, default=24)
parser.add_option('-s', '--subnet', type=int, default=6)
(options, args) = parser.parse_args()

ip = options.IP
network = options.network
subnet = options.subnet
n_sub = len(bin(subnet+1)[2:])


def int2bin(n, l=8):
    bin_str = bin(n)[2:]
    while len(bin_str) < l:
        bin_str = '0' + bin_str
    return bin_str


def bin2int(s):
    return str(int(s, 2))


print(ip + '/' + str(network))
a = ip.split('.')
ip_str = ''

for i in ip.split('.'):
    ip_str += int2bin(int(i))


def str2ip(s):
    return bin2int(s[:8]) + '.' + bin2int(s[8:16]) + '.' + bin2int(s[16:24]) + '.' + bin2int(s[24:32])


def str2broadcast(s, network):
    return str2ip(s[:network] + len(s[network:])*"1")


def str2netmask(network):
    return str2ip(network*"1" + (32-network)*"0")


def textcolor_display(text):
    begin = '\033[96m'
    end = '\033[00m'
    return str(begin + text + end)


table = PrettyTable(['Network', 'DEC', 'BIN1', 'BIN2',
                     'BIN3', 'BIN4', 'Broadcast', 'Netmask'])
table.align['DEC'] = 'l'
table.align['Broadcast'] = 'l'
table.add_row(['Net0', str2ip(ip_str), ip_str[:8], ip_str[8:16],
               ip_str[16:24], ip_str[24:32], str2broadcast(ip_str, network), str2netmask(network)])

for i in range(2**n_sub):
    bin_str = int2bin(i, n_sub)
    ip_str_tmp = ip_str
    s = ip_str[:network] + bin_str + ip_str[network+n_sub:]
    table.add_row(['SubNet' + str(i+1), str2ip(s), s[:8],
                   s[8:16], s[16:24], s[24:32], str2broadcast(s, network + n_sub), str2netmask(network+n_sub)])

print(table)

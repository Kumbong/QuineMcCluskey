from qm.qm import QM
import argparse


parser = argparse.ArgumentParser(description='Enter minterms and don\'t cares')
parser.add_argument('minterms', metavar='m', type=str, nargs='+',
help='comma seperated list of minterms to be reduced')
parser.add_argument("-d", "--dont_cares", default="", help="comma seperated list of don't cares")
parser.add_argument("-v", "--variables", default="", help="comma seperated list of variables")
args = parser.parse_args()

minterms  = args.minterms[0].split(',')

if args.dont_cares:
    dcares = args.dont_cares.split(',')
else:
    dcares = []

if args.variables:
    variables = args.variables.split(',')
else:
    variables = ['x'+str(i) for i in range(len(minterms)+len(dcares))]


c = QM(minterms,dcares,variables)
print(c.pis())
epis = c.primary_epis()
print(epis)

chars = list(map(lambda x: c.to_char(x,variables),epis))
print(chars)

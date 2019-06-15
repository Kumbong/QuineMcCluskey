from core.qm.qm import QM
import argparse


parser = argparse.ArgumentParser(description='Quine McCluskey Circuit Minimizer')
parser.add_argument('minterms', metavar='m', type=str, nargs='+',
help='comma seperated list of minterms to be reduced')
parser.add_argument("-d", "--dont_cares", default="", help="comma seperated list of don't cares")
parser.add_argument("-v", "--variables", default="", help="comma seperated list of variables")
#parser.add_argument("-ss", "--show_steps", default="yes", help="show steps leading to solution")

args = parser.parse_args()

minterms  = args.minterms[0].split(',')

if args.dont_cares:
    dcares = args.dont_cares.split(',')
else:
    dcares = []

if args.variables:
    variables = args.variables.split(',')
else: 
    variables = []

c = QM(minterms,dcares,variables)


#solve and print the solution
print('Prime implicants')
print(c.pis())

print('Essential prime implicants')
epis = c.primary_epis()


print(epis)
print('Essential prime implicants in variable form')
chars = list(map(lambda x: c.to_char(x,variables),epis))
print(chars)

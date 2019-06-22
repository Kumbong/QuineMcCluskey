from core.qm.qm import QM
import argparse

#TODO
#add validation for variables from CLI and GUI


#used to check if a string can be an integer 
def representsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

####### read and parse arguments from the command line ######################
parser = argparse.ArgumentParser(description='Quine McCluskey Circuit Minimizer')
parser.add_argument('minterms', metavar='m', type=str, nargs='+',
help='comma seperated list of minterms to be reduced')
parser.add_argument("-d", "--dont_cares", default="", help="comma seperated list of don't cares")
parser.add_argument("-v", "--variables", default="", help="comma seperated list of variables")
parser.add_argument("-s", "--show_steps", default="yes", help="show steps leading to solution")

args = parser.parse_args()

minterms  = args.minterms[0].split(',')

#make sure all the values in the values entered for minterms are valid integers
for mt in minterms:
    #if it is not a whitespace and it is not an integer 
    if (mt and not representsInt(mt)) or ((mt and representsInt(mt)) and int(mt) < 0):
        raise argparse.ArgumentTypeError('Integer values expected for minterms')

#make sure all the values in the values entered for dont cares are valid integers
if args.dont_cares:
    dcares = args.dont_cares.split(',')
    #make sure the don't cares are all integer values
    for dc in dcares:
        if (dc and not representsInt(dc)) or ((dc and representsInt(dc)) and int(dc) < 0):
            raise argparse.ArgumentTypeError('Integer values expected for don\'t cares')
else:
    dcares = []

##################################add validation for variables here ####################
if args.variables:
    variables = args.variables.split(',')
else: 
    variables = []

#make sure show steps is either a yes or a no 
if args.show_steps.lower() != 'yes' and args.show_steps.lower() != 'no':
    raise argparse.ArgumentTypeError('show_steps expects yes or no')
    
#simply expression and print solution if necessary
qm = QM(minterms,dcares,variables)
# pis = qm.pis()
# epis = qm.primary_epis()
# sepis =  qm.secondary_epis()

sols = qm.minimize()
if args.show_steps == 'yes':
    print(qm.procedure)

else:
    print('Solution')
    print(sols[0])

    if len(sols)>1:
        for i in range(1,len(sols)):
            print(sols[i])


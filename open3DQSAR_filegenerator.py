import random
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--input', type=str, default=None, help='Path to a .txt file specifying the input')
parser.add_argument('--trn', type=int, default=None, help='Numbers of compounds in training set')
parser.add_argument('--tsn', type=int, default=None, help='Numbers of compounds in test set')
parser.add_argument('--num', type=int, default=None, help='How many new files are to be generated')
args = parser.parse_args()


def make_random_string(trn, tsn):
    # Generate tsn unique random numbers between 1 and trn
    nums = random.sample(range(1, trn + 1), tsn)
    nums.sort()
    return ",".join(str(n) for n in nums)

def modify_line_by_match(filename, match_text, new_text, number):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if match_text in line:
            lines[i] = new_text + "\n"
            break

    with open(filename.split('.')[0]+'_'+str(number)+'.txt', 'w') as f:
        f.writelines(lines)

ls=[]
for i in range(args.num):
    ls.append(make_random_string(args.trn,args.tsn))

filename=args.input


if __name__ == '__main__':
   for i in range(len(ls)):
       modify_line_by_match(filename,"set id_list=","set id_list="+str(ls[i])+" attribute=testset", i)

   
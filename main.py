from read_file import read_file
from write_file import write_file
from Validator import validator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', type=str, default="D:\\11.txt", help='Input path')
parser.add_argument('--output', type=str, default="C:\\Users\\User\\Desktop\\output.txt", help='Output path')
args = parser.parse_args()

array = validator(read_file(args.input).read_file())
valid = array.count_valid_records()
invalid = array.count_invalid_records()
result = array.count_invalid_arguments()
write_file(args.output).write_file(array)

print("Count valid records " + str(valid))
print("Count invalid records " + str(invalid))
print(result)








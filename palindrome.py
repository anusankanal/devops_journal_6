import sys

if len(sys.argv)!=2:
  print("Usage:python palindrome.py <string>")
sys.exit(1)

input_str=sys.argv[1]
if input_str==input_str[::-1]:
  print(f"{input_str}" is apalindrome.')
else:
  print(f"{input_str}" is apalindrome.')

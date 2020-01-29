import sys

def setup(routing_table, ip):
  # The compressed table is the first command line arg
  db_list = open(sys.argv[1]) 

  # IP list is second command line arg
  ip_list = open(sys.argv[2])

  for l in db_list.readlines():
    if (not l == '\n'):
      routing_table.append(l.split())
  
  for i in ip_list.readlines():
    if (not i == '\n'):
      ip.append(i[:-1])

def search_table(table, ip_address, file):
  # Search the routing table for each ip here and write to file
  print("placeholder")

def main():
  routing_table = []
  IPs = []

  # setup data structures
  setup(routing_table, IPs)

  # open file to write to
  res = open("res.txt", "w")

  # for each ip, look up on routing table
  for ip in IPs:
    search_table(routing_table, ip, res)

  res.close()
  

if __name__ == "__main__":
  main()
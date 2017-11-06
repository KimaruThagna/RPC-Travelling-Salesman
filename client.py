import rpyc

proxy = rpyc.connect('localhost', 7001)

print(' RECOGNIZED POINTS \n'
      'A-NAIROBI\n'
      'B-RONGAI\n'
      'C-KIAMBU\n'
      'D-THIKA\n'
      'E-KAREN\n'
      'F-OSOITA\n'
      'G-PARKLANDS\n')
StartPoint=input('Enter Your Starting town')
destination=input('Enter your Destination')
paths = proxy.root.line_counter(StartPoint,destination)

def header():
    return '=====================================================================\n' \
           '___________________________PATH FINDER________________\n' \
           '__________________THE TRAVELLING SALESMAN PROBLEM____________________\n' \
           '=====================================================================\n' \
           'RRECOGNIZED POINTS \n' \
           'A- NAIROBI \n' \
           'B- RONGAI \n' \
           'C-KIAMBU \n' \
           'D-THIKA \n' \
           'E- KAREN \n' \
           'F-OSOITA \n'\
           'G-PARKLANDS\n'
print(header(),paths)

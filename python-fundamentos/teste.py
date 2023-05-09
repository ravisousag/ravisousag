N = int(input())

while(N > 0):
  a = str(input())
  b = str(input())
  
  if a[-2::] == b[-2::]:
    print('encaixa')
  else:
    print('nao encaixa')
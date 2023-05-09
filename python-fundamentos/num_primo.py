N = int(input())

cont=0
while cont <=N:
  a = str(input())
  b = str(input())
  aa=a.strip()
  bb=b.strip()
  print(aa)
  print(bb)

  if aa[-2::] == bb[-2::]:
    print('encaixa')
  else:
    print('nao encaixa')
  cont += 1 + cont
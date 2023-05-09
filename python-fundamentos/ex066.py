count = soma = 0
while True:
   num = int(input('Digite um numero: '))
   if num == 999:
      break
   count += 1
   soma += num
print(f'Foram digitados {count} números e a soma entre eles é {soma}')
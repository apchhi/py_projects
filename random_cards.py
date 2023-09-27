# # random card
import random

znachenye = (6,7,8,9,10,"Valet","Dama","Korol","Tuz")
mast = ("bubi", "chervi", "kresti", "piki")

def main():
  for i in range(5):
    rand_znachenye = random.randint(0,9)
    get_znachenye = znachenye[rand_znachenye]
      
    gen_mast = random.randint(0,3)
    get_mast = mast[gen_mast]
    
    print(f'{i+1} card - {get_znachenye} {get_mast}')

main()
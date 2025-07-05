# #sync example:

# import time

# #step 1:
# print("pani ubalna suru..")
# time.sleep(5)
# print("pani ubal gaya.")

# #step 2:
# print("Roti banana shuru..")
# time.sleep(2)
# print("Roti ban gai.")

#async example:

import asyncio

async def pani_ubalo():
  print("pani ubalna suru..")
  await asyncio.sleep(5)
  print("pani ubal gaya.")


async def Roti_banao():
  print("Roti banana shuru..")
  await asyncio.sleep(3)
  print("Roti ban gai.")

async def main():
  await asyncio.gather(
    pani_ubalo(),
    Roti_banao()
  )
asyncio.run(main())

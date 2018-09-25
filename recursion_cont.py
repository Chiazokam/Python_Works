def get(self, key):
  start_slot = self.hash_function(key, len(self.slots))
  data = None
  stop = False
  found = False
  position = start_slot
  while self.slots[position] != None and \
  not found and not stop:
  if self.slots[position] == key:
  found = True
  data = self.data[position]
  else:
  position=self.rehash(position, len(self.slots))
  if position == start_slot:
  stop = True
  return data
def __getitem__(self, key):
  return self.get(key)
def __setitem__(self, key, data):
  self.put(key, data)

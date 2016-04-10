
def save(filename, contents):
  fh = open(filename, 'w')
  fh.write(contents)
  fh.close()

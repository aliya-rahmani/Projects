# Write
with open("containers.txt", "w") as file_to_write:
  file_to_write.write("Pod/n")
  file_to_write.write("Service/n")
  file_to_write.write("Volume/n")
  file_to_write.write("Namespace/n")


# Read
with open("containers.txt") as file_to_read:
  lines = file_to_read.readlines()
  print(lines)

# Output: ['Pod\n', 'Service\n', 'Volume\n', 'Namespace\n']

# Generator
def process_file_lazily():

  with open("containers.txt") as file_to_read:
    for line in file_to_read.readlines():
      yield line


# Create generator
pipeline = process_file_lazily()
# convert to lowercase
lowercase = (line.lower() for line in pipeline)
# print first processed line
print(next(lowercase))

# Output: pod

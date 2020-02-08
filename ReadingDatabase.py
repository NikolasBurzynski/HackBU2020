

file = open("database.txt", "r+");
data = file.read().replace("\n", " ").split(" ");
print(data);



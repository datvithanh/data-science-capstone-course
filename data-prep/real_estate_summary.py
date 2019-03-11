
apartments = []
s = set()
with open('data/apartments.txt', 'r') as f:
    for line in f:
        apartments.append(line.split('|')[:-1])
        s.add(line.split('|')[-2])
        
print(apartments)
print(len(s))

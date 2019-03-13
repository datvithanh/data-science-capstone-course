
apartments = []
with open('data/apartments.txt', 'r') as f:
    for line in f:
        apartments.append(line.split('|')[:-1])

filtered_apartments = [x for x in apartments if x[0]
                       != 'Thỏa thuận' and x[1] != 'Không xác định']
d = {}
for i in filtered_apartments:
    if i[-1] not in d.keys():
        d[i[-1]] = []
    d[i[-1]].append(float(i[0].replace(' triệu/tháng', '')) /
                    float(i[1].replace(' m²', '')))

for key, value in d.items():
    print(key, sum(value)/len(value)*1000000)

for key, value in d.items():
    print(key, len(value))

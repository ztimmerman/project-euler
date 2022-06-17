#Problem 17
ones_place = ['','one','two','three','four','five','six','seven','eight','nine']
tens_place = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

count = len(ones_place[1]) + len('thousand') #count for 1000 #11
#count for 100,200,300,400,500,600,700,800,900
for x in range(1,10,1):
    count += len(ones_place[x]+'hundred+')
#1-9
oneToNinetyNine = sum([len(x) for x in ones_place])
#Sum of all characters in numbers from ten to 19
oneToNinetyNine += sum([len(x) for x in ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']])
#20-99
for tens in tens_place[2:]:
    for ones in ones_place:
        oneToNinetyNine += len(tens+ones)
count += oneToNinetyNine
#101-999, exempting above
for x in range(1,10,1):
    count +=len(ones_place[x]+'hundred'+'and') * 99 + oneToNinetyNine

print(count)
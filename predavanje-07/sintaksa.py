# pass, break, continue
# count += 1
# count -= 1
# count *= 1
# count /= 1
# CTRL + C


count = 0

while True:
    if count == 1000:
        break
    count = count + 1
    if count % 2 == 0:
        print(count)
    else:
        print(count)
        continue
    print('----------')

    

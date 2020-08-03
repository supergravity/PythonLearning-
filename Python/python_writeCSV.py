import csv

titles=['computer','moniter','keyboard']
prices=['$9999','$2999','$399']

with open('price.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow(['items','price'])
    for t,p in zip(titles, prices):
        w.writerow([t,p])


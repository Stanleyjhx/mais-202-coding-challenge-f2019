import matplotlib.pyplot as plt
import csv

mortgage_id = []
rent_id = []
own_id = []

m_amount = 0
r_amount = 0
o_amount = 0

m_average = 0
r_average = 0
o_average = 0

with open("home_ownership_data.csv", "r") as f1:
    state_reader = csv.reader(f1)
    for line in state_reader:
        if line[1] == 'MORTGAGE':
            mortgage_id.append(line[0])
        elif line[1] == 'OWN':
            own_id.append(line[0])
        elif line[1] == 'RENT':
            rent_id.append(line[0])
with open("loan_data.csv", "r") as f2:
    amount_reader = csv.reader(f2)
    #update the amount
    for line in amount_reader:
        if line[0] in mortgage_id:
            m_amount += int(line[1])
        elif line[0] in own_id:
            o_amount += int(line[1])
        elif line[0] in rent_id:
            r_amount += int(line[1])

m_average = m_amount/len(mortgage_id)
r_average=r_amount/len(rent_id)
o_average=o_amount/len(own_id)

x =  ['MORTGAGE','OWN','RENT']
y =  [m_average,o_average,r_average]
#draw the figure
plt.bar(x, y, align =  'center')

plt.title('Average loan amounts per home ownership') 
plt.ylabel('Average own amount($)')
plt.xlabel('Home ownership')
plt.show()



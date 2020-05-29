applecost = 10
no_of_apples_per_dozen = 12
applewholesale = 10
applepurchased = int(input("Enter apples"))
insert2mango=20
insert3orange=50
if applepurchased>100:
    totalsale = no_of_apples_per_dozen*applepurchased*applecost
else:
    totalsale = applewholesale * applepurchased * applecost

print(totalsale)
print(insert2mango)
print(insert3orange)


print("How many kilometers did you run today?")
kms = input()
miles = round(float(kms)/1.609344, 3)
print(" Your {}km run was {}mi".format(kms, miles))
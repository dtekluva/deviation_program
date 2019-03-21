response_sample = {"mean_dev": 252, "original_list": [1,2,3,5,6], "xbar": [3,-6,-5,-6,7,]}

# print(response_sample)

print(f"X".center(8), f"X-Xbar".center(8), '\n')

for item in zip(response_sample["original_list"],response_sample["xbar"]):
    print(f"{item[0]}".center(8), f"{item[1]}".center(8))

print('\n',f"mean_dev".center(8) , f"{response_sample['mean_dev']}".center(8))


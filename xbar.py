_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x_bar_list = []
def xbar(_list):
        sum_ = sum(_list)
        mean = (sum_) / len(_list)
        for number in _list:
                dev = number - mean
                x_bar_list.append(dev)
        return x_bar_list
xbar(_list)
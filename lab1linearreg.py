hrs = [0, 1, 2, 3, 3, 5, 5, 6, 7, 7, 10, 5]
mar = [96, 85, 82, 74, 95, 68, 76, 58, 65, 75, 50, 84]

def com_slope(hrs, mar):
    n = len(hrs)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0

    for i in range(n):
        sum_x += hrs[i]
        sum_y += mar[i]
        sum_xy += hrs[i] * mar[i]
        sum_x2 += hrs[i] ** 2

    #formula
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    mean_x = sum_x / n
    mean_y = sum_y / n
    c = mean_y - m * mean_x

    return m, c

m, c = com_slope(hrs, mar)
print("Slope (b):", m)
print("Intercept (c):", c)

check = int(input("Enter the hours to predict marks:"))
X_pred = 9
Y_pred = c + m * X_pred
print(f"Predicted marks for {X_pred} hours:", Y_pred)

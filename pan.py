from sklearn.linear_model import LinearRegression

# Dữ liệu diện tích căn nhà
X = [[60], [80], [100], [120], [140]]  # Diện tích căn nhà (m2)

# Dữ liệu giá trị căn nhà tương ứng
y = [300, 400, 500, 600, 700]  # Giá trị căn nhà (nghìn đô la)

# Xây dựng mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, y)

# Trích xuất hệ số góc của mô hình
intercept = model.intercept_
coef = model.coef_

print("Hệ số của mô hình:", coef)
print("Hệ số góc của mô hình:", intercept)
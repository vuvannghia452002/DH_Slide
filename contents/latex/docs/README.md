[text](<Danh sách thành viên.md>)

# Khảo sát

[text](HRM.md)
[text](<Business Model Canvas.md>)
[text](<Quy trình nghiệp vụ.md>)

<!-- ## Yêu cầu (Requirement tttttt) -->
<!-- ### Tình hình hiện tại -->
<!-- Data Sources + Database storage + report -->
<!-- ### Yêu cầu cải tiến -->
<!-- Yêu cầu -->
<!-- ![alt text](image-3.png) -->
<!-- Phân tích xxxx theo xxxx -->

[text](<Khám phá dữ liệu.md>)

# Phân tích và Thiết kế

[text](<Kiến trúc hệ thống phân tích dữ liệu.md>) 
[text](<Quy trình ETL.md>)
[text](<Thực hiện ETL.md>)



<!-- ## Mô hình dữ liệu Logic -->
<!-- Mô hình dữ liệu OLAP   OLAP trung tên bên dướiii -->
<!-- ![alt text](image-5.png) -->
<!-- ![alt text](image-13.png) -->
<!-- # Mô hình OLTP -->
<!-- # Mô hình ERD -->
<!-- # Mô hình OLAP -->
<!-- Bảng mysql, ngôi sao -->
<!-- ![alt text](image-8.png) -->
<!-- Gạch chân, tô màu -->
<!-- Chuyển đổi OLTP sang OLAP -->
<!-- ![alt text](image-7.png) -->
<!-- ![alt text](image-6.png) -->

Xác định các chiều khái niệm
# Xác định các chiều khái niệm

<!-- Ghi thêm số lượng (3 phòng ban...) -->
<!-- 3,4,6,8 -->

![alt text](image-4.png)
🍀 Bước 1. Xác định các chiều (Dimension) và Giá trị phân tích (Facts) của khối dữ liệu

🍀 Bước 2: Xác định hệ thống các chiều
🌳 Ví dụ:
👉 khu vực của khách hàng thì cụ thể là các khu vực nào
👉 độ tuổi của khách hàng thì cụ thể là các độ tuổi nào
👉 sản phẩm thì cụ thể danh sách các sản phẩm là gì
👉 dữ liệu trong khoảng thời gian nào (mấy năm, mấy tháng)

<!-- ✍️ Hướng dẫn: Bạn sử dụng tính năng remove duplicate với từng cột dữ liệu để tạo ra từng chiều rồi copy vào một sheet. -->

<!-- ! -->
<!-- 🍀 Bước 4: Phân tích tương quan -->

Tiếp theo sau khi tìm hiểu phân phối. Ta đi vào điểm hiểu mối quan hệ giữa các thành phần với nhau.

Mối quan hệ giữa dim-dim; dim-fact; fact-fact
🌳 Ví dụ:
👉 Mối quan hệ giữa thời gian gọi điện chăm sóc và tỷ lệ chuyển đổi
👉 Khu vực chứa các tỉnh thành hay tỉnh thành chứa các khu vực hay không liên quan tới nhau
👉 Mối quan hệ giữa độ tuổi và hạn mức tín dụng
👉 Mối quan hệ giữa thu nhập và khả năng chi trả
👉 Mối quan hệ giữa chi phí marketing và doanh số
👉 Mối quan hệ giữa giá trị một đơn hàng và tỷ lệ chuyển đổi

<!-- ✍️ Hướng dẫn: bạn sử dụng tính năng pivot table, pivot chart hoặc sử dụng add-in Data Analysis để thống kê và vẽ các đặc trưng này -->

# Xây dựng Dashboard

## Mã QR Dashboard
## xxxxxxxxxx

🍀 Bước 5: Phân tích đa chiều
Ở bước này, bạn có thể phân tích một chủ điểm dựa cần phần tích (facts) trên một hệ thống các báo cáo nhìn cùng một lúc gọi là dashboard.
Điều này giống như bạn nhìn hệ thống camera giám sát an ninh tại một tòa nhà hay hệ thống điều phối giao thông.

Thông qua các slice & dice cắt lớp sẽ giúp bạn mổ xẻ và phân tích được chi tiết dữ liệu hơn.
Bạn sử dụng các thao tác:
👉 Slice
👉 Dice
👉 Pivot
👉 Rollup
👉 Drill Down
để phân tích.

<!-- ✍️ Hướng dẫn: bạn kết hợp với tính năng pivot table, pivot chart, slicer, timeline, sparkline,... để tạo một dashboard -->

Dashboard

![alt text](image-2.png)

# Tổng kết
Tổng kết

![alt text](image-14.png)
![alt text](image-15.png)

<!--  -->

https://www.kaggle.com/docs/api
https://www.kaggle.com/code/colara/human-resources-analytics-a-descriptive-analysis
https://www.kaggle.com/datasets/rishikeshkonapure/hr-analytics-prediction
https://www.kaggle.com/code/jacksonchou/hr-analytics
https://www.kaggle.com/datasets/davidepolizzi/hr-data-set-based-on-human-resources-data-set
https://www.kaggle.com/datasets/rhuebner/human-resources-data-set
https://www.kaggle.com/code/sayamkumar/employee-attrition-prediction/input
https://www.kaggle.com/datasets/rhuebner/human-resources-data-set/data

<!-- https://downloadlynet.ir/2024/28/116039/01/machine-learning-data-science-with-python-kaggle-pandas/20/?#/116039-udemy-182411021524.html -->
<!-- https://downloadlynet.ir/2024/28/116043/01/machine-learning-data-science-with-python-kaggle-a-z/21/?#/116043-udemy-182411020524.html -->

Các từ khóa bạn có thể tham khảo như:
👉 Issue tree
👉 Data analysis taxonomy
👉 Logic tree MECE
👉 Fishbone Diagram
Mình có gửi một số hình vẽ tổng hợp kiến thức như
👉 Business Analytics
👉 Data platform
👉 Data Taxonomy

link hướng dẫn vẽ cây phân tích vấn đề:
https://www.prezent.ai/learn-guides/issues-trees
link hướng dẫn vẽ cây phân tích vấn đề lợi nhuận:
https://www.craftingcases.com/profitability-tree-guide/
link bài viết trên này trên website:
https://hocexcelcoban.com/mindmap-ung-dung-trong-phan.../
Trước đi làm thì mình có sử dụng một dạng biểu diễn đa chiều hơn cây phân tích là dạng bảng cho phép thể hiện được nhiều thông tin hơn.

# AI: Data Mining (Khai phá dữ liệu)

🍀 Bước 6: Khai phá dữ liệu (Data mining)
Bạn áp dụng các mô hình, phương pháp học sâu,... để tìm ra các thông tin sâu hơn từ tập dữ liệu.
🌳 Ví dụ:
👉 Khách hàng khi mua sản phẩm A thì hay quan tâm tới sản phẩm nào khác
👉 Các hành gian lận hay có các dấu hiệu gì
👉 Dự báo được kế hoạch kinh doanh cho chu kỳ tiếp theo
👉 Xu hướng sản phẩm đang dịch chuyển theo hướng nào

<!--  -->

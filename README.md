# Motion_detection

Descripe algorithm :

    Dựa vào frame hiện tại và frame ngay trước đó để xác định movement

Use:

    Tạo class Motion_Detection với các tham số :
        
        first_frame : frame đầu tiên

        MIN_SIZE_FOR_MOVEMENT (default 2000 , là kích thước tối thiểu contour sau khi tính hiệu của 2 frame liên tiếp và đưa về threshold)

        Min_movement=3 (số frame no movement tối thiểu để khẳng định là frame hiện tại thực sự không chuyển động, giảm việc dự đoán no_movement khi có chuyển động)
    
Test :

        test.py

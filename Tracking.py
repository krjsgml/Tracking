import cv2

# haarcascades fontalface 경로 
face_cascade = cv2.CascadeClassifier('C:/jangbogo/haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('C:/jangbogo/haarcascade_upperbody.xml')

# font 설정
font = cv2.FONT_ITALIC
# open video
cap = cv2.VideoCapture(0)

# KCF, CSRT, MOSSE, GOTURN
# Boosting : 오래된 추적기로 성능이 떨어짐
# MIL : Boosting에 비해 정확도가 좋으나 실패보고가 잘 정상적으로 안됨
# KCF : Bossting, MIL보다 빠르지만, 가림 현상을 잘 처리하지 못함
# CSRT : KCF보다 정확하지만 느림
# MedianFlow : 실패보고가 잘 작동하나 빠른 변화에 취약함
# TLD : 가림현상에 잘 작동하나 Android 버전에서 에러가 빈번하게 발생
# MOSSE : 정확도는 떨어지지만 매우 빠름
# Goturn : 딥러닝 기반으로 추가 모델 파일이 필요함


# Tracker create
trackerKCF = cv2.TrackerTLD_create()

# 마우스 클릭 시 클릭 좌표 저장 변수
coordinate_x = 0
coordinate_y = 0

# 사용자가 Frame에서 없어질 때, Tracking을 정지시키기 위한 Flag변수
stop_flag = 0

# 마우스 이벤트 콜백함수 정의
def mouse_callback(event, x, y, flags, param): 
    global coordinate_x, coordinate_y
    # 왼쪽 마우스 버튼이 클릭되었을 경우
    if event == cv2.EVENT_LBUTTONDOWN:
        # x,y(마우스) 좌표 저장
        coordinate_x = x
        coordinate_y = y

# face_detect
def face_detect():
    # result의 역할이 과연 무엇일지 공부해보기
    global stop_flag
    global coordinate_x, coordinate_y
    while True:
        # read cam
        _, frame = cap.read()

        frame = cv2.flip(frame,1)
        # convert color to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # set parameter for cascade
        faces = face_cascade.detectMultiScale(gray,1.3,7)

        # find face
        # 얼굴이 검출되었다면 얼굴 위치에 대한 좌표 정보를 리턴받음.
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),1)
            cv2.putText(frame,"detected face",(x-5,y-5),font,0.5,(255,255,0),2)

            # 마우스 좌표가 얼굴 박스 안에 있을 때
            if x <= coordinate_x and coordinate_x <= x+w and y<=coordinate_y and coordinate_y<=y+h:
                # user_face에 좌표정보 저장
                user_face = x,y,w,h
                # while문 탈출을 위한 flag
                stop_flag = 1

            # 마우스 좌표 변수 초기화
            coordinate_x = 0
            coordinate_y = 0

        # show frame(window)
        cv2.imshow("frame", frame)

        # mousecallback
        cv2.setMouseCallback('frame', mouse_callback)

        # if you click 'q', program finish
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
        
        # while문 탈출
        if stop_flag == 1:
            break

    cv2.destroyAllWindows()
    
    result = trackerKCF.init(frame, user_face)
    # user_face와 result 리턴
    return user_face, result

# TrackerKCF
def tracking_user(ROI):
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame,1)
        # 추적 객체 위치 업데이트
        isUpdated, trackObjectTuple = trackerKCF.update(frame) 
        if isUpdated: 
            x1 = (int(trackObjectTuple[0]) , int(trackObjectTuple[1]) ) 
            x2 = (int(trackObjectTuple[0] + trackObjectTuple[2]), int(trackObjectTuple[1] + trackObjectTuple[3])) 
            cv2.rectangle(frame, x1, x2, (255, 0, 0), 2) 

        # user가 frame에서 없어졌을 때, tracking이 더 이상 진행되지 않을 때
        else:
            # print('user is missing')
            break
        
        cv2.imshow("track object", frame) 
        if cv2.waitKey(1) & 0xFF == ord("q"): 
            break 

    cap.release() 
    cv2.destroyAllWindows()

roi, result = face_detect()
tracking_user(roi)
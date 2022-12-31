# PetSo_backend
# B5.🚀로켓단🚀 -  🐶펫소 (PetSo)🐱

### 팀 명 :  🚀로켓단🚀

### 프로젝트 명 :  🐶펫소 (PetSo)🐱

![Untitled](https://user-images.githubusercontent.com/112169271/209808718-7cb1b6bb-e868-4b19-b7e2-9420978c6d06.png)

- 프로젝트 설명
    - 대표적인 반려동물 강아지와 고양이들을 키우는 집사들의 도움 커뮤니티.
    - 한국지능정보사회진흥원이 운영하는 AIhub에서 제공하는 반려동물 피부 질환 이미지 데이터를 전처리한 후 YOLOv5의 모델 중 하나인 yolov5n모델에 훈련시켜 미란, 결절 증상을 탐지하도록 학습, 일반 사용자들이  쉽게 판단하기 어려운 피부 질환들을 예측하여 알려주고, 사용자 주변의 병원들을 추천해주는 서비스 제공
        
          
        
- 서비스 목표(목적)
    - 반려 동물을 키우는 과정에서 만나는 어려움들을 사용자들이 서로 소통하고 , 나타내는 증상을 이미지로 검색하여 예상 병명을 빠르게 파악할 수 있는 서비스를 제공하며, 커뮤니티 게시판과 실시간 채팅 기능으로 반려 동물 케어 중 발생하는 문제 해결 방법과 일상 등을 공유하여 유저 간의 원활한 피드백 및 소통을 목적으로 하는 서비스입니다.

# 🎁 기술 스택
- Programming : <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"> <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white"> <img src="https://img.shields.io/badge/HTML-blueviolet?style=for-the-badge&logo=HTML&logoColor=white"> <img src="https://img.shields.io/badge/CSS-sucess?style=for-the-badge&logo=CSS&logoColor=white">
- Framework : <img src="https://img.shields.io/badge/DjangoRestFramework-092E20?style=for-the-badge&logo=Django&logoColor=white"> 
- Library : <img src="https://img.shields.io/badge/Pytorch-F7931E?style=for-the-badge&logo=Pytorch&logoColor=white">

---

# 팀원 소개

| 직책 | 이름 | 이메일 |
| --- | --- | --- |
| 팀장 | 박소민 | som2145@gmail.com |
| 팀원 | 최신욱 | timeiscoal@gmail.com |
| 팀원 | 장혜림 | fla12181@gmail.com |
| 팀원 | 문규빈 | 2019captain@gmail.com |
| 팀원 | 이현재 | hyunjae0723@gmail.com |

---

# 💻 **팀원별 역할**

**기능**

(문규빈 , 박소민, 이현재 )

- 사용자
    - 프로필
    - 소셜 로그인 서비스(네이버, 카카오,구글, 깃허브)
    - 팔로우 기능
    - 회원가입/로그인
    

(최신욱, 이현재)

- 반려동물
    - 내 반려동물 등록
    - 사용자가 입력한 이미지를 사용해 반려동물의 피부 질환  사물인식 모델을 활용해 탐지
        - YOLOv5
    

(장혜림, 최신욱)

- 게시글
    - 반려 동물 자랑하기(사진 업로드)
    - 반려 물품 추천 및 후기
    - 질병 공유하기(사진 업로드)
    - 댓글
    - 좋아요, 북마크
    

(최신욱)

- 그 외 서비스
    - 동물 병원 추천
        - 어떤 방식으로 동물 병원을 추천 할 것인가.
            - 자기 근처?
            - 지역 전체?
            - 24시간 동물 병원? (야간 병원)
    
    - 실시간 채팅방( ex) 동글 채팅 )
        - 권한 설정

- 추가 기능 (기본 기능 구현 이후 선택사항)
    - 캘린더
        - 알림 설정 (병원 예약 날짜 확인 혹은 예방 접종 알림)
            - 알림 방식
                - 팝업
                - 메일
                - 문자 (본인 부담)
    - 유저 간 메신저
        - 쪽지
        - 메세지
    - 툴즈 제공 ex) 사료 칼로리 계산기, 권장 칼로리 계산기, 비만도 계산기, 나이 계산기

---

# 🪄 **우리 팀 약속**

### 약속

- 태도
    - 바르고 고운 말
    - 본인이 맡은 기능 책임감 있게 마무리하기
    - 서로 모르는 거 공유하기
    - 팀원들 간의 배려와 존중하기
    - 하다가 힘들 때는 팀원들과 상황 공유 및 의사소통하기
- 업무
    - 진행현황 공유
        - 20:00 ~ 21:00
        - 현 진행 상황 공유 및 피드백
    - Github Merge
        - 지정된 시간 Merge, pull request
        - 상황에 따라 유동적으로 진행
            - 11 : 30
            - 17 : 30
            - 20 : 30
    - branch Name
        - 각자 구현 하려는 기능 별로 branch 생성

---

# **📋** 와이어 프레임

링크 - [**figma**](https://www.figma.com/file/d9GfRPrlZJVQ4wUuJfJaYC/Last-Project?node-id=0%3A1&t=B8fl4RmJ7121jTKs-0)

1. 회원가입 페이지
    
![회원가입](https://user-images.githubusercontent.com/112169271/209808837-059b033a-8154-4232-90fd-b69cd75aafc5.png)

2. 로그인 페이지

![Untitled (1)](https://user-images.githubusercontent.com/112169271/209808856-c3784cd4-3863-41ca-af72-2a3938393008.png)

3. 개인 프로필

![Untitled (2)](https://user-images.githubusercontent.com/112169271/209808875-6915df56-68d7-4ed8-bdc6-9c7081395d5c.png)

4. 펫 프로필 등록

![Untitled (3)](https://user-images.githubusercontent.com/112169271/209808945-1214a4a2-06ce-445b-9a4c-9d5bf1ca73cb.png)

5. 프로필 수정

![Untitled (4)](https://user-images.githubusercontent.com/112169271/209808978-292ef6c7-214c-434a-888b-da1d873b4e79.png)

6. 메인 페이지
    
![Untitled (5)](https://user-images.githubusercontent.com/112169271/209808999-5fae8fc6-6469-4fcd-833c-37145c213ace.png)

7. 게시글 상세페이지
    
![Untitled (6)](https://user-images.githubusercontent.com/112169271/209809021-e447d20a-c6e5-4474-b774-bbd9875efb98.png)

8. 게시글 수정페이지

![Untitled (7)](https://user-images.githubusercontent.com/112169271/209809052-821038ac-8853-429b-a269-35bb1ddf8b40.png)

9. 반려동물 피부병변 검사 페이지

![Untitled (8)](https://user-images.githubusercontent.com/112169271/209809075-b5bb2547-7be0-451d-82a1-7502db676a13.png)

10. 반려동물 피부병변 결과 페이지

![Untitled (9)](https://user-images.githubusercontent.com/112169271/209809098-7db80f9c-1805-4b3f-a551-535d096cbbb5.png)

11. 채팅

![Untitled (10)](https://user-images.githubusercontent.com/112169271/209809113-3429621e-9067-4eab-88f0-6dc50a14bdb8.png)

12. 

![Untitled (11)](https://user-images.githubusercontent.com/112169271/209809132-2be28685-f662-4856-8bfb-e23e41c2c73e.png)

---

# **📋 ERD**

링크 - [**erdcloud**](https://www.erdcloud.com/d/XNL2BZd9mzNkvQLWB)

![Untitled](https://user-images.githubusercontent.com/112169271/209809242-eb05e047-6544-403f-a28d-3352b627ac21.png)

---

# **⭐ 컨벤션**


## ▫️ Branch

User

Pet

Post

Inference

## ▫️ Commit Message

### Commit Type

- Add : 새로운 파일 추가
- Feat : 새로운 기능 추가/수정/삭제
- Fix : 버그 수정
- Update : 기존 기능 추가/수정/삭제
- Refactor: 코드 리팩토링
- Rename : 파일 혹은 폴더명을 수정하거나 옮기는 작업만인 경우
- Remove : 파일을 삭제하는 작업만 수행한 경우

### Subject

- 50자를 넘기지 않고, 커밋 타입을 준수함.

### Body

- 72자를 넘기지 않고, 모든 커밋에 본문 내용을 작성할 필요는 없음.

## ▫️ **Pull Request**

### PR 타입(하나 이상의 PR 타입 선택)

- [ ]  디자인 변경
- [ ]  기능 추가
- [ ]  기능 삭제
- [ ]  버그 수정
- [ ]  의존성, 환경 변수, 빌드 관련 코드 업데이트

### 반영 브랜치

- 작업 브랜치 -> PR 요청 브랜치

### 변경 사항

- 변경사항 상세 설명

### 테스트 결과

- 사진 설명

      (사진 업로드)

---

# 📓 API 개발

[API](https://www.notion.so/bcba587962464ca69173f581e283a1b3)

<img width="669" alt="api_1" src="https://user-images.githubusercontent.com/112169271/209812305-1326bc71-838c-4248-b9ad-8dd1f771bfcc.png">
<img width="663" alt="api_2" src="https://user-images.githubusercontent.com/112169271/209812314-7175eef6-2db1-4172-b9d2-652ad2147fca.png">

---

# ⏰ 개발 일정

- 실시간 업데이트

[개발 일정](https://www.notion.so/21e7d7f81a22436094fe1de0ed433de5)

---

# 🎯 **Troubleshooting**

    
- 2022.12.06
    - 소셜로그인 - 콜백 함수로 return되는 JsonResponse를 프론트엔드에서 다루는 방법에 대해 고민
        - 구글 콜백 URI를 프론트엔드의 login.html경로로 지정해 경로 뒤에 코드 정보를 받아서
        
        ![Untitled (1)](https://user-images.githubusercontent.com/112169271/209809559-a38ada96-086b-482f-a7fc-b5788c566c5c.png)

        - 자바스크립트를 통해 주소 내에 code가 존재할 시, 그 값을 담아 백엔드 콜백 URL로 await fetch 요청을 보내
        
        ![Untitled (2)](https://user-images.githubusercontent.com/112169271/209809588-084d8849-a3da-4163-a9eb-beb3959a1afb.png)

        - JsonResponse를 받아 access_token / refresh_token / payload 생성
        
        
- 2022.12.15
    - **add_pet 페이지 백엔드로 post요청시 HTTP status 400 이슈**
        - pet_age 모델 필드가 PositiveIntegerField 이기 때문에 숫자 이외의 텍스트를 입력할 시 is_valid에서 걸러짐
        - 프론트엔드의 나이 input 란에 type=”number” min=”1” 적용
        - 반려동물들은 나이를 햇수만 따지지 않고 개월수도 따지는 경우가 많기 때문에 펫 등록 페이지 나이 등록 방식 변경 고려 필요(PositiveIntegerField → CharField)
    
    - **프론트엔드에서 유저의 펫 리스트를 get요청을 보냈을 시 Array가 아닌 Promise{<pending>} (pending 상태의 promise 배열) 으로 받아지는 경우**
        
        ![Untitled (3)](https://user-images.githubusercontent.com/112169271/209809642-7e52970d-4057-4681-815d-fe251eefcdf4.png)

        - Promise{<pending>} 형식으로 response 데이터가 받아졌을 시 Array가 아니므로 forEach 함수가 작동되지 않고 forEach is not a function 에러가 뜸
        - 비동기 함수를 하나만 쓰는것으로 해결
        
        
        
- 2022.12.23
    
    백엔드 https 적용 배포 시도중 connection timed out 에러  
    
    <img width="663" alt="스크린샷 2022-12-23 오후 3 48 13" src="https://user-images.githubusercontent.com/112169271/209809676-407ecf2c-1178-45f8-97b2-7e2cb9b5b0e3.png">

    <img width="1286" alt="스크린샷 2022-12-23 오후 3 50 51" src="https://user-images.githubusercontent.com/112169271/209809689-d9876f2d-5e54-4d70-9564-f62f928e0e6b.png">

        
    인바운드에서 모든 트래픽을 허용해주는 규칙을 적용해주고 난 뒤 정상적으로 사이트에 들어가지는 것을 확인할 수 있었습니다.
    
    
    
- 2022.12.23
    
    **웹 배포 환경에서 페이지네이션을 적용한(viewset) 게시글의 이미지 경로가 다른 문제**
    
    ![Untitled (4)](https://user-images.githubusercontent.com/112169271/209809816-a03ef532-e5b0-46ce-a225-6d2f1ab06347.png)

    일반 article로 get 요청 image 경로
    
    ![Untitled (5)](https://user-images.githubusercontent.com/112169271/209809824-c96ed3ac-7c62-4540-a301-b185fe1106e3.png)

    페이지네이션 적용(viewset)한 경로에 get 요청 시 이미지 경로
    
    게시물을 viewset으로 받을 시 json데이터의 result항목을 기존 article과 같이 쓰는데 이 때 이미지의 경로가 다른 것을 확인
    
    ![Untitled (6)](https://user-images.githubusercontent.com/112169271/209809851-9357d3fc-65de-42a0-b129-2e8ad2b86fe8.png)

    **해결방법** 
    
    자바스크립트 내에서 [http://backend:8000](http://backend:8000) 까지의 글자를 지우는 것으로(substr) 해결
    
    ![Untitled (7)](https://user-images.githubusercontent.com/112169271/209809865-c8f855fd-e68d-4ef3-9cf9-8d62893ec315.png)

    
    
- 2022.12.27
    
    **프로필 - 이미지 파일이 없을 시 default.jpeg를 띄우지 못하는 문제**
    
    프로필의 디폴트 이미지가 원래 백엔드 media/profile 폴더 안에 default.jpeg를 넣어서 띄웠는데, 배포시에 media를 .gitignore로 무시하다보니 생긴 문제.
    
    ![Untitled (8)](https://user-images.githubusercontent.com/112169271/209809945-aa5b4277-2bc6-402f-80cb-6694e3302973.png)

    **해결 방법 1 : ec2 환경에 default.jpeg 이미지를 media/profile 폴더에 추가하기**
    
    깃허브 최상단에 default.jpeg 파일 추가 후 ec2 환경에서 내려받아 media/profile 폴더로 이동
    
    ![Untitled (9)](https://user-images.githubusercontent.com/112169271/209809951-c853e14d-86d4-4ac4-9d92-c3db6bf9373e.png)

    실패
    
    배포환경에서는 postgres로 미디어, 스태틱 파일들을 collectstatic을 하는 명령어가 있는데 그 영향인지 경로가 제대로 작동하지 않는 것 같다.
    
    postgres의 볼륨 내에서 경로를 찾아 옮겨줘야 하는 것으로 추정
    
    **해결방법 2 : 프론트엔드 자바스크립트 내에서 해결**
    
    디폴트 이미지의 경로까지는 담고 있으므로, 프로필 이미지를 띄우는 태그에 조건문을 주어 
    
    디폴트 이미지 경로일 시 프론트엔드에서 이미지를 띄우도록 src를 교체.
    
    ![Untitled (10)](https://user-images.githubusercontent.com/112169271/209809963-376ecf73-5722-42d2-b8c3-c7e1815ad5a5.png)

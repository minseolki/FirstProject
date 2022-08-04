# 오레요🍽 (오늘의 레시피 어때요?)
오늘은 무슨 요리를 할지 고민되나요? 오레요가 추천해드립니다.💪   

## 어떤 서비스 인가요?
사용자들이 자유롭게 레시피를 올리고 커뮤니케이션 할 수 있는 서비스   
[서비스 바로가기](http://13.56.18.9/)   

## 어떤 기능이 있나요?
- (메인) 등록된 레시피 불러오기
  - 등록된 모든 레시피를 확인 할 수 있습니다.
  - 레시피 이미지, 버튼 선택시 상세 레시피로 이동합니다.
  - 스크롤이 일정 픽셀이상 넘어갈 경우 위로 올라가는 TOP버튼이 생성됩니다.
  - 유저 PC의 쿠키값 확인 후 토큰 유무에 따라 로그인 여부를 확인해 헤더값이 변경됩니다.
  - 웹 브라우저가 일정 픽셀이하로 줄어들 경우 UI가 변경됩니다.

- 로그인
  - 로그인이 안될 경우 에러메세지를 유저에게 알려줍니다.
  - 로그인 성공시 유저 PC 쿠키에 토큰을 저장합니다.
  - 빈값이 있을 경우 유저에게 알려줍니다.
  - 비밀번호를 보거나 숨길 수 있습니다.
 
- 회원가입
  - 아이디 유효성 검사 후 유저에게 알려줍니다.
  - 비밀번호 유효성 검사 후 유저에게 알려줍니다.
  - 비밀번호를 암호화하여 DB에 저장합니다.
  - 빈값이 있을 경우 유저에게 알려줍니다.
 
- 레시피 등록
  - 유저가 이미지, 제목, 한줄평, 레시피를 등록 가능합니다.
  - 이미지 URL을 등록하고 레시피 등록 전 미리보기가 가능합니다.
  - 빈값이 있을 경우 유저에게 알려줍니다.

- 레시피 상세 / 댓글달기
  - 레시피의 상세 정보를 확인할 수 있습니다.
  - 댓글을 작성할 수 있습니다.
  - 유저가 올린 댓글을 조회할 수 있습니다.

## API
| 기능 | Method | URL | request | respose |
| --- | --- | --- | --- | ---|
| 메인 | GET | /api/recipe | {'title' : title, 'line_desc' : line_desc, 'img':img} | 레시피 이름, 한 줄 설명, 이미지 |
| 댓글 조회, 댓글 등록 | GET, POST | /api/comment | {'name':name, 'comment':comment} | 이름, 코멘트 |
| 회원가입 | POST | /api/sign_in | {'name' : name, 'id' : id, 'password':password} | 이름, 아이디, 비밀번호 |
| 로그인 | POST | /api/login | {'id' : id, 'password' : password} | JWT 토큰값 |
| 레시피 작성 | POST | /api/recipe | {'title' : title, 'line_desc' : line_desc, 'content':content, 'img':img, 'time':time} | 레시피 이름, 한 줄 설명, 상세 설명, 이미지, 작성 일자 |


## 기술 스택

![HTML5](https://img.shields.io/badge/HTML5-E34F26?&style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?&style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-f1e05a?&style=for-the-badge&logo=javascript&logoColor=white)
![BootStrap CSS](https://img.shields.io/badge/Bootstrap-7952B3?&style=for-the-badge&logo=bulma&logoColor=white)

![Python](https://img.shields.io/badge/Python-3776AB?&style=for-the-badge&logo=bulma&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?&style=for-the-badge&logo=mongodb&logoColor=white)
![Git](https://img.shields.io/badge/-Git-F05032?&style=for-the-badge&logo=git&logoColor=white)
![Github](https://img.shields.io/badge/-Github-181717?&style=for-the-badge&logo=github&logoColor=white)


## 팀원 소개
| 이름 | 구현 기능 | 기능 상세 |
| ----- | ----- | ---- |
| 박세린 | 레시피 등록 | 레시피 등록 페이지, 이미지 등록/불러오기, 레시피 상세 페이지 |
| 이혜진 | 댓글 달기 | 레시피 상세페이지 댓글 조회, 등록 |
| 임연주 | 메인페이지 | 메인페이지, 헤더, 레시피 불러오기, 탑 버튼 |
| 전민석(팀장) | 회원가입 | 회원가입 페이지, 회원가입 유효성 검사 |
| 홍준형 | 로그인 | 로그인 페이지, 로그인 유효성 검사, 브라우저에 쿠키 저장 |

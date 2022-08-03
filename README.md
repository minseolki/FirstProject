# 오레요🥗 (오늘의 레시피 어때요?)
오늘은 무슨 요리를 할지 고민되나요? 오레요가 추천해드립니다.💪   

## 어떤 서비스 인가요?
사용자들이 자유롭게 레시피를 올리고 커뮤니케이션 할 수 있는 서비스   
[서비스 바로가기]()   

## 어떤 기능이 있나요?
1. (메인) 등록된 레시피 불러오기
2. 로그인
3. 회원가입
4. 레시피 등록
5. 레시피 상세 / 댓글달기

## API
| 기능 | Method | URL | request | respose |
| --- | --- | --- | --- | ---|
| 메인 | GET | /api/recipe | {'title' : title, 'line_desc' : line_desc, 'img':img} | 레시피 이름, 한 줄 설명, 이미지 |
| 댓글 조회, 댓글 등록 | GET, POST | /api/comment | {'name':name, 'comment':comment} | 이름, 코멘트 |
| 회원가입 | POST | /api/sign_in | {'name' : name, 'id' : id, 'password':password} | 이름, 아이디, 비밀번호 |
| 로그인 | POST | /api/login | {'id' : id, 'password' : password} | JWT 토큰값 |
| 레시피 작성 | POST | /api/recipe | {'title' : title, 'line_desc' : line_desc, 'content':contetn, 'img':img} | 레시피 이름, 한 줄 설명, 상세 설명, 이미지 |


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

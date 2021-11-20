# Instagram Project

## 프로젝트 구성

- **Project Period** : 21.11.18 - 21.11.20
- **Language** : Python 3.9
- **F/W** : Django 3.2.9
- **IDE** : PyCharm
- **Version Control** : Git

## 구현 기능

- 인스타그램 CRUD
  - 글 작성
  - 글 수정
  - 글 삭제
  - 글 상세
- 좋아요 및 저장
- 파일 업로드
- 로그인 및 로그아웃

## 리팩터링 요구사항

1. 네브(nav) 영역에 있는 글 작성 기능 위치 변경 및 이름 변경
   1. 파일 업로드 x, 글 작성 o
2. 좋아요 및 저장 클릭 시 Ajax써서 화면 이동 안되도록 수정
   1. 현재는 Spring 사용할때처럼 깜빡이지는 않는데, 맨 아래 글 좋아요 클릭 시 상단 페이지로 이동
   2. 앞딴에서 JS써서 구현을 하는데, 파이썬이니까 예제 참조
3. 댓글 작성 기능 추가 필요
   1. 댓글 작성 클릭
   2. 팝업창 출력, 백 그라운드 영역은 .dim 처리
      1. **실제 인스타그램 페이지 참고**


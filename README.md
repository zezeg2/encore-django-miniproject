# *AWS 기반 커뮤니티 게시판 구축*

### 프로젝트 사용 기술 및 개발 도구

| AWS                                                          | Docker                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="https://lh4.googleusercontent.com/gze5vGywgznJYs9FKEj-Iotugn3ptUtE99VZ8qeJvuyXxTCk04XTz4s52bwCNicX_fxepAh2643rQjci1sGY6NgZ6R7deVJuew4liO1AkFDSBrWGrU18GP3HjmCqzlm7m_ITrDjPut4" alt="img" style="zoom:25%;margin-left:100px;" /> | ![img](https://lh3.googleusercontent.com/QRHpgg1LtuEfOi0vEiBamw_ZPwPVoE3E5PRRGt_08iWWrwqlxHGnEOukYv7dkKlGVC8Eoc3r_51DwztCzbWQPxsqnVVzCLMg78QB4EmafsYNKhwQlux8-upDEo95De8oleB6mk1-J0k) |
| Pycharm                                                      | django                                                       |
| ![img](https://lh5.googleusercontent.com/_sVYPsa1nc3wvKuN9pQ9eUwxIzT-rjK4pvYX3K9mzFtd9dulDTYPUNiYaU1wNlkazZqau80rcYu2j554oRWqGGxKD8Yx4N48wAKkwhJ9p8UfgrcpFrZ4Yb1tRu3G-B-OJDY9StQ6Lzo) | <img src="https://lh5.googleusercontent.com/0g_xCaXEoh53C-yZC53tAfmpyn15L44bKdz7TOrBKIsnA26o_D4gq8zPBCYakUP1-EuudY2-6mnKzCghdysPAcIo4R-OlyPLV4LqFtn6vwQ1GVJt5NRRuqLUw1BQjOIl7XOvUHuLoAM" alt="img" style="zoom:25%;" /> |

### 비즈니스 요구사항 - [Dev] Django 

- 회원가입이 가능했으면 함.
- 수정,삭제, 검색 기능이 있어야 함.
- 이미지 업로드 기능 추가 .
- 게시판 카테고리가 있어야함.
- 특정 권한을 가지는 유저가 게시판 생성 가능
-  유저들의 게시판 이용빈도에 따라 노출되는 게시판이 유동적으로 변화되도록 설계 
- 로그아웃 기능이 있어야함.



### MTV 아키텍처 (MVC아키텍처 기반)

![img](https://lh5.googleusercontent.com/GkTZBWTcT5LW7iJDGBJXM0W_rzX7Vlvg4QL0YKT_RXkOCNuGqvEag0rnwYUFskDAFsiDUkLQ9N7iRLe1_E3RtA19l53ZgTbH40Dkv5_s1dAXeaiRLgema27kKKqwVAqzR0nmFCg0elI)



#### Models(데이터베이스 설계)

- user - 장고내장 회원관리 시스템 사용 : 권한관리 편의성을 위해 내장회원시스템 사용

- post - 게시판에 등록될 포스트, 외래키로 board의 id참조

- board - 태그라는 속성에서 하나의 키워드를 입력받음

- comment - user의 id와 post의 id를 외래키로 참조

- favorite - user의 관심키워드를 등록하도록 하여 board의 태그와 비교하여 게시판을 추천하도록 함



#### ERD 설계

<img src="https://lh5.googleusercontent.com/xXoCKewW06fjSkSLzl-7AzTwgDYJ__Q2vwr9JVpwtLn9-kYA8TTuxdkXp5JUHSUf30fQSXqOxTScwQcsuMzgnHPdkcZqrxMV9bDJ8aP3rEGRJYDcp835MFZYmjc4qKmx1mBx5dQrd3E" alt="img" style="zoom: 67%;" />

#### Templates

- layout : 사이트 전체적인 틀을 표시, block content 사용

- form : 로그인,회원가입, 포스팅 등 form이 요구되는 페이지를 표시

- post_list : 메인페이지, 서버에 등록된 게시판과 글을 보여주고 게시판, 포스트 검색기능 지원

- board_list : 검색된 게시판을 표시하는 페이지

- post_detail : 포스트의 상세 내용 페이지, 포스트의 id를 GET요청하여 댓글기능 구현

- profile : 유저정보 페이지, 유저 id를 GET요청



#### View(Class Based View)

- PostListVIew - Get요청을 처리하여 게시판, 포스트 쿼리셋 표시, Pagination 추가

- PostCreateView,PostUpdateView - form의 Post,Update 요청을 처리하여 DB 에 post 추가

- PostDeleteView - Delete요청 처리하여 DB로부터 post 삭제

- BoardListView - Get요청을 처리하여 게시판 쿼리셋 표시

- CommetCreateView post_detail 페이지 내의 form의 Post요청을 처리하여 DB에 comment추가

- CommentDeleteView - Delete요청 처리하여 DB로부터 comment 삭제



### 구현화면

![img](https://lh5.googleusercontent.com/Q5FNkF6MIUAiJ01yLqTsfmDN8hGWAZEgMfJ4aSpWuLLBevD091b514ugvCa5Tlijqx98zeYn-FIiK0LB_78bjj065RGJjxOEuW-vatcHgBowoXZdoQNTYyicFSwRG2V4UPfXaAQoVqM)

![img](https://lh4.googleusercontent.com/XpK1Xrgu9wy1onYTIQddF684d2_QLGYPAxM-9D_zx-RqHTSxSZ3oEDMe8MmwcEF1pLQ9yHURiT0ISpkFa3XSgccH_mYvH43LxQy_s_RcEIXNTOcnm1ZUl8BYPj5agjb3D19XRmGchPk)

### 아키텍처 요구사항 - [Infra] AWS

- Database의 외부 접속 불가
- 대용량 트래픽에 대응
- 인프라의 확장성



#### 인프라 아키텍처

![img](https://lh4.googleusercontent.com/bqXB1frt5yBPD7arruwfbZYmGQuDW3WEj398QHPyVaXVXhTBoOeVLjxwf1k4B0ksGdKtrlffuFRqKqaejeVKW_p6Pih90cSGHVA8PKTNkr9sbRHk6N5djAaVOHJebN4yGay2msgVnNA)

1. DB 외부 접근 불가
   - RDS를 Private Subnet에서 구성함.

2. 대용량 트래픽 대응
   - ALB를 통해서 트래픽을 가용영역 A와 C에 분산

3. 인프라 확장성 확보
   - Public Subnet에서 ASG을 구성



#### 아키텍처 기대 효과

- 초기 투자 비용 없이 사용한 만큼만 지불할수 있어 비용절감에 효율적.

- 예측 불가한 과다 트래픽에 빠르게 대응 가능 .

- 차후 Auto Scaling 통한 용량 확장 가능성.

- 내구성, 가용성이 높아 안정성이 확보 된다.

- 관리 및 유지보수가 용이하여 시간을 절약할 수 있음.



<iframe src="https://drive.google.com/file/d/1jYjtg_WEMibp0m2Aduk5KrEZQ5sY2sLV/preview" width="640" height="480"></iframe>





#### Demo.

http://myproject-1174782895.ap-northeast-2.elb.amazonaws.com/boards/



#### 컨테이너화 파일

```
docker pull whdgus003/my-djangoweb:v2
```




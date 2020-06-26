## 플레이데이터 취업교육과정 수강생 박채연의 사전교육을 위한 repository(=repo)입니다.
#### 진행 순서
1. Python 강의 
https://programmers.co.kr/learn/courses/2

    (1) "Correction_Note": 실습 문제 오답노트
 
    (2) "Lecture_Note": 강의 중 핵심 코드
 
 
2.  Python Quiz

    (1) quiz: Quiz 1 - 20
  
    (2) quiz: Quiz 2-1 ~ 2-4
  
3. Algorithm 강의

    https://www.youtube.com/playlist?list=PL9mhQYIlKEhfg0aLdaO04wYUovLMXY4DU


4. Algorithm quiz

    quiz: algorithm_quiz 1-4

5. 보충 서적 및 website


   (1) 예제로 배우는 파이썬 프로그래밍
   
   http://pythonstudy.xyz/python/article/405-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%91%EC%85%80%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

   (2) 파이썬 자습서(한국판)
   
   https://docs.python.org/ko/3/tutorial/controlflow.html#the-range-function

   (3) 왕초보를 위한 Python
   
   https://wikidocs.net/43

   (4) Stackoverflow_ hidden-features-of python
   
   https://stackoverflow.com/questions/101268/hidden-features-of-python

   (5) 혼자 공부하는 Python (Youtube Playlist)
   
   https://www.youtube.com/playlist?list=PLBXuLgInP-5kr0PclHz1ubNZgESmliuB7

   (7) 김왼손의 미운 코딩 새끼(Programmers lecture)
   
   https://programmers.co.kr/learn/courses/29
   
   
   Book
   
   1)혼자서 공부하는 파이썬 --윤인성 저
   
  
#### Summarize note


  1. 자료형과 문자열
  
  
  str()함수는 숫자를 문자열로 변환합니다.
  
  format() 함수를 이용하면 숫자와 문자열을 다양햔 형태로 출력할 수 있습니다.
  
  upper()와 lower() 함수는 문자열의 알파벳을 대문자 혹은 소문자로 변경합니다.

  strip()함수는 문자열 양옆에서 공백을 제거합니다.
  
  find() 함수는 문자열 내부에 특정 문자가 어디에 위치하는지 찾을 때 사용합니다.
  
  in 연산자는 문자열 내부에 여떤 문자열이 있는지 확인할 때 사용합니다.
  
  split()함수는 문자열을 특정한 문자로 자를 때 사용합니다.
  
  
  2. 숫자
  
  숫자 자료형 : 소수점이 없는 정수형과 소수점이 있는 실수형(부동 소수점)
  
  숫자 연산자: +, -, *,/ 와 같은 사칙 연산자와 //(정수 나누기 연산자), %(나머지 연산자), **(제곱 연산자)
  
  연산자에는 우선순위가 존재 곱셈, 나누기 --> 더하기,빼기 --> 잘 모를 때는 괄호
  
  3. 변수와 입력
  
  변수 선언은 변수를 생성하는 것을 의미하고, 변수 할당은 변수에 값을 넣는 것을 의미합니다.
  
  변수 참조는 변수에서 값을 꺼내는 것을 의미합니다.
  
  input()함수는 명령 프롬프트에서 사용자로부터 데이터를 입력받을 때 사용합니다.
  
  int()함수는 명령 프롬프트에서 사용자로부터 데이터를 입력 받을 때 사용합니다.
  
  4. 숫자와 문자열의 다양한 기능
  
  5. 불 자료형과 if 조건문
  
  불(boolean)은 파이썬의 기본 자료형으로  True와 False를 나타내는 값입니다.
  
  비교 연산자는 숫자 또는 문자열에 적용하며, 대소를 비교하는 연산자입니다.
  
  논리 연산자는 not, and, or 연산자가 있으며, 불을 만들 때 사용합니다.
  
  if 조건문은 조건에 따라 코드를 실행하거나 실행하지 않게 만들고 싶을 때 사용하는 구문입니다.
  
  6. if~else와 elif 구문
  
  else 구문은 if 조건문 뒤에 사용하며, if 조건문의 조건이 거짓일 때 실행됩니다.
  
  elif 구문은 if 조건문과 else 구문 사이에 입력하며, 세 개 이상의 조건을 연결하여 사용할 때 적절합니다.
  
  if 조건문의 조건식에서 False로 변환되는 값은 None, 0, 0.0과 빈 문자열, 빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리 등입니다.
  
  pass 키워드는 프로그래밍 전체 골격을 잡아놓고, 내부에 처리할 내용은 나중에 만들고자 할 때 pass라는 키워드를 입력해 둡니다.
  
  
  
  7. 리스트와 반복문
  
  리스트(list)는 여러 가지 자료를 저장할 수 있는 자료형
  
  요소(element)는 리스트 내부에 있는 각각의 내용
  
  인덱스(index)는 리스트 내부에서 값의 위치 의미
  
  for 반복문은 특정 코드를 반복해서 실행할 때 사용하는 기본적인 구문
  
  8. 딕셔너리와 반복문
  
  딕셔너리는 키 기반으로 여러 자료를 저장하는 자료형
  
  키는 딕셔너리 내부에서 값에 접근할 때 사용
  
  값은 딕셔너리 내부에 있는 각각의 내용 의미
  
  9. 반복문과 while 반복문
  
  10. 문자열, 리스트, 딕셔너리와 관련된 기본 함수
  
  11. 함수
  
  12. 예외 처리
  
  13. 모듈

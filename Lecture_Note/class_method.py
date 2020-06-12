"""
메소드 이해하기
메소드(Method)
메소드는 함수와 비슷하다.
클래스에 묶여서 클래스의 인스턴스와 관계되는 일을 하는 함수
클래스 내부에 함수를 포함시킨 예


self
메소드의 첫번째 인자
인스턴스의 매개변수를 전달 할 때는 self 매개변수는 생략하고 전달

"""


class Human( ):
    '''인간'''
    def create( name, weight ): # 다음 강의에서 자세히 설명
        person = Human()
        person.name = name
        person.weight = weight
        return person

    def eat( self ):
        self.weight += 0.1
        print("{}가 먹어서 {}kg이 되었습니다".format(self.name, self.weight))

    def walk( self ):
        self.weight -= 0.1
        print("{}가 걸어서 {}kg이 되었습니다".format(self.name, self.weight))

person = Human.create("철수", 60.5)
person.eat()

class Animal( ):
    def __init__( self, name ):
        self.name = name

class Human( Animal ):
    def __init__( self, name, hand ):
        super().__init__( name )        # 부모클래스의 __init__ 메소드 호출
        self.hand = hand

person = Human( "사람", "오른손" )

print(person)

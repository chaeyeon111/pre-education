class Animal():

    def walk(self):
        print("걷는다.")

    def eat(self):
        print("먹는다.")

    def greet(self):
        print("인사한다.")


class Human(Animal):



    def wave(self):
        print("손을 흔들면서".format(self.hand))

        """
        super()
        super()
        자식클래스에서 부모클래스의 내용을 사용하고 싶은 경우
        super().부모클래스내용
        """
        super().greet()

    def greet(self):
        self.wave()


class Dog(Animal):

    def wag(self):
        print("꼬리를 흔들면서")

    def greet(self):
        self.wag()

        super().greet()




person = Human()
person.walk()
person.eat()
person.wave()
person.greet()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()

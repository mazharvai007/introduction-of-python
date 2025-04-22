class Korean:
    def speak(self):
        print("Speak in Korean")


class Bangladesh:
    def speak(self):
        print("Speak in Bengali")


def translation(people):
    return people.speak()


korean = Korean()
bangladesh = Bangladesh()

translation(korean)
translation(bangladesh)

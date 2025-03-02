from person import Person


def test_get_full_name():
    person1 = Person("John" , "Doe", 22, "male")
    
    assert person1.get_full_name() == "John Doe"

def UT_eid(first_name, middle_name, last_name, number):
    word = first_name[0] + middle_name[0] + last_name[0]
    number = str(number)
    concatenated = word + number
    return concatenated

def create_UT_eid(initials:str, num: int) -> str:
    return initials + str(num)

EID1 = UT_eid("Ricardo", "Francisco", "Pozas", 123)
print(EID1)
assert UT_eid("Ricardo", "Francisco", "Pozas", 123) == "RFP123", "ERROR!"

EID2 = create_UT_eid("RFP", 123)
print(EID2)
assert create_UT_eid("RFP", 123) == "RFP123", "ERROR!"


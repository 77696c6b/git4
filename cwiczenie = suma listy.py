#1
def listsum2(num6List):
    theSuma = 0
    for i in num6List:
        theSuma = theSuma + i
    return theSuma

print(listsum2([3,5]))



print("mozna pod definicja printowac multiple listy:pamietaj o indentacji przed return bo python robi to nieprawidlowo")

#2 teraz zrobie prawidlowo

def jakasliste(onazwieabc):
    suma = 0
    for x in onazwieabc:
        suma = suma + x
    return suma  #tutaj byl blad , nie dodawalo bo return bylo w niewlasciwym miejscu. zadaleko w prawo o jedno indentation.



print(jakasliste([6,7,9]))
print (jakasliste([3,6,8]))
print (jakasliste([39,69]))






input()























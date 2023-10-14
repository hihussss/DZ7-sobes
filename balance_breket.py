from stack import Stack


def is_breket_correct(list_breket: str) -> str:
    if isinstance(list_breket,str):
        list_breket = list(list_breket)
    brekket = Stack(list_breket)
    first_len = brekket.size() 
    if brekket.is_empty:
        answer = "Пустое множество"
    for i in brekket.stek:
       if i == "(" or i == "{" or i == "[":
           brekket.push(i)
       elif i == ")" or i == "}" or i == "]":
           brekket.pop()
    if brekket.size() == first_len:
        answer = "Сбалансированно"
    else:
        answer = "Несбалансированно"
    return answer       
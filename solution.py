def validate_date(date: str) -> str:
    d, m, a = map(int, date.split())
    if a % 4==0 and (a%100!=0 or a%400==0):
        dias_mes =[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        dias_mes =[31,28,31,30,31,30,31,31,30,31,30,31]
    if m < 1 or m > 12:
        return "Fecha incorrecta"
    if d < 1 or d > dias_mes[m - 1]:
        return  "Fecha incorrecta"
    return "Fecha correcta"
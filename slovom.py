def slovom(n):
    def get_number(n):
        nbrs = {
        0 : "", 1 : "eдин", 2 : "два", 3 : "три", 4 : "четири", 5 : "пет", 6 : "шест", 7 : "седем", 8 : "осем", 9 : "девет", 10 : "десет",
        11 : "единадесет", 12 : "дванадесет", 13 : "тринадесет", 14 : "четиринадесет", 15 : "петнадесет", 16 : "шестнадесет",
        17 : "седемнадесет", 18 : "осемнадесет", 19 : "деветнадесет",
        20 : "двадесет", 30 : "тридесет", 40 : "четиридесет", 50 : "петдесет", 60 : "шестдесет", 70 : "седемдесет", 80 : "осемдесет", 90 : "деведесет",
        100 : "сто", 200 : "двеста", 300 : "триста", 400 : "четиристотин", 500 : "петстотин",
        600 : "шестстотин", 700 : "седемстотин", 800 : "осемстотин", 900 : "деветстотин"}
        if n < 20:
            return nbrs[n] #example: 0-19
        elif n < 100:
            if n % 10:
                return nbrs[n - n % 10] + ' и ' + nbrs[n % 10] #example: 21-29
            else:
                return nbrs[n - n % 10] #example: 20,30,40
        elif n < 1000:
            if n % 100:
                if n % 10:
                    if n % 100 < 20:
                        return nbrs[n - n % 100] + ' и ' + nbrs[n % 100] #example: 101-119
                    else:
                        return nbrs[n - n % 100] + ' ' + nbrs[n % 100 - n % 10] + ' и ' + nbrs[n % 10] #example: 121-129
                else:
                    return nbrs[n - n % 100] + ' и ' + nbrs[n % 100 - n % 10] #example: 120,130,140
            else:
                return nbrs[n - n % 100] #example: 100,200,300
        elif n < 1000000:
            if n % 1000:
                if n % 100 < 20 or not n % 100 % 10:
                    if n % 1000 > 100:
                        return get_number(int(n/1000)) + ' хиляди ' + get_number(int(n%1000)) #example: X100 - X999
                    else:
                        return get_number(int(n/1000)) + ' хиляди и ' + get_number(int(n%1000))  #example: X000 + X099
                else:
                    return get_number(int(n/1000)) + ' хиляди ' + get_number(int(n%1000))
            else:
                return get_number(int(n/1000)) + ' хиляди ' #example: 1000,2000,3000
    whole = int(n)
    remainder = int(round(n % 1 * 100))
    first_part , second_part = "" , ""
    if whole:
        first_part = get_number(whole)
        first_part += ' лева'
        first_part = first_part.replace('едно хиляди', 'хиляда')
        if whole == 1:
            first_part = first_part.replace('eдин лева', 'един лев')
    if remainder:
        second_part = get_number(remainder)
        if whole:
            second_part = " и " + get_number(remainder)
        second_part += ' стотинки'
        if remainder == 1:
            second_part = second_part.replace('eдин стотинки', 'една стотинка')        
        second_part = second_part.replace('едно хиляди', 'хиляда')
        second_part = second_part.replace('два стотинки', 'две стотинки')        
    response =  first_part + second_part
    return response

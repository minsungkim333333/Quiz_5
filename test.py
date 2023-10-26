def smc(jrb, nmb, kind):
    dsy = jrb+nmb
    result=0
    if dsy < 500000000 and kind == '일반건설공사_갑':
        rate=0.0293
        result=dsy*rate
    elif 5000000000 > dsy >= 500000000 and kind == '일반건설공사_갑':
        rate=0.0186
        result=dsy*rate+5349000
    elif 5000000000 <= dsy and kind == '일반건설공사_갑':
        rate=0.0197
        result=dsy*rate
    elif dsy < 500000000 and kind == '일반건설공사_을':
        rate=0.0309
        result= dsy*rate
    elif 5000000000 > dsy >= 500000000 and kind == '일반건설공사_을':
        rate=0.0199
        result= dsy*rate+5499000
    elif 5000000000 <= dsy and kind == '일반건설공사_을':
        rate=0.0210
        result= dsy*rate
    elif dsy < 500000000 and kind == '중건설공사':
        rate=0.0343
        result= dsy*rate
    elif 5000000000 > dsy >= 500000000 and kind == '중건설공사':
        rate=0.0235
        result= dsy*rate+5400000
    elif 5000000000 <= dsy and kind == '중건설공사':
        rate=0.0244
        result= dsy*rate
    elif dsy < 500000000 and kind == '철도궤도신설공사':
        rate=0.0245
        result= dsy*rate
    elif 5000000000 > dsy >= 500000000 and kind == '철도궤도신설공사':
        rate=0.0157
        result= dsy*rate+4411000
    elif 5000000000 <= dsy and kind == '철도궤도신설공사':
        rate=0.0166
        result= dsy*rate
    elif dsy < 500000000 and kind == '특수및기타건설공사':
        rate=0.0185
        result= dsy*rate
    elif 5000000000 > dsy >= 500000000 and kind == '특수및기타건설공사':
        rate=0.0120
        result= dsy*rate+3250000
    elif 5000000000 <= dsy and kind == '특수및기타건설공사':
        rate=0.0127
        result= dsy*rate
    else:
        return 0
    return result
def persent(gyr, money):
    cost=0
    if 70 > gyr >= 50:
        cost = money * 0.5
    elif 90 > gyr >= 70:
        cost = money * 0.7
    elif gyr >= 90:
        cost = money * 0.9
    else:
        return 0
    return cost
def smc_2(jrb, nmb, kind):
    dsy = jrb+nmb
    result=0
    if kind == '일반건설공사_갑':
        rate=0.0215
        result=dsy*rate
    elif kind == '일반건설공사_을':
        rate=0.0229
        result=dsy*rate
    elif kind == '중건설공사':
        rate=0.0266
        result=dsy*rate
    elif kind == '철도궤도신설공사':
        rate=0.0181
        result=dsy*rate
    elif kind == '특수및기타건설공사':
        rate=0.0138
        result=dsy*rate
    else:
        return 0
    return result
while True:
    a=int(input('1. 재료비를 입력해주세요.(숫자만 입력해주세요. 단위 : 원)'))
    b=int(input('2. 직접 노무비를 입력해주세요.(숫자만 입력해주세요. 단위 : 원)'))
    c=input('3. 다음의 보기 중 공사의 종류를 선택하여 입력해주세요.(일반건설공사_갑, 일반건설공사_을, 중건설공사, 철도궤도신설공사, 특수및기타건설공사)')
    d=int(input('4. 공사의 진척도를 입력해주세요. (단위 : %)'))
    e=input('5. 보건관리자 선임대상 공사인가요? 예/아니요')
    if e == '예':
        cost_2=int(smc_2(a,b,c))
        use_money=int(persent(d,cost_2))
        if cost_2 == 0:
            print('정보가 알맞지 않습니다. 정보를 다시 입력해주세요.')
        elif use_money == 0:
            print('안전관리비는 '+str(cost_2)+'원 입니다.')
            print('안전관리비 최저 사용금액이 없습니다.')
        else:
            print('안전관리비는 '+str(cost_2)+'원 입니다.')
            print('안전관리비를 ' +str(use_money) +'원 이상 사용하여야 합니다.')
    elif e == '아니요':
        cost=int(smc(a,b,c))
        use_money=int(persent(d,cost))
        if cost == 0:
            print('정보가 알맞지 않습니다. 정보를 다시 입력해주세요.')
        elif use_money == 0:
            print('안전관리비는 '+str(cost)+'원 입니다.')
            print('안전관리비 최저 사용금액이 없습니다.')
        else:
            print('안전관리비는 '+str(cost)+'원 입니다.')
            print('안전관리비를 ' +str(use_money) +'원 이상 사용하여야 합니다.')
    else:
        print('정보가 알맞지 않습니다. 다시 입력해주세요.')

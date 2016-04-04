def BMI():
    height=input ("input user height (m):")
    weight=input ("input user weight (kg):")
    BMI=weight/(height*height)
    print BMI
    if BMI<=18.5:
        res= 'underweight'
    elif 18.5<BMI<=23:
        res= 'normalweight'
    elif 23<BMI<=25:
        res= 'overweight'
    elif 25<BMI<=30:
        res= 'obesity'
    else:
        res= 'an seriously obese'
    return res
print BMI()
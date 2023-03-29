credit_sum_s = 0
credit_sum_r = 0
point_sum = 0
while 1 :
    print("작업을 선택하세요.")
    print("1. 입력")
    print("2. 계산")
    answer = input()
    point = 0
    if answer == '1':
        print("학점을 입력하세요: ")
        credit = input()
        print("평점을 입력하세요: ")
        score = input()
        match score:
            case 'A+':
                point = 4.5
            case 'A':
                point = 4.0
            case 'B+':
                point = 3.5
            case 'B':
                point = 3.0
            case 'C+':
                point = 2.5
            case 'C':
                point = 2.0
            case 'D+':
                point = 1.5
            case 'D':
                point = 1.0
            case 'F':
                point = 0.0

        point_sum = point_sum+point*float(credit)
        credit_sum_s = credit_sum_s + int(credit)
        credit_sum_r = credit_sum_r + int(credit)
        if score == 'F' :
            credit_sum_r = credit_sum_r - int(credit)

    elif answer == '2' :
        break

submit = point_sum/credit_sum_s
read = point_sum/credit_sum_r

print(f"제출용: {credit_sum_s}학점 (GPA: {submit})")
print(f"열람용: {credit_sum_r}학점 (GPA: {read})")







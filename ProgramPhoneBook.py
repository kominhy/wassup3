prompt = """
홍길동 010-123-4567

1. 연락처 추가
2. 연락처 전체 보기
3. 검색, 이름을 입력받아서 전화번호 조회
4. 수정, 이름을 입력받아서 전화번호 입력수정
5. 삭제, 이름 입력받아서 삭제
6. 프로그램 종료

Enter Number : """

a = {'홍길동': '010-1234-6789'}
num = 0

while num != 6: # 전체 창
    print(prompt)
    num = int(input())
    
    while num == 1 : # 1.연락처 추가
        name = input('이름을 입력해주세요.')
        num2 = input('번호를 입력해주세요.') 
        a[name] = num2
        print(name,num2,'추가되었습니다.')
        num = int(input('나가려면 0, 계속은 1을 입력하세요.'))
        if num == 0 :
            break
    

    while num == 2 : # 2. 연락처 전체 보기
        print('연락처 전체 보기',a)
        num = int(input('나가려면 0, 계속은 2를 입력하세요'))
        if num == 0 :
            break

    while num == 3 :
        print('검색, 이름을 입력받아서 전화번호 조회')
        sear = input('이름 입력 :')
        print(a.get(sear))
        num = int(input('나가려면 0을 계속은 3을 입력하세요'))
        if num == 0 :
            break

    while num == 4 :
        print('수정, 이름을 입력받아서 전화번호 입력수정')
        sear = input('이름 입력 :')
        
        if sear in a:
            print('수정할 번호: ',a.get(sear))
            a[sear] = input('새 번호 :')
            
        else :
            print('없는 번호입니다.')
        
        num = int(input('나가려면 0을 계속은 4을 입력하세요'))
        if num == 0 :
            break

    while num == 5 :
        print('삭제, 이름 입력받아서 삭제')
        name2 = input('이름 입력 :')
    
        if name2 in a :
            print(a.get(sear),'를 정말 삭제하시겠습니까?')
            yes=0
            yes = int(input('yes:1 / NO:0 입력하세요.'))
            if yes == 1 :
                del a[sear]
                print('삭제되었습니다.')
            else :
                print('취소되었습니다.')
        else :
            print('없는 이름입니다.')
    
        num = int(input('나가려면 0을 계속은 5을 입력하세요'))
        if num == 0 :
            break
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_list = [
    '장생전',
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]


#flag = true면 모든책을 빌릴수있는거, false면 없는거
#처음에는 뭐 빌릴수 있겠지 하고 생각을 함
flag = True
#print("손님이 모든 책을 빌릴수 있는지 문의")

for book1 in rental_list:
    #print("손님이 빌릴 책 ==== " + book1)    
    book_exist = False  #책이 있나 책장에서 확인 - 아직 확인이 안됐으니까 없다고 가정
    #print("책이 없다고 가정을 하자")

    for book2 in list_of_book: #책장을 뒤져보자 하나씩
        #print("책장에서 꺼낸책 ====" + book2)
        if book1 == book2: #방금 책장에서 꺼낸책(book2) 체크하려는 책(book1)과 일치하네?
            #print("책장에서 꺼낸책과 손님이 빌릴책이 일치")
           # print("지금검색한 책은 존재한다.")
            book_exist = True # 아 책이 있다!

    #print("책장의 모든책을 뒤져봤다")
    if book_exist == True: 
         pass
    else:
        print(book1 + " 은/는 보유하고 있지 않습니다.")


if flag == True:
    print("모든 도서가 대여 가능한 상태입니다.")
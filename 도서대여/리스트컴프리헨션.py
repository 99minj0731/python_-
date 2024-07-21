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

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

#책을 입력으로 받아서 대여가 가능한지? 판단하는 함수
#대여가능이면 True, 없는책이면 False를 return
def book_available(input_book):
#    if input_book in list_of_book:
#        return True
#    else :
#        return False
    for book in list_of_book:
        if input_book == book:
            return True
#        else:
#           return False
    return False


missing_book = [book1 for book1 in rental_book if book_available(book1) == False]

for book in missing_book:
    print (f'{book} 을/를 보충하여야 합니다.')

if len(missing_book) == 0 :
    print(f'모든 도서가 대여가능합니다.')
## book club glasses

books = [
        (0, "zero"), 
        (2, "two"), 
        (4, "for"), 
        (6, "six"), 
        (8, "eight")
]

print('This is our book club points program. She gives points for the books you buy.\n')
num_books = int(input('Enter the number of books you have purchased this month: '))

points = 0

# find closest value
for book_count, point_count in books:
    if num_books >= book_count:
        points = point_count
    else:
        break

print('Points awarded to you: ', points)


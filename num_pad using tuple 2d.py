#mobile calculator using 2dimensional
#use tuple 2d

pad=(
(1,2,3),
(4,5,6),
(7,8,9),
('*',0,'#')
)
for x in pad:
    for y in x:
        print(y,end="  ")
    print()

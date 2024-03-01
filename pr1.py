import random

# تولید لیست تصادفی
my_list = [random.randint(1, 5) for _ in range(10)]
print("لیست اولیه:", my_list)

# عنصر مورد نظر برای حذف
element_to_remove = random.choice(my_list)
print("عنصر مورد نظر برای حذف:", element_to_remove)

# حذف تمام ظواهر عنصر مورد نظر
count_removed = 0
while element_to_remove in my_list:
    my_list.remove(element_to_remove)
    count_removed += 1

print("لیست پس از حذف عنصر مورد نظر:", my_list)
print("تعداد عناصر حذف شده:", count_removed)

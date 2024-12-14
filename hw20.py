# תרגילי לוגיקה ויישום
from unittest import removeResult


#1

# פונקציה המקבלת סוגריים ומחזירה אמת אם היא חוקית ושקר אם לא

#נבחן את האפשרויות

#אם האובייקט הוא סוגריים פתוחות בהתחלה אז זה תקין אך אם סגורות זה לא תקין
# (/ }
# אם אחרי הסוגריים הפתוחים יבואו סוגריים סגורים מאותה הצורה תקין- אם לא, לא תקין
# ()/ {)
# בעצם אם הסוגריים בסוף תואמות לסוגרים שלפני- תקין אם לא - שגיאה
# ({([]


def check_brackets(brackets: str) -> bool:
    '''

    :param brackets:הפונקציה מקבלת סוגריים
    :return: ובודקת אם הן תקינות
    '''
    list_char: list[str] = [] # הרשימה בא יכנסו הסוגריים הפתוחים
    for c in brackets: #הלולאה תרוץ על כל האיברים
        if c in ["(", "{", "["]: # ןתבדוק אם הסוגריים פתוחים
            list_char.append(c) # אם כן תוסיף לרשימה
            continue # הלולאה תחזור על עצמה כל עוד האיבר הוא סוגריים פתוחים

        elif c in [")", "}", "]"]:
            if not list_char:
                return False

            # כעת נבדוק את ההתאמה של הסוגריים
            last = list_char[-1]
            if c == ")" and last == "(" or c == "}" and last == "{" or \
                c == "]" and last == "[":
                list_char.pop()
            else:
                return False

    return len(list_char) == 0

print(check_brackets("(){{}}[]"))
print(check_brackets("[]({{)"))


# 2

def list_without_duplicates(list_dup) -> list:
    result = []
    last = None

    for i in list_dup:
        if i != last:
            result.append(i)
            last = i

    return result

print(list_without_duplicates([1,1,2,2,3,3,3,4,5,6,6]))


#3
list1 = [1,2,2,3,4]
list2 = [1,2,4]

def connecting_sorted_lists(list1: list[int], list2: list[int]) -> list:
    result: list[int] = []
    i, j = 0, 0
    while i < len(list1) and j > len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

        result.extend(list1[i:])
        result.extend(list2[j:])

        return result

connecting_sorted_lists([1,2,2,3,4], [1,2,4])









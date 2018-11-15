from menu import show_menu
from chengxu import *

def main():
  L = []
  while True:
    show_menu()
        # 此处先显示菜单
    s = input("请选择: ")
    if s == 'q':
        break
    elif s == '1':
        L += input_student()
    elif s == '2':
        output_student(L)
    elif s == '3':
        delete_student(L)
    elif s == '4':
        check_student(L)
    elif s == '5':
        amend_student(L)
    elif s == '6':
        output_student_by_score_desc(L)
    elif s == '7':
        output_student_by_score_asc(L)
    elif s == '8':
        output_student_by_age_desc(L)
    elif s == '9':
        output_student_by_age_asc(L)
    elif s == 'h':
        save_to_file(L)
    elif s == 'r':
        L = read_from_file()



if __name__ == '__main__':
    main()

import my_python_area

if __name__ == '__main__':


    c = my_python_area.Circle(10)
    c_area = c.fig_area()
    print(c_area)
    t = my_python_area.Triangle(5,4,3)
    t_area = t.fig_area()
    t_2 = my_python_area.Triangle(6,8,10)
    print(t_area)
    print(t.is_right())
    print(t_2.is_right())


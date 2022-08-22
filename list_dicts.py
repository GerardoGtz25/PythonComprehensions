def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Gerardo", "lastName": "Gutierrez"}

    super_list = [
      {"firstname": "Gerardo", "lastName": "Gutierrez"},
      {"firstname": "Alejandra", "lastName": "Rodriguez"},
      {"firstname": "Gabriela", "lastName": "Mendez"},
      {"firstname": "Alejandra", "lastName": "Gomez"},
    ]

    super_dict = {
      "natural_nums": [1,4,5,6],
      "integer_nums": [-5, 3,0],
      "floating_nums": [1.5,8.5,-5.2]
    }

    for key, value in super_dict.items():
        print(key, "-", value)



if __name__ == '__main__':
    run()
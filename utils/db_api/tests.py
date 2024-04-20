from sqlite import Database


def test():
    db = Database(path_to_db='D:/projetcs/python/bot/complain_bot/data/main.db', )
    # db.create_table_users()
    # print("Users")
    # db.create_table_information()
    # print("Information")
    db.select_all_info()
    print("All")
    # db.drop_information()
    # print("O'chirildi")

    # db.add_user(1, "One", "email", 'ru')
    # db.add_user(2, "olim", "olim@gmail.com", 'uz')
    # db.add_user(3, 1, 1)
    # db.add_user(4, 1, 1)
    # db.add_user(5, "John", "john@mail.com")

    # users = db.select_all_users()
    # print(f"Barcha fodyalanuvchilar: {users}")
    # user = db.select_user(Name="John", id=5)
    # print(f"Bitta foydalanuvchini ko'rish: {user}")



test()
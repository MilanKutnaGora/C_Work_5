from config_parser import config
from dbm import DBManager
from work_utils import create_database, insert_data, create_tables, get_employer_info

if __name__ == '__main__':
    """
    Основной скрипт для работы с базой данных и вывода информации.
    """

    # Получите идентификаторы компаний из вашего кода
    company_ids = [1490605, 15474, 213221, 1312952, 903198, 3288498, 2937002, 3389204, 239363, 227780]
    sql_file = "table.sql"
    db_name = 'base'
    params = config()
    create_database(db_name, params)
    create_tables(db_name, params)
    insert_data(get_employer_info(company_ids), db_name, params)

    # Создайте экземпляр DBManager
    db_manager = DBManager(db_name, params)

    while True:
        print("*" * 50)
        print("Меню:")
        print("1. Показать компании и количество вакансий")
        print("2. Показать все вакансии")
        print("3. Средняя з/п")
        print("4. Макс. з/п")
        print("5. Вакансии по запросу")
        print("0. Выход")
        print("*" * 50)

        user_choice = input("Ведите пункт меню: ")
        # Для каждого идентификатора компании получите информацию и вставьте ее в базу данных

        match user_choice:
            case "1":
                print(db_manager.get_companies_and_vacancies_count())

            case "2":
                print(db_manager.get_all_vacancies())

            case "3":
                print(db_manager.get_avg_salary())

            case "4":
                print(db_manager.get_vacancies_with_higher_salary())

            case "5":
                word = input("")
                print(db_manager.get_vacancies_with_keyword(word))

            case "0":
                quit()
            case _:
                print("некорректный ввод")

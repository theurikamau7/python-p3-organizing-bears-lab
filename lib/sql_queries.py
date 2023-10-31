import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

create_file = open("lib/create.sql")
create_as_string = create_file.read()
cursor.executescript(create_as_string)

insert_file = open("lib/seed.sql")
insert_as_string = insert_file.read()
cursor.executescript(insert_as_string)

select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex = 'F';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age
FROM bears
WHERE alive = 1
ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
WHERE age = (SELECT MAX(age) FROM bears) AND name IS NOT NULL;
"""

select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
WHERE age = (SELECT MIN(age) FROM bears);
"""
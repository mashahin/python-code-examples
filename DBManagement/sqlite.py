import sqlite3

# connect with a new database
connection = sqlite3.connect("aquarium.db")
print(connection.total_changes)

# define table schema
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS fish (name TEXT, species TEXT, tank_number INTEGER)")

# add data to the database
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'Shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'Cuttlefish', 2)")
print(connection.total_changes)

# read data from database
data = cursor.execute("SELECT * FROM fish").fetchall()
for row in data:
    print(row)

# read a specific record
target_fish = input("Enter the name of target fish: ")
record = cursor.execute(
    "SELECT * FROM fish WHERE name = ?",
    (target_fish,), 
).fetchall()
print(record)

# modify data - move a fish to a different tank
fish_to_move = input("Enter the name of the fish to be moved: ")
new_tank_number = input(f"Enter the new tank number for {fish_to_move}: ")
cursor.execute(
    "UPDATE fish SET tank_number = ? WHERE name = ?",
    (new_tank_number, fish_to_move)
)
data = cursor.execute("SELECT * FROM fish").fetchall()
for row in data:
    print(row)

# delete a record
released_fish_name = "Sammy"
cursor.execute(
    "DELETE FROM fish WHERE name = ?",
    (released_fish_name,)
)
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
for row in rows:
    print(row)

# clean up
from contextlib import closing

with closing(sqlite3.connect("aquarium.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)

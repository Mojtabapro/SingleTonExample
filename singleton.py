import datetime

class Logger:
    _instance = None  # save instance Singleton

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.log_file = "app.log"
        return cls._instance

    def log(self, message):
#add log file for record
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.datetime.now()} - {message}\n")



########################################################################################
class SingletonMeta(type):
    """ Singleton"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
#connet to database
    def __init__(self):
        self.connection = self.connect_to_db()

    def connect_to_db(self):
        #simulate connect to database
        return f"Connected to database at {id(self)}"

    def query(self, sql):
        print(f"Executing query: {sql}")

class AdvancedDatabaseConnection(DatabaseConnection):
    def optimize_queries(self):
        print("Optimizing queries for better performance...")





# test Singleton
logger1 = Logger()
logger2 = Logger()

logger1.log("Application started...")
logger2.log("User logged in.")

print(logger1 is logger2)  # True



#  Singleton test in database
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  #  True

db1.query("SELECT * FROM users;")

# تست ارث‌بری از Singleton
adv_db1 = AdvancedDatabaseConnection()
adv_db2 = AdvancedDatabaseConnection()
print(adv_db1 is adv_db2)  # True

adv_db1.optimize_queries()


from fetcher import MySql_Rectangle_Data_Fetcher

def main():
    server = input("Enter name of database server: ")
    username = input("Enter your user name: ")
    password = input("Enter your password: ")
    dbname = input("Enter the name of the database: ")
    fetch = MySql_Rectangle_Data_Fetcher(server, dbname, username, password)
    if fetch.is_connected():
        rec_list = fetch.get_data("select * from rectangle")
        if rec_list != None:
            for r in rec_list:
                print(r.to_string())
        else:
            print("The database is not connected.")
        fetch.close()


if __name__ == "__main__":
    main()

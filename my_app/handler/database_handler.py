import mysql.connector

class database_handler():
    """
    Database handler
    """
    def __init__(self):
        """
        Initialize database_handler class

        Variables:
            __ENDPOINT: url
            __PORT: Endpoint port
            __USER: user
            __PASWWORD: password
            __DBNAME: Database name
        """
        self.__ENDPOINT="zemoga-test-db.crhpedy9xxto.us-east-1.rds.amazonaws.com"
        self.__PORT="3306"
        self.__USER="zemoga_test_db"
        self.__PASWWORD="Zem0ga.101"
        self.__DBNAME="zemoga_challenge_db"

    def __db_connection(self):
        """
        Make a database connection whit the specified parameters

        Returns:
            conn:   mysql.connector.connect object
            cur:    mysql.connector.connect.cursor objetc
            error:  if the connection fails
        """
        conn = mysql.connector.connect(host=self.__ENDPOINT, port=self.__PORT, database=self.__DBNAME, user=self.__USER, password=self.__PASWWORD, ssl_ca="SSLCERTIFICATE")
        cur = conn.cursor()
        return conn, cur

    def get_users(self):
        """
        Reads the database and returns general user information

        Returns:
            users:   dict - Contains the user's names, pictures and name_id
            error: otherwise
        """
        try:
            conn, cur = self.__db_connection()
            cur.execute("""SELECT title, image_url, twitter_user_name FROM portfolio""")
            query_results = cur.fetchall()
            cur.close()
            conn.close()
            
            users = list()
            for user in query_results:
                temp_dict = dict()
                temp_dict['name'] = user[0]
                temp_dict['image_url'] = user[1]
                temp_dict['name_id'] = user[2]
                users.append(temp_dict)

            return users

        except Exception as e:
            print("Database connection failed due to {}".format(e))

    def get_user_info(self, user_name):
        """
        Reads the database and returns all the information of a specific user

        Params:
            user_name: name of the user

        Returns:
            user:   dict - Contains all the user's information
        """
        try:
            conn, cur = self.__db_connection()
            cur.execute("""SELECT * FROM portfolio WHERE twitter_user_name='{}'""".format(user_name))
            value_results = cur.fetchall()
            cur.execute("""SHOW COLUMNS FROM portfolio """)
            column_results = cur.fetchall()
            cur.close()
            conn.close()

            user = dict()
            for column, value in zip(column_results, value_results[0]):
                user["{}".format(column[0])] = value
            
            return user
        except Exception as e:
            print("Database connection failed due to {}".format(e))   

    def update_user_info(self, new_user_info):
        """
        Uptades the information of a specific user

        Params:
            new_user_info: dict - Contains the new user information
        """
        try:
            conn, cur = self.__db_connection()
            cur.execute("""UPDATE portfolio SET description="{}", image_url="{}", title="{}" WHERE twitter_user_name='{}'""".format(new_user_info['description'], new_user_info['image_url'], new_user_info['title'], new_user_info['user_name']))
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print("Database connection failed due to {}".format(e))  
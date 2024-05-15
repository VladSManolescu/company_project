from flask import Flask, request

import company_func

config = company_func.initialise_config()
app = Flask(__name__)


@app.route("/", methods=['GET'])
def first_func():
    return {"message": "Hello world!"}


@app.route("/home", methods=['PUT', 'POST'])
def second_func():
    print(request.method)
    return {"message": "Post or put request"}


@app.route("/emps")
def get_employees():
    sql_query = "SELECT * from company.employees"
    return company_func.read_from_database(sql_query, config)






if __name__ == '__main__':
    app.run()
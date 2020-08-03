from firebase import firebase
from app import app
from flask import render_template
from flask import request
# import pdb
# import pprint


db = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/')

# List of all the Majors
majors = db.get('/major_and_req', None)
majors = [*majors]  #This unpacts the dictionary into its keys and converts it into a lists
links = db.get('/major_and_link', None)

# this is a dictionary with major:list(classes)
majors_and_reqs = {}

for i in majors:
    major = '/major_and_req/{}'.format(i)
    classes = set([*db.get(major, None).values()])
    majors_and_reqs[i] = classes


def output_majors(classes_of_user):
    results = set()

    for i in classes_of_user:
        for j in majors_and_reqs:
            if i in majors_and_reqs[j]:
                results.add(j)
    if not results:
        return "Classes might not be entered properly"
    return results


def majors_and_links(majors):
    major_and_link = {}
    for i in majors:
        major_and_link[i] = links[i]

    return major_and_link


def is_list(value):
    return isinstance(value, set)


@app.route('/majors', methods=['GET', 'POST'])
def func():
    input = request.form['classes_input']
    user_classes = input.split(', ')

    # breakpoint()
    majors = output_majors(user_classes)

    options = majors_and_links(majors)

    # print(majors)

    data = {
        "input": input,
        "is_list": is_list(majors),
        "options": options,
    }


    return render_template("majors.html", **data)

# <!--------------------pseudo Code---------------->
#
# user_classes = []
#
# possible = []
#
# for i in user_classes:
#
#     if #look for verificaiton of value - A && #extract the path in which the class has been verified -E:
#         possible.append()
#
#
# pprint(possible)

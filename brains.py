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
    results = {}
    for i in classes_of_user:  # goes through each class in the list
        for j in majors_and_reqs:  # goes through each major - list of classes
            if i in majors_and_reqs[j]:  # checks if the user_class is in the list of classes in the major
                if j in results:  # if the major is in the dict, increment by one
                    results[j] += 1
                else:  # if the major is not inside of it, it is initiated
                    results[j] = 1
    if not results:
        return "Classes might not be entered properly"
    return results


def majors_and_links(majors):
    major_and_link = {}
    if isinstance(majors, str):  # in case that the classes does not exist in Database
        major_and_link["#"] = "#"
    else:
        for i in majors:  # if it returns then it will create a dict with links
            major_and_link[i] = links[i]
    return major_and_link


def is_list(value):
    return isinstance(value, dict)


@app.route('/majors', methods=['GET', 'POST'])
def func():
    input = request.form['classes_input'].upper()
    user_classes = input.split(', ')

    # returns a dictionary if classes were inputed correctly
    majors = output_majors(user_classes)



    if majors:
        # returns a dictionary
        options = majors_and_links(majors)


    data = {
        "input": input,
        "is_list": is_list(majors),
        "majors": majors,
        "links": options,
        "homepage": request.url_root
    }


    return render_template("majors.html", **data)

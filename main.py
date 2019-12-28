import data_manager
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('László')
    return render_template('mentor_names.html', mentor_names=mentor_names)


@app.route('/all-mentors')
def all_names():
    first_and_last_name = data_manager.get_all_first_name_and_last_name()
    return render_template('first_second_name.html', first_and_last_name=first_and_last_name)


@app.route('/mentors-nicknames')
def route_mentors_nicknames():
    city = 'Miskolc'
    mentors_nicknames = data_manager.get_mentors_nicknames_by_city(city)
    return render_template('mentors_nicknames.html', mentors_nicknames=mentors_nicknames, city=city)


@app.route('/applicant-fullname-phonenumber-by-first-name')
def route_applicant_fullname_phonenumber():
    first_name = 'Carol'
    applicant_full_name_and_phone_number = data_manager.get_applicant_fullname_and_phone_number_by_first_name(
        first_name)
    return render_template('applicant_details.html',
                           applicant_full_name_and_phone_number=applicant_full_name_and_phone_number)


@app.route('/applicant-fullname-phonenumber-by-email')
def route_applicant_fullname_phonenumber_by_email():
    email = '@adipiscingenimmi.edu'
    applicant_fullname_phonenumber_by_email = data_manager.get_applicant_fullname_and_phone_number_by_email(
        email)
    return render_template('applicant_details.html',
                           applicant_fullname_phonenumber_by_email=applicant_fullname_phonenumber_by_email)


@app.route('/add-applicant', methods=['GET', 'POST'])
def add_applicant():
    application_code = data_manager.random_application_code
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        phone_number = request.form['phone-number']
        email = request.form['email']
        data_manager.add_new_applicant(first_name.strip(), last_name.strip(), phone_number.strip(), email.strip(),
                                       application_code)
        return redirect(url_for('add_applicant'))
    applicant_details = data_manager.get_applicant_details(application_code)
    return render_template('add_applicant.html', applicant_details=applicant_details)


@app.route('/update-phone-number', methods=['GET', 'POST'])
def route_update_phone_number():
    if request.method == 'POST':
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        phone_number = request.form['phone-number']
        data_manager.update_applicant_phone_number(first_name.strip(), last_name.strip(), phone_number.strip())
        details = data_manager.get_applicant_fullname_and_phone_number_by_first_name(first_name.strip())
        return render_template('update_applicant_details.html', details=details)
    return render_template('update_applicant_details.html')


@app.route('/delete-applicant-by-email', methods=['GET', 'POST'])
def route_delete_applicant_by_domain():
    if request.method == 'POST':
        domain = request.form['domain']
        deleted_applicants = data_manager.get_applicant_fullname_and_phone_number_by_email(domain)
        data_manager.remove_applicants_by_domain(domain.strip())
        return render_template('delete_applicant_by_domain.html', deleted_applicants=deleted_applicants)
    return render_template('delete_applicant_by_domain.html')


if __name__ == '__main__':
    app.run(debug=True)

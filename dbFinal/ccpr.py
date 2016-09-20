import sqlite3
import sys
from bottle import route, run, debug, template, request, error
# http://bottlepy.org/docs/dev/tutorial_app.html

@route('/ccpr/')
def ccpr_listVol():
	if request.GET.get('save','').strip():
		selectQ = request.GET.get('selectQ', '').strip()
	  	fromQ = request.GET.get('fromQ', '').strip()
		whereQ = request.GET.get('whereQ', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()
		try:
			c.execute("SELECT %s FROM %s WHERE %s" % (selectQ, fromQ, whereQ))
			result = c.fetchall()
			names = [description[0] for description in c.description]

			conn.commit()
			c.close()

			return template('templates/make_table', rows=result, names=names, table='')

		except sqlite3.OperationalError as e:
			return "Operational Error executing query in database. Error: ", str(e)

	else:
		return template('templates/new_ccpr')

@route('/volunteer/')
def ccpr_listVol():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Volunteer;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	# SELECT * FROM Volunteer ORDER BY volunteerID
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='Volunteer')
	return output


@route('/volunteer/new/', method=['GET'])
def volunteer_new():
	if request.GET.get('save','').strip():
		volunteerName = request.GET.get('volunteerName', '').strip()
		volunteerLastName = request.GET.get('volunteerLastName', '').strip()
		volunteerAddress = request.GET.get('volunteerAddress', '').strip()
		volunteerCity = request.GET.get('volunteerCity', '').strip()
		volunteerZipCode = request.GET.get('volunteerZipCode', '').strip()
		volunteerChurch = request.GET.get('volunteerChurch', '').strip()
		volunteerGender = request.GET.get('volunteerGender', '').strip()
		volunteerPhone = request.GET.get('volunteerPhone', '').strip()
		volunteerOccupation = request.GET.get('volunteerOccupation', '').strip()
		volunteerChaplain = request.GET.get('volunteerChaplain', '').strip()
		volunteerInterest = request.GET.get('volunteerInterest', '').strip()
		volunteerZone = request.GET.get('volunteerZone', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Volunteer " \
						"(volunteerName, volunteerLastName, volunteerAddress, " \
						"volunteerCity, volunteerZipCode, volunteerChurch, " \
						"volunteerGender, volunteerPhone, volunteerOccupation, " \
						"volunteerChaplain, volunteerInterest, volunteerZone) " \
						"VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ",
						(volunteerName, volunteerLastName, volunteerAddress, volunteerCity, volunteerZipCode, volunteerChurch, volunteerGender, volunteerPhone, volunteerOccupation, volunteerChaplain, volunteerInterest, volunteerZone))

		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Volunteer', id=new_id)

	else:
		return template('templates/new_volunteer')

@route('/volunteer/<volunteerId:int>/', method=['GET'])
def volunteer_edit(volunteerId):
	if request.GET.get('save','').strip():
		volunteerName = request.GET.get('volunteerName', '').strip()
		volunteerLastName = request.GET.get('volunteerLastName', '').strip()
		volunteerAddress = request.GET.get('volunteerAddress', '').strip()
		volunteerCity = request.GET.get('volunteerCity', '').strip()
		volunteerZipCode = request.GET.get('volunteerZipCode', '').strip()
		volunteerChurch = request.GET.get('volunteerChurch', '').strip()
		volunteerGender = request.GET.get('volunteerGender', '').strip()
		volunteerPhone = request.GET.get('volunteerPhone', '').strip()
		volunteerOccupation = request.GET.get('volunteerOccupation', '').strip()
		volunteerChaplain = request.GET.get('volunteerChaplain', '').strip()
		volunteerInterest = request.GET.get('volunteerInterest', '').strip()
		volunteerZone = request.GET.get('volunteerZone', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("UPDATE Volunteer " \
						"SET volunteerName = ?, volunteerLastName = ?, volunteerAddress = ?, " \
						"volunteerCity = ?, volunteerZipCode = ?, volunteerChurch = ?, " \
						"volunteerGender = ?, volunteerPhone = ?, volunteerOccupation = ?, " \
						"volunteerChaplain = ?, volunteerInterest = ?, volunteerZone = ? " \
						"WHERE id = ?",
						(volunteerName, volunteerLastName, volunteerAddress, volunteerCity, volunteerZipCode, volunteerChurch, volunteerGender, volunteerPhone, volunteerOccupation, volunteerChaplain, volunteerInterest, volunteerZone, volunteerId))

		conn.commit()
		c.close()

		return "Volunteer with ID %s has been saved\n <a href='/ccpr/'>HOME</a>" % volunteerId

	else:
		conn = sqlite3.connect('ccpr.db')
		conn.row_factory = sqlite3.Row
		c = conn.cursor()
		c.execute("SELECT * FROM Volunteer where id=?;",(str(volunteerId)))
		result = c.fetchone() #fetchone returns a row where the keys are the columns names.
		print result
		print result.keys()
		c.close()
		return template('templates/edit_volunteer',id=volunteerId, v=result)

@route('/prison/')
def ccpr_listPri():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Prison ;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='')
	return output

@route('/prison/new/')
def prison_new():
	if request.GET.get('save','').strip():
		prisonName = request.GET.get('prisonName', '').strip()
		prisonAddress = request.GET.get('prisonAddress', '').strip()
		prisonCity = request.GET.get('prisonCity', '').strip()
		prisonZipCode = request.GET.get('prisonZipCode', '').strip()
		prisonGender = request.GET.get('prisonGender', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Prison " \
					"(prisonName, prisonAddress, prisonCity, prisonZipCode, prisonGender) "\
					"VALUES (?,?,?,?,?) ",
					(prisonName, prisonAddress, prisonCity, prisonZipCode, prisonGender))

		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Prison', id=new_id)

	else:
		return template('templates/new_prison')

@route('/prisoner/')
def ccpr_listPri():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Prisoner;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='')
	return output

@route('/prisoner/new/')
def prisoner_new():
	if request.GET.get('save','').strip():
		prisonerName = request.GET.get('prisonerName', '').strip()
		prisonerGender = request.GET.get('prisonerGender', '').strip()
		prisonerZone = request.GET.get('prisonerZone', '').strip()
		volunteerID = request.GET.get('volunteerID', '').strip()
		prisonID = request.GET.get('prisonID', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Prisoner " \
				"(prisonerName, prisonerGender, prisonerZone, prisonID, volunteerID) " \
				"VALUES (?,?,?,?,?) ",
				(prisonerName, prisonerGender, prisonerZone, prisonID, volunteerID))

		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Prisoner', id=new_id)

	else:
		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()
		c.execute("SELECT id, volunteerName, volunteerLastName FROM Volunteer;")
		volunteers = c.fetchall()
		c.execute("SELECT id, prisonName FROM Prison;")
		prisons = c.fetchall()
		c.close()

		output = template('templates/new_prisoner', volunteers=volunteers, prisons=prisons)

		return output

@route('/child/')
def ccpr_listChild():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Child;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='')
	return output

@route('/child/new/')
def child_new():
	if request.GET.get('save','').strip():
		prisonerID = request.GET.get('prisonerID', '').strip()
		childName = request.GET.get('childName', '').strip()
		childLastName = request.GET.get('childLastName', '').strip()
		childAge = request.GET.get('childAge', '').strip()
		childGender = request.GET.get('childGender', '').strip()
		childAddress = request.GET.get('childAddress', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Child " \
				"(prisonerID, childName, childLastName, childAge, childGender, childAddress) " \
				"VALUES (?,?,?,?,?,?) ",
				(prisonerID, childName, childLastName, childAge, childGender, childAddress))
		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Child', id=new_id)

	else:
		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()
		c.execute("SELECT id, prisonerName FROM Prisoner;")
		prisoners = c.fetchall()

		c.close()

		output = template('templates/new_child', prisoners=prisoners)

		return output

@route('/position/')
def ccpr_listPos():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Position;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='')
	return output

@route('/position/new/')
def new_position():
	if request.GET.get('save','').strip():
		positionName = request.GET.get('positionName', '').strip()
		posDescription = request.GET.get('posDescription', '').strip()
		posTerms = request.GET.get('posTerms', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Position " \
					"(positionName, posDescription, posTerms) "\
					"VALUES (?,?,?) ",
					(positionName, posDescription, posTerms))

		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Position', id=new_id)

	else:
		return template('templates/new_position')

@route('/period/')
def ccpr_listPeriod():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Period ORDER BY periodInitial;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='')
	return output

@route('/period/new/')
def new_period():
	if request.GET.get('save','').strip():
		periodInitial = request.GET.get('periodInitial', '').strip()
		periodLast = request.GET.get('periodLast', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Period " \
					"(periodInitial, periodLast) "\
					"VALUES (?,?) ",
					(periodInitial, periodLast))

		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Period', id=new_id)

	else:
		return template('templates/new_period')

@route('/board/')
def ccpr_listBoard():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Board ORDER BY periodID, positionID;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='')
	return output

@route('/board/new/')
def new_board():
	if request.GET.get('save','').strip():
		periodID = request.GET.get('periodID', '').strip()
		volunteerID = request.GET.get('volunteerID', '').strip()
		positionID = request.GET.get('positionID', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Board " \
				"(periodID, volunteerID, positionID) " \
				"VALUES (?,?,?) ",
				(periodID, volunteerID, positionID))

		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Board', id=new_id)

	else:
		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()
		c.execute("SELECT id, volunteerName, volunteerLastName FROM Volunteer;")
		volunteers = c.fetchall()
		c.execute("SELECT id, periodInitial FROM Period;")
		periods = c.fetchall()
		c.execute("SELECT id, positionName FROM Position")
		positions = c.fetchall()
		c.close()

		output = template('templates/new_board', volunteers=volunteers, periods=periods, positions=positions)

		return output

@route('/visit/')
def ccpr_listVisit():
	conn = sqlite3.connect('ccpr.db')
	c = conn.cursor()
	c.execute("SELECT * FROM Visit;")
	names = [description[0] for description in c.description]
	result = c.fetchall()
	c.close()

	output = template('templates/make_table', rows=result, names=names, table='')
	return output

@route('/visit/new/')
def new_visit():
	if request.GET.get('save','').strip():
		visitDay = request.GET.get('visitDay', '').strip()
		visitHour = request.GET.get('visitHour', '').strip()
		visitProgram = request.GET.get('visitProgram', '').strip()
		volunteerID = request.GET.get('volunteerID', '').strip()
		prisonID = request.GET.get('prisonID', '').strip()

		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()

		c.execute("INSERT INTO Visit " \
				"(volunteerID, prisonID, visitDay, visitHour, visitProgram) " \
				"VALUES (?,?,?,?,?) ",
				(volunteerID, prisonID, visitDay, visitHour, visitProgram))

		new_id = c.lastrowid

		conn.commit()
		c.close()

		return template('templates/results', table_name='Visit', id=new_id)

	else:
		conn = sqlite3.connect('ccpr.db')
		c = conn.cursor()
		c.execute("SELECT id, volunteerName, volunteerLastName FROM Volunteer;")
		volunteers = c.fetchall()
		c.execute("SELECT id, prisonName FROM Prison;")
		prisons = c.fetchall()
		c.close()

		output = template('templates/new_visit', volunteers=volunteers, prisons=prisons)

		return output

@error(403)
def mistake403(code):
    return 'The parameter you passed has the wrong format!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'
# Use for development
# Help to find errors
debug(True)
# Start the web server
run(reloader=True)

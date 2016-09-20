<p>Add a new volunteer to the database :</p>
<form action="/volunteer/new/" method="GET">
<table>
    <tr>
      <td>Name:</td>  <td><input type="text" size="15" maxlength="15" name="volunteerName"></td>
    </tr>
    <tr>
      <td>Last Name:</td><td><input type="text" size="15" maxlength="15" name="volunteerLastName"></td>
    </tr>
    <tr>
      <td>Address:</td><td><input type="text" size="30" maxlength="30" name="volunteerAddress"></td>
    </tr>
    <tr>
      <td>City:</td><td><input type="text" size="10" maxlength="10" name="volunteerCity"></td>
    </tr>
    <tr>
      <td>Zipcode:</td><td><input type="number" size="5" maxlength="5" name="volunteerZipCode"></td>
    </tr>
    <tr>
      <td>Church:</td><td><input type="text" size="30" maxlength="30" name="volunteerChurch"></td>
    </tr>
    <tr>
      <td>Gender:</td><td><input type="radio" name="volunteerGender" value="M" checked> Male
      <input type="radio" name="volunteerGender" value="F"> Female </td>
    </tr>
    <tr>
      <td>Phone:</td><td><input type="tel" name="volunteerPhone"></td>
    </tr>
    <tr>
      <td>Occupation:</td><td><input type="text" size="20" maxlength="20" name="volunteerOccupation"></td>
    </tr>
    <tr>
      <td>Chaplain:</td><td><input type="radio" name="volunteerChaplain" value="Yes"checked> Yes
      <input type="radio" name="volunteerChaplain" value="No"> No</td>
    </tr>
    <tr>
      <td>Interest:</td><td><input type="text" size="20" maxlength="20" name="volunteerInterest"></td>
    </tr>
    <tr>
      <td>Living Zone:</td>
      <td>
        <select name="volunteerZone">
          <option value="1">Metro</option>
          <option value="2">North</option>
          <option value="3">South</option>
          <option value="4">Center</option>
          <option value="5">East</option>
          <option value="6">West</option>
        </select>
      </td>

</td>
    </tr>
</table>
<input type="submit" name="save" value="save">
</form>

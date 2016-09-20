<p>Add a new prison to the database :</p>
<form action="/prison/new/" method="GET">
<table>
  <tr>
    <td>Name:</td>  <td><input type="text" size="15" maxlength="15" name="prisonName"></td>
  </tr>
  <tr>
    <td>Address:</td><td><input type="text" size="30" maxlength="30" name="prisonAddress"></td>
  </tr>
  <tr>
    <td>City:</td><td><input type="text" size="10" maxlength="10" name="prisonCity"></td>
  </tr>
  <tr>
    <td>Zipcode:</td><td><input type="number" size="5" maxlength="5" name="prisonZipCode"></td>
  </tr>
  <tr>
    <td>Gender:</td><td><input type="radio" name="prisonGender" value="M" checked> Male
    <input type="radio" name="prisonGender" value="F"> Female </td>
  </tr>
</table>
<input type="submit" name="save" value="save">
</form>

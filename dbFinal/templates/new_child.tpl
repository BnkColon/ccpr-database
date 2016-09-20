<p>Add a new child to the database :</p>
<form action="/child/new/" method="GET">
<table>
  <tr>
    <td>
      Prisoner:
    </td>
    <td>
      <select name=prisonerID>
      %for prisoner in prisoners:
      <option value={{prisoner[0]}}>{{prisoner[1]}}</option>
      %end
      </select>
    </td>
  </tr>
  <tr>
    <td>Name:</td>  <td><input type="text" size="15" maxlength="15" name="childName"></td>
  </tr>
  <tr>
    <td>Last Name:</td><td><input type="text" size="15" maxlength="15" name="childLastName"></td>
  </tr>
  <tr>
    <td>Age:</td><td><input type="number" size="2" maxlength="2" name="childAge"></td>
  </tr>
  <tr>
    <td>Gender:</td><td><input type="radio" name="childGender" value="M" checked> Male
    <input type="radio" name="childGender" value="F"> Female </td>
  </tr>
  <tr>
    <td>Address:</td><td><input type="text" size="30" maxlength="30" name="childAddress"></td>
  </tr>
</table>
<input type="submit" name="save" value="save">
</form>

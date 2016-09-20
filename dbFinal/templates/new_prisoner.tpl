<p>Add a new prisoner to the database :</p>
<form action="/prisoner/new/" method="GET">
<table>
  <tr>
    <td> Name: </td>
    <td><input type="text" size="15" maxlength="15" name="prisonerName"></td>
  </tr>
  <tr>
    <td> Gender:</td>
    <td><input type="radio" name="prisonerGender" value="M" checked> Male
    <input type="radio" name="prisonerGender" value="F"> Female </td>
  </tr>
  <tr>
    <td> Living Zone: </td>
    <td>
      <select name="prisonerZone">
        <option value="1">Metro</option>
        <option value="2">North</option>
        <option value="3">South</option>
        <option value="4">Center</option>
        <option value="5">East</option>
        <option value="6">West</option>
      </select>
    </td>
  </tr>
  <tr>
    <td>
      Prison:
    </td>
    <td>
      <select name=prisonID>
      %for prison in prisons:
      <option value={{prison[0]}}>{{prison[1]}}</option>
      %end
      </select>
    </td>
  </tr>
  <tr>
    <td>
      Volunteer in charge:
    </td>
    <td>
      <select name=volunteerID>
      %for volunteer in volunteers:
      <option value={{volunteer[0]}}>{{volunteer[1]}} {{volunteer[2]}}</option>
      %end
      </select>
    </td>
  </tr>
</table>
<input type="submit" name="save" value="save">
</form>

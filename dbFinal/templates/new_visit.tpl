<p>Add a new visit to the database :</p>
<form action="/visit/new/" method="GET">
<table>
  <tr>
    <td>
      Volunteer:
    </td>
    <td>
      <select name=volunteerID>
      %for volunteer in volunteers:
      <option value={{volunteer[0]}}>{{volunteer[1]}} {{volunteer[2]}}</option>
      %end
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
    <td>Day:</td>  <td><input type="date" name="visitDay" min="2000-01-02"></td>
  </tr>
  <tr>
    <td>Hour:</td><td><input type="time" name="visitHour"></td>
  </tr>
  <tr>
    <td>Program:</td><td><input type="text" size="20" maxlength="20" name="visitProgram"></td>
  </tr>

</table>
<input type="submit" name="save" value="save">
</form>

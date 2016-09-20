<p>Add a new board member to the database :</p>
<form action="/board/new/" method="GET">
<table>
  <tr>
    <td>
      Period:
    </td>
    <td>
      <select name=periodID>
      %for period in periods:
      <option value={{period[0]}}>{{period[1]}}</option>
      %end
      </select>
    </td>
  </tr>
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
      Position:
    </td>
    <td>
      <select name=positionID>
      %for position in positions:
      <option value={{position[0]}}>{{position[1]}}</option>
      %end
      </select>
    </td>
  </tr>
</table>
<input type="submit" name="save" value="save">
</form>

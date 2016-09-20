<p>Add a new position to the database :</p>
<form action="/position/new/" method="GET">
<table>
  <tr>
    <td>Position:</td>  <td><input type="text" size="15" maxlength="15" name="positionName"></td>
  </tr>
  <tr>
    <td>Description:</td><td><input type="text" size="20" maxlength="20" name="posDescription"></td>
  </tr>
  <tr>
    <td>Terms:</td><td><input type="text" size="20" maxlength="20" name="posTerms"></td>
  </tr>
</table>
<input type="submit" name="save" value="save">
</form>

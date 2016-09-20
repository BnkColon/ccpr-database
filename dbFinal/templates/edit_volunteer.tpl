<p>Edit Volunteer :</p>
<form action="/volunteer/{{id}}/" method="GET">
<table>
    <tr>
      <td>Name:</td>  <td><input type="text" size="15" maxlength="15" name="volunteerName" value="{{v['volunteerName']}}"></td>
    </tr>
    <tr>
      <td>Last Name:</td><td><input type="text" size="15" maxlength="15" name="volunteerLastName" value="{{v['volunteerLastName']}}"></td>
    </tr>
    <tr>
      <td>Address:</td><td><input type="text" size="30" maxlength="30" name="volunteerAddress" value="{{v['volunteerAddress']}}"></td>
    </tr>
    <tr>
      <td>City:</td><td><input type="text" size="10" maxlength="10" name="volunteerCity" value="{{v['volunteerCity']}}"></td>
    </tr>
    <tr>
      <td>Zipcode:</td><td><input type="number" size="5" maxlength="5" name="volunteerZipCode" value="{{v['volunteerZipCode']}}"></td>
    </tr>
    <tr>
      <td>Church:</td><td><input type="text" size="30" maxlength="30" name="volunteerChurch" value="{{v['volunteerChurch']}}"></td>
    </tr>
    <tr>
      <td>Gender:</td>
      <td>
        <input type="radio" name="volunteerGender" value="M"
        %if v['volunteerGender'] == 'M':
          checked\\
        %end
        > Male </input>
        <input type="radio" name="volunteerGender" value="F"\\
        %if v['volunteerGender'] == 'F':
          checked\\
        %end
        > Female </input>
      </td>
    </tr>
    <tr>
      <td>Phone:</td><td><input type="tel" name="volunteerPhone" value="{{v['volunteerPhone']}}"></td>
    </tr>
    <tr>
      <td>Occupation:</td><td><input type="text" size="20" maxlength="20" name="volunteerOccupation" value="{{v['volunteerOccupation']}}"></td>
    </tr>
    <tr>
      <td>Chaplain:</td><td>
        <input type="radio" name="volunteerChaplain" value="Yes"\\
        %if v['volunteerChaplain'] == 'Yes':
          checked\\
        %end
        > Yes </input>
      <input type="radio" name="volunteerChaplain" value="No"\\
      %if v['volunteerChaplain'] == 'No':
        checked\\
      %end
      > No
    </td>
    </tr>
    <tr>
      <td>Interest:</td><td><input type="text" size="20" maxlength="20" name="volunteerInterest" value="{{v['volunteerInterest']}}"></td>
    </tr>
    <tr>
      <td>Living Zone:</td>
      <td>
        <select name="volunteerZone">
          <option value="1"\\
          %if v['volunteerZone'] == '1':
            selected\\
          %end
          >Metro</option>

          <option value="2"\\
          %if v['volunteerZone'] == '2':
            selected\\
          %end
          >North</option>

          <option value="3"\\
          %if v['volunteerZone'] == '3':
            selected\\
          %end
          >South</option>

          <option value="4"\\
          %if v['volunteerZone'] == '4':
            selected\\
          %end
          >Center</option>

          <option value="5"\\
          %if v['volunteerZone'] == '5':
            selected\\
          %end
          >East</option>

          <option value="6"\\
          %if v['volunteerZone'] == '6':
            selected\\
          %end
          >West</option>
        </select>
      </td>

</td>
    </tr>
</table>
<input type="submit" name="save" value="save">
</form>

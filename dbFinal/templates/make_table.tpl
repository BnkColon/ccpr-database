%#template to generate a HTML table from a list of tuples
<p> Prison Fellowship of Puerto Rico:</p>
<table border="1">
<thead>
%for name in names:
<th>{{name}}</th>
%end
</thead>
%for row in rows:
    <tr>
        %for i in range(0,len(row)):
        <td>
          %if i == 0 and table != '':
            <a href='{{row[i]}}/'>{{row[i]}}</a>
          %else:
            {{row[i]}}
          %end
        </td>
        %end
    </tr>
%end
</table>

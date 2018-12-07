*************************************************************************************************

1. This part of code is for implementing the drop downs that i have mentioned in my README file
   this is what i have worked on sprint 3.

*************************************************************************************************

-----------------------------------------------
Javascript code below for drop down menu:
-----------------------------------------------

<script type="text/javascript">
    function populate(s1,s2){
        var s1 = document.getElementById(s1);
        var s2 = document.getElementById(s2);
        s2.innerHTML = "";
        if(s1.value == "Science and Engineering"){
            var optionArray =["computer science|Computer Science","biology|Biology",
                "chemistry & biochemistry|Chemistry & Biochemistry","engineering technology|Engineering Technology",
                "mathematics|Mathematics","physics|Physics"];
        }
        else if (s1.value == "Applied Arts"){
            var optionArray =["aerospace studies|Aerospace Studies","agriculture|Agriculture",
                "criminal justice|Criminal Justice","family & consumer science|Family & Consumer Science",
                "military science|Military Science","social work|Social Work",
                "occupational, workforce and leadership studies|Occupational, Workforce and Leadership Studies"];
        }
        else if (s1.value == "McCoy College of Business Administration"){
            var optionArray =["school of business|School of Business"];
        }
        else if (s1.value == "Education"){
            var optionArray=["curriculum and instruction| Curriculum And Instruction",
                "health and human performance|Health and Human Performance",
                "counseling,leadership,adult education and school psychology|" +
                "Counseling,Leadership,Adult Education and School Psychology"];
        }
        else if (s1.value == "Fine Arts and Communication"){
            var optionArray =["fine arts and communication|Fine Arts and Communication"];
        }
        else if(s1.value == "Health Professions"){
            var optionArray =["physical therapy|Physical Therapy","radiation therapy|Radiation Therapy",
                "respiratory care|Respiratory Care","health information management|Health Information Management"];
        }
        else if(s1.value == "Liberal Arts"){
            var optionArray =["anthropology|Anthropology","english|English","geography|Geography","history|History",
                "modern language|Modern Language","philosophy|Philosophy","political science|Political Science",
                "psychology|Psychology","sociology|Sociology"];
        }
        for(var option in optionArray){
            var pair = optionArray[option].split("|");
            var newOption = document.createElement("option");
            newOption.value = pair[0];
            newOption.innerHTML = pair[1];
            s2.options.add(newOption);
        }
    }
</script>

--------------------------------------------
HTML code below for the drop down menu:
--------------------------------------------

<select id="college" name="college" onchange="populate(this.id,'department')">
                    <option value="Applied Arts">Applied Arts</option>
                    <option value="McCoy College of Business Administration">McCoy College of Business Administration</option>
                    <option value="Education">Education</option>
                    <option value="Fine Arts and Communication">Fine Arts and Communication</option>
                    <option value="Health Professions">Health Professions</option>
                    <option value="Liberal Arts">Liberal Arts</option>
                    <option value="Science and Engineering">Science and Engineering</option>
                </select>

*******************************************************************************************************

2. This part of code is for creating the results table that i have mentioned in the README file
   this is what i have worked on sprint 3.

*******************************************************************************************************
-----------------------------------
CSS design code below for table:
-----------------------------------

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}

--------------------------------------
HTML design code below for table:
--------------------------------------

<div id="show"></div>
    <div id="sbh" style="visibility: hidden">
        <h1 style="margin-left:230px;margin-top:80px;">Search Results</h1>
        <div style="margin-left:-60px;margin-right:80px;margin-top:80px;">
            <table>
                  <tr>
                    <th>Book Name</th>
                    <th>CourseId</th>
                    <th>Department</th>
                  </tr>
				  {% for book in results %}
				     <tr>
						 <td>{{ book['Book Name'] }}</td>
						 <td>{{ book['Course_ID'] }}</td>
						 <td>{{ book['Department'] }}</td>
					 </tr>
				  {% endfor %}
            </table>
        </div>
    </div>

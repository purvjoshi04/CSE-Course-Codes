 //getDate() method
 let day=new Date();
 console.log(day.getDate());
 /*
 The getDate() method returns the day of the month (1 to 31) of a date.
 
 output:
 1
 */
 
 //getDay() method
 console.log(day.getDay());
 /*
 The getDay() method returns the day of the week (0 to 6) of a date.
 
 output:
 3
 3=wedenesday
 */
 
 //getFullYear() method
 console.log(day.getFullYear());
 /*
 getFullYear() returns the full year (4 digits) of a date.
 
 output:
 2023
 */
 
 //getHours() method
 console.log(day.getHours());
 
 /*
 getHours() returns the hour (0 to 23) of a date.
 
 output:
 14
 */
 
 //getMilliseconds() method
 console.log(day.getMilliseconds());
 
 /*
 getMilliseconds() returns the milliseconds (0 to 999) of a date.
 
 output:
 558
 */
 
 //getMinutes() method
 console.log(day.getMinutes());
 
 /*
 getMinutes() returns the minutes (0 to 59) of a date.
 
 output:
 6
 */
 
 //getMonth() method
 console.log(day.getMonth());
 
 /*
 getMonth() returns the month (0 to 11) of a date.
 
 output:
 1
 1=february
 */
 
 //getSeconds() method
 console.log(day.getSeconds());
 
 /*
 getSeconds() returns the seconds (0 to 59) of a date.
 
 output:
 32
 */
 
 //getTime() method
 console.log(day.getTime());
 
 /*
 getTime() returns the number of milliseconds since January 1, 1970 00:00:00.
 
 output;
 1675260727057
 */
 
 //setDate() method 
 day.setDate(1);
 console.log(day);
 /*
 setDate() sets the day of the month of a date.
 
 output:
 2023-02-01T16:27:44.221Z
 */
 
 //setFullYear() method
 day.setFullYear(2021);
 console.log(day);
 /*
 setFullYear() sets the year of a date.
 
 setFullYear() can also set month and day.
  output:
  2021-02-01T16:29:24.079Z
  */
 
 //setHours() method
 day.setHours(13);
 console.log(day);
 
 /*
 setHours() sets the hour of a date.
 
 setHours() can also set minutes, seconds and milliseconds.
 
 output:
 2021-02-01T13:31:28.560Z
 */
 
 //setMilliseconds method
 day.setMilliseconds(120);
 console.log(day);
 
 /*
 setMilliseconds() sets the milliseconds of a date.
 
 output:
 2021-02-01T13:33:46.120Z
 */
 
 //setMinutes method
 day.setMinutes(55);
 console.log(day);
 
 /*
 getMinutes() returns the minutes (0 to 59) of a date.
 
 output:
 2021-02-01T13:55:35.120Z
 */
 
 //setMonth() method
 day.setMonth(4);
 console.log(day);
 
 /*
 The setMonth() method sets the month of a date object.
 
 Note: January is 0, February is 1, and so on.
 
 This method can also be used to set the day of the month.
 
 output:
 2021-05-01T13:55:56.120Z
 */
 
 //setSeconds() method
 day.setSeconds(20);
 console.log(day);
 
 /*
 The setSeconds() method sets the seconds of a date object.
 
 This method can also be used to set the milliseconds.
 
 output:
 2021-05-01T13:55:20.120Z
 */
 
 //setTime() method
 day.setTime(1332403882588);
 console.log(day);
 
 /*
 The setTime() method sets a date and time by adding or subtracting a specified number of milliseconds to/from midnight January 1, 1970.
 
 output:
 2012-03-22T08:11:22.588Z
 */
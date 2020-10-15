function scheduleAgenda() {
  var spreadsheet = SpreadsheetApp.getActiveSheet();
  var calendarId = spreadsheet.getRange("c4").getValue();
  var eventCal = CalendarApp.getCalendarById(calendarId);

  var signups = spreadsheet.getRange("A6:C25").getValues();

  for (x=0; x<signups.length; x++){

    var schedule = signups[x];

    var startTime = schedule[0];
    var endTime = schedule[1];
    var agenda = schedule[2];

    eventCal.createEvent(agenda, startTime, endTime);
  }


}

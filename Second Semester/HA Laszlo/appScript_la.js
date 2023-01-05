function newForm() {
  var sheet = SpreadsheetApp.getActive();
  var values = sheet.getDataRange().getValues();
  var last_row = values[values.length - 1];

  if (last_row[0]) return;

  var form = FormApp.create("New form");

  var clebrity = last_row.slice(1);

  form
    .addGridItem()
    .setTitle("Rate artists")
    .setRows(clebrity)
    .setColumns([1, 2, 3, 4, 5]);

  sheet.getRange("A" + sheet.getLastRow()).setValue(form.getId());
  Logger.log("Form ID: " + form.getId());
  ScriptApp.newTrigger("average").forForm(form.getId()).onFormSubmit().create();
}

function average() {
  const docs = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = docs.getSheets()[0];
  var values = sheet.getDataRange().getValues();
  var last_row = values[values.length - 1];

  var form = FormApp.openById(last_row[0]);
  var respons = form.getResponses();
  var respondentsNum = [];

  var sums = [],
    i = 0;

  while (i < last_row.length - 1) {
    sums.push(0);
    respondentsNum.push(0);
    i++;
  }

  for (const element of respons) {
    var itemResponses = element.getItemResponses();

    for (var j = 0; j < itemResponses.length; j++) {
      var itemResponse = itemResponses[j];
      var votesOfArtists = itemResponse.getResponse();

      for (var k = 0; k < votesOfArtists.length; k++) {
        if (votesOfArtists[k]) {
          sums[k] += parseInt(votesOfArtists[k]);
          respondentsNum[k] += 1;
        }
      }
    }
  }

  for (var i = 0; i < last_row.length - 1; i++) {
    var cc = sheet.getRange(2, i + 2);
    if (respondentsNum[i]) cc.setValue(sums[i] / respondentsNum[i]);
    else cc.setValue(0);
  }
}

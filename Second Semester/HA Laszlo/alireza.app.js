function myFunction() {
  var sheet = SpreadsheetApp.openById(getId("TopRanks"));

  var triggers = ScriptApp.getProjectTriggers();
  for (var i = 0; i < triggers.length; i++)
    ScriptApp.deleteTrigger(triggers[i]);

  createForm();

  ScriptApp.newTrigger("createForm")
    .forSpreadsheet(sheet.getId())
    .onChange()
    .create();
}

function createForm() {
  var sheet = SpreadsheetApp.openById(getId("TopRanks"));
  var values = sheet.getDataRange().getValues();
  var last_row = values[values.length - 1];
  var form_name = last_rank_name();

  var form = last_row[0]
    ? FormApp.openById(last_row[0])
    : FormApp.create(form_name);

  if (!last_row[0]) {
    for (var i = 3; i < last_row.length; i++) {
      form
        .addMultipleChoiceItem()
        .setTitle(last_row[i])
        .setChoiceValues(["1", "2", "3", "4", "5"])
        .showOtherOption(false);
    }
  }

  var responseForm = last_row[1]
    ? SpreadsheetApp.openById(last_row[1])
    : SpreadsheetApp.create(form_name + " (response)");

  sheet.getRange("A" + sheet.getLastRow()).setValue(form.getId());
  sheet.getRange("B" + sheet.getLastRow()).setValue(responseForm.getId());

  ScriptApp.newTrigger("formSubmit")
    .forForm(form.getId())
    .onFormSubmit()
    .create();
}

function formSubmit() {
  var sheet = SpreadsheetApp.openById(getId("TopRanks"));
  var values = sheet.getDataRange().getValues();

  for (var i = 0; i < values.length; i++) {
    var formId = values[i][0];
    var responseId = values[i][1];
    if (!formId || !responseId) continue;
    saveResponse(formId, responseId);
  }
}

function saveResponse(formId, responseId) {
  var form = FormApp.openById(formId);
  var response = SpreadsheetApp.openById(responseId);

  var formResponses = form.getResponses();

  for (var k = 0; k < form.getItems().length; k++) {
    var row = String.fromCharCode(67 + k);
    response.getSheets()[0].getRange(2, 2).setValue("Average");
    response
      .getSheets()[0]
      .getRange(1, k + 3)
      .setValue(form.getItems()[k].getTitle());
    var cell_formula =
      "=IF(COUNT(" +
      row +
      "3:" +
      row +
      "),AVERAGE(" +
      row +
      "3:" +
      row +
      "),0)";
    response
      .getSheets()[0]
      .getRange(2, k + 3)
      .setValue(cell_formula);
  }

  for (var i = 0; i < formResponses.length; i++) {
    var formResponse = formResponses[i];
    var itemResponses = formResponse.getItemResponses();
    response
      .getSheets()[0]
      .getRange(i + 3, 1)
      .setValue((i + 1).toString());
    response
      .getSheets()[0]
      .getRange(i + 3, 2)
      .setValue(formResponse.getTimestamp());
    for (var j = 0; j < itemResponses.length; j++) {
      var itemResponse = itemResponses[j];
      for (var k = 0; k < form.getItems().length; k++) {
        if (
          form.getItems()[k].getTitle() == itemResponse.getItem().getTitle()
        ) {
          response
            .getSheets()[0]
            .getRange(i + 3, k + 3)
            .setValue(itemResponse.getResponse());
        }
      }
    }
  }
}

function getId(name) {
  var myFiles = DriveApp.searchFiles('"me" in owners');
  var result = "";
  while (myFiles.hasNext()) {
    var file = myFiles.next();
    if (file.getName() == name) result = file.getId();
  }
  return result;
}

function last_rank_name() {
  var sheet = SpreadsheetApp.openById(getId("TopRanks"));
  var data = sheet.getDataRange().getValues();
  var last_row = data.pop();
  var name = new Date(last_row[2]);
  name = name.toISOString();
  name = name.slice(0, 10);
  return name;
}

function myFunction() {
  const docs = SpreadsheetApp.getActiveSpreadsheet()
  creation();

  ScriptApp.newTrigger("creation")
  .forSpreadsheet(docs.getId()) 
  .onChange() 
    .create();
    
}
function creation() {
  const docs = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = docs.getSheets()[0];
  const range = sheet.getDataRange();
  var values = range.getValues();
  var artist = values[values.length-2]
  if (artist[0]){
    return
      }
  artist = artist.slice(1);
  
  var form = FormApp.create('Billboard');
  form.addGridItem()
      .setTitle('Rate artists')
      .setRows(artist)
      .setColumns([1, 2, 3, 4, 5]);

      sheet.getRange("A" + (docs.getLastRow()-1)).setValue(form.getId());

      ScriptApp.newTrigger("average")
      .forForm(form.getId())
      .onFormSubmit()
      .create();
  Logger.log('Published URL: ' + form.getPublishedUrl());
  Logger.log('Editor URL: ' + form.getEditUrl());
}

function average() {
  const docs = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = docs.getSheets()[0];
  const range = sheet.getDataRange();
  const values = range.getValues();
  const artists = values[values.length-2];

  var form = FormApp.openById(artists[0]);
  var respons = form.getResponses();
  var respondentsNum = [];

  var sums = [], i = 0;

  while (i < artists.length) {
    sums.push(0);
    respondentsNum.push(0)
    i++;
  }
  
  for (const element of respons) {
    var itemResponses = element.getItemResponses();
    for (var j = 0; j < itemResponses.length; j++) {
      var itemResponse = itemResponses[j];
      var votesOfArtists = itemResponse.getResponse();

      for (var k = 0; k < votesOfArtists.length; k++) {
        if (votesOfArtists[k]){
          sums[k] += parseInt(votesOfArtists[k]);
        respondentsNum[k]+= 1
        }  
      }
    }
  }
  for (var i = 0; i < artists.length-1; i++) {
    var cell = sheet.getRange(2,i+2); 
    if (respondentsNum[i])
      cell.setValue(sums[i] / respondentsNum[i]);
    else cell.setValue(0);
  }
  }



















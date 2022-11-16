function myFunction() {
    // Google Sheet > Spread Sheet (active) > Sheet > Range > Cell
  
    let app = SpreadsheetApp;
    let ss = app.getActiveSpreadsheet();
    let activeSheet = ss.getActiveSheet(); // ss.getSheetByName
    let cell = activeSheet.getRange('B3');
   
    cell.setValue(777); // getValue()
  
    let cell2 = activeSheet.getRange(2, 3); // row_num, col_num 
    cell2.setValue(888);
  
    let range = activeSheet.getRange('E5:G7');
    range.setValue(555);
  
    // B9 - E12 : set the diagonals to 2 (from 1)
    for(i=0;i<4;i++){
      let actual_cell = activeSheet.getRange(i+9, i+2);
      actual_cell.setValue(actual_cell.getValue() + 1);
    } 
  }
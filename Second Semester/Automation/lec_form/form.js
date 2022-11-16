function get_last_id(col_num){
    let idx = 1;
  
    while(SpreadsheetApp.getActiveSheet().getRange(idx, col_num).getValue() != ''){
      idx++;
    }
  
    return idx-1;
  }
  
  function define_question_fields(form, activeSheet, col_num){
      switch(col_num){
        case 1:
          create_date_question(form, activeSheet, col_num);
          break;
        case 2:
        case 3:
          create_choice_question(form, activeSheet, col_num);
          break;
        case 4:
          create_rating_question(form, activeSheet, col_num);
          break;
      }
  
  }
  
  function create_date_question(form, activeSheet, col_num){
    form.addDateItem().setTitle(activeSheet.getRange(1, col_num).getValue());
    form.addPageBreakItem().setTitle('Start to fill it...');
  
  }
  
  function create_choice_question(form, activeSheet, col_num){
    var item = form.addCheckboxItem();
    item.setTitle(activeSheet.getRange(1, col_num).getValue());
    let last_id = get_last_id(col_num);
  
    choices = Array(last_id-1);
    for(row_num=2; row_num <= last_id; row_num++){
      choices[row_num-2] = item.createChoice(activeSheet.getRange(row_num, col_num).getValue());
    }
    item.setChoices(choices);
  }
  
  function create_rating_question(form, activeSheet, col_num){
    let last_id = get_last_id(col_num);
  
    valueArr = [];
    for(i=1; i<=last_id; i++){
      let value = activeSheet.getRange(i, col_num).getValue();
      valueArr.push(value);
    }
    let end_index = valueArr.indexOf("END");
  
    if(end_index === -1 ){
      throw Error("No end was given");
    }
  
    form.addGridItem()
       .setTitle(valueArr[0])
       .setRows(valueArr.slice(1, end_index))
       .setColumns(valueArr.slice(end_index+1, valueArr.length));
  
  }
  
  
  function myFunction() {
    var form = FormApp.create('Questionnaire');
    let sheet = SpreadsheetApp;
    let ss = sheet.getActiveSpreadsheet();
    let activeSheet = ss.getSheetByName('skeleton');
  
    let last_col = activeSheet.getLastColumn();
    for (col_num = 1; col_num <= last_col; col_num++) {
      define_question_fields(form, activeSheet, col_num);    
  
    }
  
    Logger.log('Published URL: ' + form.getPublishedUrl());
  
  
  }
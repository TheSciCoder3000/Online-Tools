window.onkeydown = function(e){
  if (e.ctrlKey && e.which == 66){// Bold HK
    bold_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 73 && !(e.shiftKey)){// Italic HK
    italic_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 85){// Underline HK
    underline_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 72){// Highlight HK
    highlight_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.altKey && e.which == 68){// Delete column
    e.preventDefault();
    delete_cell();
  }
  if (e.ctrlKey && e.shiftKey && e.which == 82) {// Add row
    e.preventDefault();
    add_row();
  }
  if (e.ctrlKey && e.shiftKey && e.which == 67) {//Add Column
    e.preventDefault();
    add_column();
  }
}

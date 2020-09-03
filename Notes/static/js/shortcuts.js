window.onkeydown = function(e){
  if (e.which == 17){
    e.preventDefault();
    window.ctrl_pressed = true;
  }
  if (e.ctrlKey && e.which == 66){// Bold HK
    bold_text();
    e.preventDefault();
  }
  if (e.ctrlKey && e.which == 83){// Bold HK
    save_changes();
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
  if (e.which == 65) {//Add File
    var folder = document.activeElement.parentNode.parentNode;
    var child_container = folder.querySelector('div');
    if (child_container.classList.toString() == "child-container") {
      e.preventDefault();
      window.selector = folder
      document.querySelector('#modal-container').style.display = "block";
      document.querySelector('#modal-text').innerHTML = "Put the name of your file down below";
      document.querySelector('#folder-root').value = folder.getAttribute('foldername');
      document.querySelector('#modal-form-btn').setAttribute('rootFolder', get_root_folder(folder))
      document.querySelector('#modal-form-btn').setAttribute('Foldername', folder.getAttribute('foldername'))
      document.querySelector('#modal-form-btn').setAttribute('create', 'File')
    }
  }
  if (e.shiftKey && e.which == 65) {//Add Folder
    var folder = document.activeElement.parentNode.parentNode;
    var child_container = folder.querySelector('div');
    if (child_container.classList.toString() == "child-container") {
      e.preventDefault();
      window.selector = folder
      document.querySelector('#modal-container').style.display = "block";
      document.querySelector('#modal-text').innerHTML = "Put the name of your folder down below";
      document.querySelector('#folder-root').value = folder.getAttribute('foldername');
      document.querySelector('#modal-form-btn').setAttribute('rootFolder', get_root_folder(folder))
      document.querySelector('#modal-form-btn').setAttribute('Foldername', folder.getAttribute('foldername'))
      document.querySelector('#modal-form-btn').setAttribute('create', 'Folder')
    }
  }
  if (e.which == 46){//Delete Folder
    var objects = document.querySelectorAll('.obj-selected');
    for (var i = 0; i < objects.length; i++) {
      var object = objects[i]
      var root_obj = object.parentNode.parentNode
      window.selector = root_obj
      function get_objName(obj) {
        if (obj.getAttribute('Foldername')){
          return obj.getAttribute('Foldername')
        } else{
          return obj.getAttribute('Filename')
        }
      }
      delete_obj(object.getAttribute('type'),
                 root_obj.parentNode.parentNode.getAttribute('Foldername'),
                 root_obj.getAttribute('Foldername'),
                 get_objName(object));
    }

    }
}

window.onkeyup = function (e){
  if (e.which == 17){
    window.ctrl_pressed = false;
  }
}
